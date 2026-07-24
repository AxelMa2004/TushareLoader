'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-06-17
FilePath: /TushareLoader/futures_loader.py
Description: 期货专题数据
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *
import time


class FutBasic(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='fut_basic.parquet')

    def _load_data(self):
        dfs = []
        for exchange in ['DCE', 'CZCE', 'SHFE', 'CFFEX', 'INE']:
            dfs.append(pro.fut_basic(exchange=exchange))
        return pd.concat(dfs).rename(columns={'ts_code': 'InnerCode'})


class FutDaily(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='fut_daily.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fut_daily(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class FutHolding(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='fut_holding.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fut_holding(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class FutWsr(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='fut_wsr.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fut_wsr(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class FutMapping(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='fut_mapping.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fut_mapping(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class FutSettle(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='fut_settle.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fut_settle(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class FutWeeklyMonthly(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='fut_weekly_monthly.parquet')

    def _load_data(self):
        dfs = []
        for freq in ['1', '2']:
            df = pro.fut_weekly_monthly(freq=freq, start_date=START, end_date=END)
            if len(df) > 0:
                dfs.append(df)
            time.sleep(0.5)
        return pd.concat(dfs).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})

