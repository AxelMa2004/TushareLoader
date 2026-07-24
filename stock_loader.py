'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-04-05 00:40:25
FilePath: /TushareLoader/stock_loader.py
Description: 
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *

class StockInfo(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="stock_info.parquet")
    def _load_data(self):
        return pro.stock_basic().rename(columns={'ts_code': 'InnerCode'})

 
class StockDailyLoader(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="stock_daily.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        data1 = pro.daily(trade_date=date_str)
        data2 = pro.daily_basic(trade_date=date_str).drop(columns=['close'])
        data3 = pro.adj_factor(trade_date=date_str)
        time.sleep(0.05)
        return pd.merge(data1, data2, on=['ts_code','trade_date'], how='left').\
            merge(data3, on=['ts_code','trade_date'], how='left').\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})



class StockStklimit(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="stk_limit.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.stk_limit(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})


class StockSuspension(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="suspension.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.suspend_d(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})



class StockMoneyFlow(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="money_flow.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.moneyflow(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})



class StockTopList(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="top_list.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.top_list(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})


class StockTopinst(TushareLoaderTSIterative):
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str=START, end: str=END):
        super().__init__(file_name="top_inst.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.top_inst(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})


