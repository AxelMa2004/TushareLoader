'''
Author: Codex
Date: 2026-06-16
FilePath: /TushareLoader/load_bond.py
Description: 债券专题数据加载器
  可转债（基础信息、日行情、发行、利率、评级、十大持有人、赎回、转股）
  大宗交易、大宗交易明细
  国债收益率曲线
  全球财经事件
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *


# ================== 可转债（常量表） ==================

class CbBasic(ProductionConstant):
    """可转债基础信息"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_basic.parquet")

    def _load_data(self):
        return pro.cb_basic().rename(columns={'ts_code': 'InnerCode'})


class CbIssue(ProductionConstant):
    """可转债发行数据"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_issue.parquet")

    def _load_data(self):
        return pro.cb_issue().rename(columns={'ts_code': 'InnerCode'})


class CbRate(ProductionConstant):
    """可转债票面利率"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_rate.parquet")

    def _load_data(self):
        return pro.cb_rate().rename(columns={'ts_code': 'InnerCode'})


class CbRating(ProductionConstant):
    """可转债债券评级（逐个转债代码+延时防限流）"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_rating.parquet")

    def _load_data(self):
        """????????????????"""
        existing_codes = set()
        existing_df = None
        if os.path.exists(self.path):
            existing_df = pd.read_parquet(self.path)
            existing_codes = set(existing_df['InnerCode'].tolist())
        all_codes = pro.cb_basic(fields='ts_code')['ts_code'].tolist()
        new_codes = [c for c in all_codes if c not in existing_codes]
        if not new_codes:
            self.logger.info('No new bonds to fetch for rating, skipping...')
            return existing_df if existing_df is not None else pd.DataFrame()
        dfs = []
        for i, code in enumerate(new_codes):
            df = pro.cb_rating(ts_code=code)
            if len(df) > 0:
                dfs.append(df)
            time.sleep(0.35)
            if (i + 1) % 100 == 0:
                self.logger.info(f"CbRating progress: {i+1}/{len(new_codes)}")
        new_data = pd.concat(dfs).rename(columns={'ts_code': 'InnerCode'}) if dfs else pd.DataFrame()
        if existing_df is not None and not existing_df.empty:
            return pd.concat([existing_df, new_data])
        return new_data



class CbCall(ProductionConstant):
    """可转债赎回信息（逐个转债代码+延时防限流）"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_call.parquet")

    def _load_data(self):
        return load_incremental_by_date(
            path=self.path,
            fetch_fn=lambda start_date, end_date: pro.cb_call(start_date=start_date, end_date=end_date),
            date_col='ann_date',
            id_cols=['InnerCode', 'ann_date', 'call_type'],
            logger=self.logger,
        )
class CbShare(ProductionConstant):
    """可转债转股结果"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="cb_share.parquet")

    def _load_data(self):
        return load_incremental_by_date(
            path=self.path,
            fetch_fn=lambda start_date, end_date: pro.cb_share(start_date=start_date, end_date=end_date),
            date_col='publish_date',
            id_cols=['InnerCode', 'publish_date'],
            logger=self.logger,
        )
class CbDaily(TushareLoaderTSIterative):
    """可转债日线行情（逐日拉取）"""
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name="cb_daily.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.cb_daily(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


# ================== 大宗交易 ==================

class BondBlk(TushareLoaderTSIterative):
    """沪深交易所债券大宗交易"""
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name="bond_blk.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.bond_blk(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


class BondBlkDetail(TushareLoaderTSIterative):
    """沪深交易所债券大宗交易明细"""
    def __init__(self, start: str = START, end: str = END):
        super().__init__(file_name="bond_blk_detail.parquet", start=start, end=end)

    def _append_data_date_raw(self, d):
        date_str = d.strftime('%Y%m%d')
        return pro.bond_blk_detail(trade_date=date_str).\
            rename(columns={'ts_code': 'InnerCode', 'trade_date': 'TradingDay'})


# ================== 国债收益率曲线 ==================

class YcCb(ProductionConstant):
    """中证债券收益率曲线"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="yc_cb.parquet")

    def _load_data(self):
        return pro.yc_cb().rename(columns={'ts_code': 'InnerCode'})


# ================== 全球财经事件 ==================

class EcoCal(ProductionConstant):
    """全球财经日历与经济事件"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="eco_cal.parquet")

    def _load_data(self):
        return pro.eco_cal()
