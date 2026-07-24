'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-04-05 13:33:01
FilePath: /TushareLoader/fundamental.py
Description: 
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tracemalloc import start

from tushare_loader import *


class Income(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="income.parquet", start=start, end=end, \
                         canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                        date_col='end_date')

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.income_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode'})
    
class Balance(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="balance.parquet", start=start, end=end, \
                         canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                        date_col='end_date')

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.balancesheet_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode','period':'TradingDay'})
    
class Cashflow(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="cashflow.parquet", start=start, end=end, \
                            canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                            date_col='end_date')
    
    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.cashflow_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode','period':'TradingDay'})
    

class Forecast(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="forecast.parquet", start=start, end=end, \
                         canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                        date_col='end_date')

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.forecast_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode','period':'TradingDay'})
    

class Express(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="express.parquet", start=start, end=end, \
                         canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                        date_col='end_date')
        
    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.express_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode','period':'TradingDay'})  

    
class FinaIndicator(TushareLoaderTSIterative):
    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="fina_indicator.parquet", start=start, end=end, \
                         canlendar_path='./toolkits/production/fundamental_canlendar.csv', \
                        date_col='end_date')
        
    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.fina_indicator_vip(period=date_str).\
            rename(columns={'ts_code': 'InnerCode','period':'TradingDay'})  