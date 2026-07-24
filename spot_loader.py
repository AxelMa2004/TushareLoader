'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-06-17
FilePath: /TushareLoader/spot_loader.py
Description: 现货/商品数据
  南华商品指数日行情、上海黄金/SGE黄金现货行情
  上海黄金基础信息
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *


NH_INDEX_CODES = [
    'NH0100.NHF',
    'NH0200.NHF',
    'NH0300.NHF',
    'NH0400.NHF',
    'NH0500.NHF',
    'NH0600.NHF',
]


class NhIndexDaily(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='nh_index_daily.parquet')

    def _load_data(self):
        dfs = []
        for code in NH_INDEX_CODES:
            dfs.append(pro.index_daily(ts_code=code))
        return pd.concat(dfs).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class SpotSge(TushareLoaderTSIterative):
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name='sge_daily.parquet', start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.sge_daily(trade_date=date_str).rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class SgeBasic(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='sge_basic.parquet')

    def _load_data(self):
        return pro.sge_basic().rename(columns={'ts_code': 'InnerCode'})

