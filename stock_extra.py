'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-06-12 21:00:00
FilePath: /TushareLoader/stock_extra.py
Description: 股票剩余数据：周线、月线、曾用名、沪深港通、融资融券明细、管理层薪酬、回购
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *


# ================== 周线/月线行情 ==================

class StockWeekly(TushareLoaderTSIterative):
    """A股周线行情（仅在每周最后一个交易日有数据）"""
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name="stock_weekly.parquet", start=start, end=end,
                         canlendar_path='./toolkits/production/weekly_canlendar.csv')

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.weekly(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class StockMonthly(TushareLoaderTSIterative):
    """A股月线行情（仅在每月最后一个交易日有数据）"""
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name="stock_monthly.parquet", start=start, end=end,
                         canlendar_path='./toolkits/production/monthly_canlendar.csv')

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.monthly(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


# ================== 基础信息（常量表） ==================

class NameChange(ProductionConstant):
    """股票曾用名"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="namechange.parquet")

    def _load_data(self):
        return pro.namechange().rename(columns={'ts_code': 'InnerCode'})


class HsConst(ProductionConstant):
    """沪深港通成份股"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="hs_const.parquet")

    def _load_data(self):
        dfs = []
        for hs_type in ['SH', 'SZ']:
            dfs.append(pro.hs_const(hs_type=hs_type))
        return pd.concat(dfs).rename(columns={'ts_code': 'InnerCode'})


# ================== 融资融券明细（逐日） ==================

class MarginDetail(TushareLoaderTSIterative):
    """融资融券交易明细"""
    rate_limit = 500  # 500 calls/min

    def __init__(self, start: str = '20100401', end: str = END):
        super().__init__(file_name="margin_detail.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.margin_detail(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


# ================== 管理层薪酬 ==================

class StkRewards(ProductionConstant):
    """管理层薪酬与持股（遍历全量股票，每个ts_code一次调用）"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="stk_rewards.parquet")

    def _load_data(self):
        codes = pro.stock_basic(fields='ts_code')['ts_code'].tolist()
        dfs = []
        for i, code in enumerate(codes):
            df = pro.stk_rewards(ts_code=code)
            if len(df) > 0:
                dfs.append(df)
            if (i + 1) % 100 == 0:
                self.logger.info(f"StkRewards progress: {i+1}/{len(codes)}")
        return pd.concat(dfs).rename(columns={'ts_code': 'InnerCode'})


# ================== 股票回购 ==================

class Repurchase(ProductionConstant):
    """股票回购"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="repurchase.parquet")

    def _load_data(self):
        return pro.repurchase().rename(columns={'ts_code': 'InnerCode'})