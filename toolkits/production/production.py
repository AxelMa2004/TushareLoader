from __future__ import annotations

import os
from abc import ABC, abstractmethod
from datetime import date, datetime
import logging
from typing import Any

import duckdb
import pandas as pd
import polars as pl
from tqdm import tqdm

from toolkits.logger import get_logger
from toolkits.tasklog import is_updated_today, update_record

data_root = os.getenv("DATA_ROOT") if os.getenv("DATA_ROOT") is not None else "./data"


def _coerce_date(value: date | datetime | str | pd.Timestamp | Any) -> date:
    """Normalize calendar / parquet values to ``datetime.date``."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, pd.Timestamp):
        return value.to_pydatetime().date()
    if isinstance(value, str):
        s = value.strip()
        if len(s) == 8 and s.isdigit():
            return datetime.strptime(s, "%Y%m%d").date()
        return pd.to_datetime(s, errors="raise").date()
    # numpy datetime64, etc.
    return pd.to_datetime(value, errors="raise").date()


def _series_to_dates(series: pd.Series) -> set[date]:
    out: set[date] = set()
    for v in series:
        out.add(_coerce_date(v))
    return out


class ProductionBase(ABC):
    def __init__(
        self,
        dir_name: str,
        file_name: str,
        logger: logging.Logger | None = None,
        mode: str = "pandas",
    ):
        self.path = os.path.join(data_root, dir_name, file_name).replace("\\", "/")
        os.makedirs(os.path.join(data_root, dir_name).replace("\\", "/"), exist_ok=True)
        self.logger = (
            logger
            if logger is not None
            else get_logger(name=file_name, filename=file_name, ifconsole=True)
        )

    @abstractmethod
    def run(self):
        pass


class ProductionConstant(ProductionBase):
    def __init__(self, dir_name: str, file_name: str, logger: logging.Logger | None = None):
        super().__init__(dir_name, file_name, logger)

    @abstractmethod
    def _load_data(self) -> pd.DataFrame | str | pl.DataFrame:
        pass

    def run(self):
        # Derive record name from path (e.g. "data/tushare/stock_info.parquet" → "stock_info")
        record_name = os.path.splitext(os.path.basename(self.path))[0]

        if is_updated_today(record_name):
            self.logger.info(f"⏭️  Skip [{record_name}]: Already executed successfully today")
            return

        try:
            data = self._load_data()
            if isinstance(data, pd.DataFrame):
                data.to_parquet(self.path)
            elif isinstance(data, str):
                duckdb.sql(f"copy (select * from {data}) to '{self.path}' (format 'parquet')")
            elif isinstance(data, pl.DataFrame):
                data.write_parquet(self.path)
            else:
                raise ValueError(f"Invalid data type: {type(data)}")

            self.logger.info(f"Successfully saved data to {self.path}!")
            update_record(record_name, status='success')
        except Exception:
            update_record(record_name, status='failed')
            raise


class ProductionTimeseries(ProductionBase):
    def __init__(
        self,
        dir_name: str,
        file_name: str,
        start: date | datetime | str | pd.Timestamp,
        end: date | datetime | str | pd.Timestamp,
        canlendar_path: str = "./toolkits/production/canlendar.csv",
        logger: logging.Logger | None = None,
        date_col: str = "TradingDay",
        desc: str = "Appending data",
    ):
        super().__init__(dir_name, file_name, logger)
        self.start = _coerce_date(start)
        self.end = _coerce_date(end)
        self.date_col = date_col
        self.missing_date: list[date] = self._cal_missing_date(canlendar_path)
        self.desc = desc

    @abstractmethod
    def _append_data(self) -> pd.DataFrame | str | pl.DataFrame:
        pass

    def _load_existing_data(self) -> set[date]:
        if os.path.exists(self.path):
            duckdb.sql(
                f"create or replace table ori_data as select * from read_parquet('{self.path}')"
            )
            existing_date = duckdb.sql(
                f"select distinct {self.date_col} from ori_data"
            ).df()
            return _series_to_dates(existing_date[self.date_col])
        return set()

    def _load_canlendar(self, canlendar_path: str) -> set[date]:
        cal = pd.read_csv(canlendar_path, dtype={"TradingDay": str})
        cal["_d"] = cal["TradingDay"].map(lambda s: _coerce_date(s))
        mask = (cal["_d"] >= self.start) & (cal["_d"] <= self.end)
        return set(cal.loc[mask, "_d"].tolist())

    def _cal_missing_date(self, canlendar_path: str) -> list[date]:
        existing_date = self._load_existing_data()
        if len(existing_date) == 0:
            return sorted(self._load_canlendar(canlendar_path))
        canlendar_date = self._load_canlendar(canlendar_path)
        missing_date = canlendar_date - existing_date
        return sorted(missing_date)

    def run(self):
        if len(self.missing_date) > 0:
            self.logger.info(f"Missing {len(self.missing_date)} dates, appending...")
            data = self._append_data()

            if isinstance(data, pd.DataFrame):
                duckdb.register("data", data)
            elif isinstance(data, str):
                duckdb.sql(f"create or replace table data as select * from {data}")
            elif isinstance(data, pl.DataFrame):
                duckdb.register("data", data)
            else:
                raise ValueError(f"Invalid data type: {type(data)}")

            if os.path.exists(self.path):
                duckdb.sql(
                    f"create or replace table ori_data as select * from read_parquet('{self.path}')"
                )
                duckdb.sql(
                    f"create or replace table ori_data as select * from ori_data union all "
                    f"select * from data order by {self.date_col}"
                )
            else:
                duckdb.sql(
                    f"create or replace table ori_data as select * from data order by {self.date_col}"
                )
            duckdb.sql(f"copy (select * from ori_data) to '{self.path}' (format 'parquet')")
            self.logger.info(
                f"Successfully appended {len(self.missing_date)} new dates to {self.path}!"
            )
        else:
            self.logger.info("No missing dates, skipping...")


class ProductionTimeseriesIterative(ProductionTimeseries):
    def __init__(
        self,
        dir_name: str,
        file_name: str,
        start: date | datetime | str | pd.Timestamp,
        end: date | datetime | str | pd.Timestamp,
        canlendar_path: str = "./toolkits/production/canlendar.csv",
        logger: logging.Logger | None = None,
        date_col: str = "TradingDay",
        desc: str | None = None,
        if_tqdm: bool = True,
    ):
        super().__init__(
            dir_name, file_name, start, end, canlendar_path, logger, date_col
        )
        self.desc = desc if desc is not None else f"Appending data for {file_name}"
        self.if_tqdm = if_tqdm

    @abstractmethod
    def _append_data_date(self, d: date) -> pd.DataFrame | str | pl.DataFrame:
        pass

    def _append_data(self) -> pd.DataFrame | str | pl.DataFrame:
        results = []
        for d in tqdm(
            self.missing_date,
            desc=f"[{self.desc}] Appending data",
            disable=not self.if_tqdm,
        ):
            data = self._append_data_date(d)
            results.append(data)

        if isinstance(results[0], pd.DataFrame):
            return pd.concat(results)
        if isinstance(results[0], str):
            union_sql = " UNION ALL ".join(f"select * from {t}" for t in results)
            duckdb.sql(f"create or replace table _tmp_iter_union as {union_sql}")
            return "_tmp_iter_union"
        if isinstance(results[0], pl.DataFrame):
            return pl.concat(results)
        raise ValueError(f"Invalid data type: {type(results[0])}")
