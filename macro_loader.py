'''
Author: Qimin Ma
Date: 2026-04-03 21:38:25
LastEditTime: 2026-06-17
FilePath: /TushareLoader/macro_loader.py
Description: 宏观经济专题数据
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from tushare_loader import *


class MoneySupply(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_money_supply.parquet')

    def _load_data(self):
        return pro.cn_m(start_m=START[:6], end_m=END[:6])


class Cpi(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_cpi.parquet')

    def _load_data(self):
        return pro.cn_cpi(start_m=START[:6], end_m=END[:6])


class Ppi(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_ppi.parquet')

    def _load_data(self):
        return pro.cn_ppi(start_m=START[:6], end_m=END[:6])


class Pmi(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_pmi.parquet')

    def _load_data(self):
        return pro.cn_pmi(start_m=START[:6], end_m=END[:6])


class Gdp(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_gdp.parquet')

    def _load_data(self):
        return pro.cn_gdp(start_q=START[:4] + '1Q', end_q=END[:4] + '4Q')


class SocialFinance(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_social_financing.parquet')

    def _load_data(self):
        return pro.sf_month(start_m=START[:6], end_m=END[:6])


class Lpr(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_lpr.parquet')

    def _load_data(self):
        return pro.shibor_lpr()


# ================== 新增宏观经济加载器 ==================

class CnSchedule(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='cn_schedule.parquet')

    def _load_data(self):
        return pro.cn_schedule()


class Hibor(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='hibor.parquet')

    def _load_data(self):
        return pro.hibor()


class Libor(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='libor.parquet')

    def _load_data(self):
        return pro.libor()


class Shibor(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='shibor.parquet')

    def _load_data(self):
        return pro.shibor()


class ShiborQuote(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='shibor_quote.parquet')

    def _load_data(self):
        return pro.shibor_quote()


class GzIndex(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='gz_index.parquet')

    def _load_data(self):
        return pro.gz_index()


class WzIndex(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='wz_index.parquet')

    def _load_data(self):
        return pro.wz_index()


class UsTrycr(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='us_trycr.parquet')

    def _load_data(self):
        return pro.us_trycr()


class UsTycr(ProductionConstant):
    def __init__(self):
        super().__init__(dir_name='tushare', file_name='us_tycr.parquet')

    def _load_data(self):
        return pro.us_tycr()

