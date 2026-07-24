''' 
Author: Qimin Ma
Date: 2026-04-03 21:52:32
LastEditTime: 2026-06-17
FilePath: /TushareLoader/main.py
Description: 
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from stock_loader import *
from stock_extra import *
from stock_factor import *
from fundamental import *
from toolkits.production.read import read_timeseries, read_constant
from index import *
from load_bond import *
from futures_loader import *
from spot_loader import *
from macro_loader import *


if __name__ == '__main__':
    # ========== 股票基础 ==========
    stock_info = StockInfo()
    stock_info.run()

    stock_daily_loader = StockDailyLoader(start='20040101')
    stock_daily_loader.run()

    stock_stklimit = StockStklimit(start='20130101')
    stock_stklimit.run()

    suspension = StockSuspension(start='20130101')
    suspension.run()

    # ========== 股票额外 ==========
    stock_weekly = StockWeekly(start='20040101')
    stock_weekly.run()

    stock_monthly = StockMonthly(start='20040101')
    stock_monthly.run()

    name_change = NameChange()
    name_change.run()

    hs_const = HsConst()
    hs_const.run()

    margin_detail = MarginDetail(start='20100401')
    margin_detail.run()

    repurchase = Repurchase()
    repurchase.run()

    # ========== 股票因子 ==========
    stk_holdernumber = StkHoldernumber()
    stk_holdernumber.run()
    block_trade = BlockTrade(start='20260101')
    block_trade.run()
    limit_list_d = LimitListD(start='20260101')
    limit_list_d.run()
    ggt_daily = GgtDaily(start='20260101')
    ggt_daily.run()
    stk_account = StkAccount()
    stk_account.run()
    # stk_shock = StkShock(start='20260101')  # 无接口权限
    # stk_shock.run()

    # ========== 基本�?==========
    income = Income(start='20080101')
    income.run()

    balance = Balance(start='20080101')
    balance.run()

    cashflow = Cashflow(start='20080101')
    cashflow.run()

    forecast = Forecast(start='20080101')
    forecast.run()

    express = Express(start='20080101')
    express.run()

    fina_indicator = FinaIndicator(start='20080101')
    fina_indicator.run()

    # ========== 资金流向 ==========
    money_flow = StockMoneyFlow(start='20130101')
    money_flow.run()

    top_list = StockTopList(start='20130101')
    top_list.run()

    top_inst = StockTopinst(start='20130101')
    top_inst.run()

    # ========== 指数 ==========
    index_info = IndexInfo()
    index_info.run()

    index_daily_loader = IndexDailyLoader()
    index_daily_loader.run()

    index_classify = IndexClassify()
    index_classify.run()

    index_member = IndexMember()
    index_member.run()

    # ========== 债券 ==========
    cb_basic = CbBasic()
    cb_basic.run()
    cb_daily = CbDaily(start='20200101')
    cb_daily.run()
    cb_issue = CbIssue()
    cb_issue.run()
    cb_rate = CbRate()
    cb_rate.run()
    cb_rating = CbRating()
    cb_rating.run()

    # ========== 可转债补充数据 ==========
    cb_call = CbCall()
    cb_call.run()
    top10_holders = Top10CbHolders()
    top10_holders.run()
    cb_share = CbShare()
    cb_share.run()
    cb_adj = CbAdj()
    cb_adj.run()
    cb_pre_conv = CbPreConv()
    cb_pre_conv.run()

    # ========== 全球经济日历 ==========
    eco_cal = EcoCal()
    eco_cal.run()

    # ========== 期货 ==========
    fut_basic = FutBasic()
    fut_basic.run()
    fut_daily = FutDaily(start='20250101')
    fut_daily.run()
    fut_holding = FutHolding(start='20250101')
    fut_holding.run()
    fut_wsr = FutWsr(start='20250101')
    fut_wsr.run()
    fut_mapping = FutMapping(start='20250101')
    fut_mapping.run()
    fut_settle = FutSettle(start='20250101')
    fut_settle.run()

    # ========== 现货 ==========
    sge_basic = SgeBasic()
    sge_basic.run()
    nh_index_daily = NhIndexDaily()
    nh_index_daily.run()
    spot_sge = SpotSge(start='20220101')
    spot_sge.run()

    # ========== 宏观经济 ==========
    money_supply = MoneySupply()
    money_supply.run()

    cpi = Cpi()
    cpi.run()

    ppi = Ppi()
    ppi.run()

    pmi = Pmi()
    pmi.run()

    gdp = Gdp()
    gdp.run()

    social_finance = SocialFinance()
    social_finance.run()

    lpr = Lpr()
    lpr.run()

    cn_schedule = CnSchedule()
    cn_schedule.run()
    hibor = Hibor()
    hibor.run()
    libor = Libor()
    libor.run()
    shibor = Shibor()
    shibor.run()
    shibor_quote = ShiborQuote()
    shibor_quote.run()
    gz_index = GzIndex()
    gz_index.run()
    wz_index = WzIndex()
    wz_index.run()
    us_trycr = UsTrycr()
    us_trycr.run()
    us_tycr = UsTycr()
    us_tycr.run()

    print('Done!')
