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
sleeptime = [0.1, 0.2, 1]

class TushareLoaderTSIterative(ProductionTimeseriesIterative):
    def __init__(self, file_name: str, start: str=START, end: str=END, \
                 canlendar_path: str='./toolkits/production/canlendar.csv', \
                date_col:str='TradingDay'):
        super().__init__(file_name=file_name, start=start, end=end, dir_name="tushare", 
                         canlendar_path=canlendar_path, date_col=date_col)

    @abstractmethod
    def _append_data_date_raw(self, d):
        pass

    def _append_data_date(self, d):
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