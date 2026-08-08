'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-04-11 09:49:18
FilePath: /TushareLoader/index.py
Description: 
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *
from tqdm import tqdm

# 常用指数 TS_CODE 列表 (纯A股，含宽基、行业、策略及转债)
index_list = [
    # --- 综合与宽基核心 ---
    "000001.SH",  # 上证指数 (新增)
    "000016.SH",  # 上证50
    "000300.SH",  # 沪深300
    "000905.SH",  # 中证500
    "000852.SH",  # 中证1000
    "000019.SH",  # 上证180
    "399006.SZ",  # 创业板指
    "000688.SH",  # 科创50
    "399989.SZ",  # 中证A500
    "899050.BJ",  # 北证50
    "000985.CSI", # 中证全指

    # --- 价值与策略 ---
    "000922.SH",  # 中证红利
    "399965.SZ",  # 红利低波 (或 399391 等)
    "000015.SH",  # 上证红利
    "399996.SZ",  # 沪深300价值
    "399998.SZ",  # 沪深300成长
    "399303.SZ",  # 深证红利 (补充一个深市红利)

    # --- 债券市场 ---
    "000832.SH",  # 中证转债 (新增)

    # --- 金融板块 ---
    "399986.SZ",  # 中证银行
    "399975.SZ",  # 证券公司
    "399973.SZ",  # 中证全指保险
    "399991.SZ",  # 非银金融

    # --- 消费与医药 ---
    "399987.SZ",  # 中证酒
    "399997.SZ",  # 中证白酒
    "399990.SZ",  # 中证消费
    "399991.SZ",  # 中证医药
    "399995.SZ",  # 医疗器械
    "399992.SZ",  # 生物医药

    # --- 科技与新能源 ---
    "399976.SZ",  # 新能源车
    "399981.SZ",  # 电子50 (或 中证电子)
    "399985.SZ",  # 计算机
    "399993.SZ",  # 5G通信
    "399994.SZ",  # 人工智能
    "399996.SZ",  # 芯片产业 (国证芯片)
    "399988.SZ",  # 军工指数

    # --- 周期与资源 ---
    "399983.SZ",  # 中证煤炭
    "399982.SZ",  # 中证钢铁
    "399984.SZ",  # 有色金属
    "399989.SZ",  # 房地产
    "399990.SZ",  # 全指能源
    "399980.SZ",  # 中证环保 (补充一个环保/碳中和方向)
]

class IndexInfo(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="index_info.parquet")
    def _load_data(self):
        return pro.index_basic().rename(columns={'ts_code': 'InnerCode'})


class IndexDailyLoader(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="index_daily.parquet")
    def _load_data(self):
        dfs = []
        for index in tqdm(index_list, desc="Loading index daily data"):
            data = pro.index_daily(ts_code=index).rename(columns={'ts_code': 'InnerCode','trade_date':'TradingDay'})
            dfs.append(data)

        res = pd.concat(dfs)
        index_info = pro.index_basic(fields=['ts_code', 'name']).rename(columns={'ts_code': 'InnerCode'})
        return pd.merge(res, index_info, on='InnerCode', how='left')


class IndexClassify(ProductionConstant):
    """指数分类与权重"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="index_classify.parquet")

    def _load_data(self):
        return pro.index_classify().rename(columns={'index_code': 'InnerCode'})


class IndexMember(ProductionConstant):
    """指数成份股"""
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="index_member.parquet")

    def _load_data(self):
        dfs = []
        for index in tqdm(index_list, desc="Loading index members"):
            df = pro.index_member(index_code=index)
            if len(df) > 0:
                dfs.append(df)
        if len(dfs) == 0:
            return pd.DataFrame()
        return pd.concat(dfs).rename(columns={'index_code': 'InnerCode', 'con_code': 'StockCode'})

class IndexWeight(ProductionConstant):
    """获取各指数月度成分股权重，需 >=2000 积分。

    首次运行从 2010 年全量拉取，后续仅增量。
    """
    def __init__(self):
        super().__init__(dir_name="tushare", file_name="index_weight.parquet")
        self.year_start = 2010

    def _load_data(self):
        dfs = []
        today_int = int(datetime.datetime.now().strftime("%Y"))
        existing_max = None

        if os.path.exists(self.path):
            existing = pd.read_parquet(self.path)
            existing_max = str(existing["trade_date"].max())[:4]
        start_year = self.year_start if existing_max is None else int(existing_max)

        for index in tqdm(index_list, desc="Loading index weights"):
            for year in range(start_year, today_int + 1):
                try:
                    df = pro.index_weight(
                        index_code=index,
                        start_date="%d0101" % year,
                        end_date="%d1231" % year,
                    )
                    if len(df) > 0:
                        dfs.append(df)
                except Exception:
                    time.sleep(0.5)
                    continue
                time.sleep(0.35)

        if len(dfs) == 0:
            return pd.DataFrame()

        new_data = pd.concat(dfs, ignore_index=True)
        new_data = new_data.rename(
            columns={"index_code": "InnerCode", "con_code": "StockCode"}
        )

        if os.path.exists(self.path):
            existing = pd.read_parquet(self.path)
            combined = pd.concat([existing, new_data], ignore_index=True)
            combined = combined.drop_duplicates(
                subset=["InnerCode", "StockCode", "trade_date"], keep="last"
            )
            return combined.sort_values("trade_date").reset_index(drop=True)

        return new_data.sort_values("trade_date").reset_index(drop=True)
