'''
Author: Codex
Date: 2026-06-17
FilePath: /TushareLoader/stock_factor.py
Description: 股票因子与市场数据
  股东人数、大宗交易、涨停板列表、沪深港通、开户数据、异常波动
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *


class StkHoldernumber(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='stk_holdernumber.parquet')

    def _load_data(self):
        return pro.stk_holdernumber().rename(columns={'ts_code': 'InnerCode'})


class BlockTrade(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='block_trade.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.block_trade(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class LimitListD(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='limit_list_d.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.limit_list_d(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class GgtDaily(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='ggt_daily.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.ggt_daily(trade_date=date_str).rename(columns={'trade_date': 'TradingDay'})


class StkAccount(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='stk_account.parquet')

    def _load_data(self):
        return pro.stk_account()


class StkShock(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='stk_shock.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.stk_shock(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})

