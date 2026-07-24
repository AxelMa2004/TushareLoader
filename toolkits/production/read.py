from __future__ import annotations

import os
from datetime import date, datetime

import duckdb
import pandas as pd
import polars as pl

from toolkits.production.production import _coerce_date

data_root = os.getenv("DATA_ROOT") if os.getenv("DATA_ROOT") is not None else "./data"

DateLike = date | datetime | str | pd.Timestamp

_INTEGER_DTYPES = frozenset(
    {
        pl.Int8,
        pl.Int16,
        pl.Int32,
        pl.Int64,
        pl.UInt8,
        pl.UInt16,
        pl.UInt32,
        pl.UInt64,
    }
)


def _polars_normalize_read_date(col_name: str, dtype: pl.DataType) -> pl.Expr:
    """Tushare 存量常为 ``YYYYMMDD`` 字符串；不能直接 ``cast(Datetime)``，需解析为 ``Date``。"""
    c = pl.col(col_name)
    if dtype == pl.Date:
        return c.alias(col_name)
    if isinstance(dtype, pl.Datetime):
        return c.dt.date().alias(col_name)
    if dtype in _INTEGER_DTYPES:
        return c.cast(pl.Utf8).str.zfill(8).str.to_date("%Y%m%d", strict=False).alias(col_name)
    cs = c.cast(pl.Utf8).str.strip_chars()
    return pl.coalesce(
        cs.str.to_date("%Y%m%d", strict=False),
        cs.str.to_date("%Y-%m-%d", strict=False),
    ).alias(col_name)


def read_constant(
    dir_name: str,
    file_name: str,
    mode: str = "pandas",
    table_name: str = "data",
) -> pd.DataFrame | pl.DataFrame | None:
    path = os.path.join(data_root, dir_name, file_name).replace("\\", "/")
    if mode == "pandas":
        return pd.read_parquet(path)
    if mode == "polars":
        return pl.read_parquet(path)
    if mode == "duckdb":
        duckdb.sql(
            f"create or replace table {table_name} as select * from read_parquet('{path}')"
        )
        return None
    raise ValueError(f"Invalid mode: {mode}")


def read_timeseries(
    dir_name: str,
    file_name: str,
    start: DateLike,
    end: DateLike,
    mode: str = "pandas",
    table_name: str = "data",
    date_col: str = "TradingDay",
    required_cols: list[str] | None = None,
    sort_by: list[str] | None = None,
    lazy: bool = False,
) -> pd.DataFrame | pl.DataFrame | pl.LazyFrame | None:
    """按 ``[start, end]``（含端点）按**日历日**筛选；``start``/``end`` 与 ``production`` 一样支持 ``date`` / 字符串等。

    ``required_cols`` 非空时，在日期筛选之后只保留这些列（须含 ``date_col`` 若仍需该列）。

    ``sort_by`` 非空时，在返回前按给定列排序（Polars 下进入 lazy 计划；用于组内 rolling 时应包含股票标识与时间列；Pandas 使用稳定排序；``duckdb`` 模式忽略此项）。

    ``lazy=True``（仅 ``mode='polars'``）时返回 ``LazyFrame``，不 ``collect``；其它 ``mode`` 下传 ``lazy=True`` 会报错。"""
    start_d = _coerce_date(start)
    end_d = _coerce_date(end)
    path = os.path.join(data_root, dir_name, file_name).replace("\\", "/")

    if lazy and mode != "polars":
        raise ValueError("read_timeseries(lazy=True) is only supported for mode='polars'")

    if mode == "pandas":
        data = pd.read_parquet(path)
        ts = pd.to_datetime(data[date_col])
        day = ts.dt.normalize()
        m = (day >= pd.Timestamp(start_d)) & (day <= pd.Timestamp(end_d))
        data = data.loc[m]
        if required_cols is not None:
            data = data[required_cols]
        if sort_by is not None:
            data = data.sort_values(sort_by, kind="mergesort")
        return data

    if mode == "polars":
        lf = pl.scan_parquet(path)
        if required_cols is not None:
            pre_cols = list(dict.fromkeys([date_col, *required_cols]))
            lf = lf.select(pre_cols)
        sch = lf.collect_schema()[date_col]
        lf = lf.with_columns(_polars_normalize_read_date(date_col, sch))
        d = pl.col(date_col)
        lf = lf.filter((d >= pl.lit(start_d)) & (d <= pl.lit(end_d)))
        if required_cols is not None:
            lf = lf.select(required_cols)
        if sort_by is not None:
            lf = lf.sort(sort_by)
        if lazy:
            return lf
        return lf.collect()

    if mode == "duckdb":
        select_list = ", ".join(required_cols) if required_cols is not None else "*"
        duckdb.sql(
            f"""
            create or replace table {table_name} as
            select {select_list} from read_parquet('{path}')
            where cast({date_col} as date) >= date '{start_d.isoformat()}'
              and cast({date_col} as date) <= date '{end_d.isoformat()}'
            """
        )
        return None

    raise ValueError(f"Invalid mode: {mode}")
