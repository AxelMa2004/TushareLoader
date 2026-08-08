'''
Author: Qimin Ma
Date: 2026-04-03 21:39:29
LastEditTime: 2026-04-05 13:32:26
FilePath: /TushareLoader/tushare_loader.py
Description: 
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
import pandas as pd
import tushare as ts
from dotenv import load_dotenv
import os
import datetime
from toolkits.production.production import ProductionTimeseries, \
    ProductionConstant, ProductionTimeseriesIterative
from abc import abstractmethod
from toolkits.tasklog import daily_run
from toolkits.logger.logger import get_logger
import time

load_dotenv()

ts.set_token(os.getenv("TUSHARE_API_KEY"))
pro = ts.pro_api()
START = '20040101'
END = datetime.datetime.now().strftime('%Y%m%d')

# Create canlander:
@daily_run(name="create_canlendar", logger=get_logger(name="create_canlendar"))
def create_canlendar():
    canlendar = pro.trade_cal(start_date=START, end_date=END, exchange='SSE', \
        is_open=1, fields='pretrade_date').sort_values(by='pretrade_date')
    canlendar.columns = ['TradingDay']
    canlendar.to_csv('./toolkits/production/canlendar.csv', index=False)

@daily_run(name="create_fundamental_canlendar", logger=get_logger(name="create_fundamental_canlendar"))
def create_fundamental_canlendar():
    # Select those with month-date in 0331, 0630, 0930, 1231
    canlendar = pro.trade_cal(start_date=START, end_date=END, exchange='SSE', \
        fields='pretrade_date').sort_values(by='pretrade_date')
    mmdd = canlendar['pretrade_date'].astype(str).str[4:]
    canlendar = canlendar[mmdd.isin(['0331', '0630', '0930', '1231'])][['pretrade_date']]
    canlendar.columns = ['TradingDay']
    canlendar.drop_duplicates(inplace=True)
    canlendar.sort_values(by='TradingDay', inplace=True)
    canlendar.to_csv('./toolkits/production/fundamental_canlendar.csv', index=False)

# sleep time:

@daily_run(name="create_monthly_canlendar", logger=get_logger(name="create_monthly_canlendar"))
def create_monthly_canlendar():
    """月度交易日历：每月最后一个交易日"""
    canlendar = pd.read_csv("./toolkits/production/canlendar.csv")
    canlendar["ym"] = canlendar["TradingDay"].astype(str).str[:6]
    monthly = canlendar.groupby('ym', as_index=False)['TradingDay'].last()
    monthly[["TradingDay"]].to_csv("./toolkits/production/monthly_canlendar.csv", index=False)


@daily_run(name="create_weekly_canlendar", logger=get_logger(name="create_weekly_canlendar"))
def create_weekly_canlendar():
    """周度交易日历：每周最后一个交易日"""
    canlendar = pd.read_csv("./toolkits/production/canlendar.csv")
    canlendar["dt"] = pd.to_datetime(canlendar["TradingDay"].astype(str))
    iso = canlendar["dt"].dt.isocalendar()
    canlendar["yw"] = iso["year"].astype(str) + "-W" + iso["week"].astype(str).str.zfill(2)
    weekly = canlendar.groupby("yw", as_index=False)["TradingDay"].last()
    weekly[["TradingDay"]].to_csv("./toolkits/production/weekly_canlendar.csv", index=False)


sleeptime = [0.1, 0.2, 1]


def load_incremental_by_date(path, fetch_fn, date_col='publish_date', id_cols=None, logger=None):
    """通用日期增量加载帮助函数
    已有数据时：取最新日期，仅拉增量
    首次加载：按年份批量拉取
    """
    if os.path.exists(path):
        existing = pd.read_parquet(path)
        latest_dt = pd.to_datetime(existing[date_col]).max()
        latest = latest_dt.strftime('%Y%m%d')
        today = datetime.datetime.now().strftime('%Y%m%d')

        if latest >= today:
            if logger:
                logger.info('Already up to date (latest: %s)' % latest)
            return existing

        if logger:
            logger.info('Fetching records since %s...' % latest)
        new_df = fetch_fn(start_date=latest, end_date=today)
        if new_df is None or len(new_df) == 0:
            if logger:
                logger.info('No new records')
            return existing

        new_df = new_df.rename(columns={'ts_code': 'InnerCode'})
        combined = pd.concat([existing, new_df], ignore_index=True)
        if id_cols:
            combined = combined.drop_duplicates(subset=id_cols)
        combined = combined.sort_values(date_col).reset_index(drop=True)
        return combined

    if logger:
        logger.info('First run: fetching by year batches...')
    all_data = []
    for year in range(2018, 2027):
        df = fetch_fn(start_date='%d0101' % year, end_date='%d1231' % year)
        if df is not None and len(df) > 0:
            all_data.append(df)
        time.sleep(0.5)
        if logger:
            logger.info('  Year %d: %d records' % (year, len(df) if df is not None else 0))

    if not all_data:
        return pd.DataFrame()
    result = pd.concat(all_data, ignore_index=True).rename(columns={'ts_code': 'InnerCode'})
    return result.sort_values(date_col).reset_index(drop=True)

class TushareLoaderTSIterative(ProductionTimeseriesIterative):
    def __init__(self, file_name: str, start: str=START, end: str=END, \
                 canlendar_path: str='./toolkits/production/canlendar.csv', \
                date_col:str='TradingDay'):
        super().__init__(file_name=file_name, start=start, end=end, dir_name="tushare", 
                         canlendar_path=canlendar_path, date_col=date_col)

    def __init__(self, file_name, start=START, end=END, canlendar_path="./toolkits/production/canlendar.csv", date_col="TradingDay", rate_limit_sleep=0.35):
        super().__init__(file_name=file_name, start=start, end=end, dir_name="tushare", canlendar_path=canlendar_path, date_col=date_col)
        self.rate_limit_sleep = rate_limit_sleep

    @abstractmethod
    def _append_data_date_raw(self, d):
        pass

    def _append_data_date(self, d):
        time.sleep(self.rate_limit_sleep)
        df = self._append_data_date_raw(d)
        if len(df) == 0:
            for sleep_time in sleeptime:
                df = self._append_data_date_raw(d)
                if len(df) > 0:
                    break
                time.sleep(sleep_time)
                if sleep_time == sleeptime[-1]:
                    self.logger.warning(f"Failed to append data for {d} after {sleep_time} seconds, skip it.")
        return df

create_canlendar()
create_fundamental_canlendar()
create_monthly_canlendar()
create_weekly_canlendar()