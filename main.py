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



def safe_run(loader, name):
    """安全运行包装器，失败时记录错误但不中断整体流程"""
    try:
        loader.run()
    except Exception as e:
        print("[ERROR] %s: %s" % (name, e))
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # ========== 股票基础 ==========
    stock_info = StockInfo()
    safe_run(stock_info, "stock_info")

    stock_daily_loader = StockDailyLoader(start='20040101')
    safe_run(stock_daily_loader, "stock_daily_loader")

    stock_stklimit = StockStklimit(start='20130101')
    safe_run(stock_stklimit, "stock_stklimit")

    suspension = StockSuspension(start='20130101')
    safe_run(suspension, "suspension")

    # ========== 股票额外 ==========
    stock_weekly = StockWeekly(start='20040101')
    safe_run(stock_weekly, "stock_weekly")

    stock_monthly = StockMonthly(start='20040101')
    safe_run(stock_monthly, "stock_monthly")

    name_change = NameChange()
    safe_run(name_change, "name_change")

    hs_const = HsConst()
    safe_run(hs_const, "hs_const")

    margin_detail = MarginDetail(start='20100401')
    safe_run(margin_detail, "margin_detail")

    repurchase = Repurchase()
    safe_run(repurchase, "repurchase")

    # ========== 股票因子 ==========
    stk_holdernumber = StkHoldernumber()
    safe_run(stk_holdernumber, "stk_holdernumber")
    block_trade = BlockTrade(start='20260101')
    safe_run(block_trade, "block_trade")
    limit_list_d = LimitListD(start='20260101')
    safe_run(limit_list_d, "limit_list_d")
    ggt_daily = GgtDaily(start='20260101')
    safe_run(ggt_daily, "ggt_daily")
    stk_account = StkAccount()
    safe_run(stk_account, "stk_account")
    # stk_shock = StkShock(start='20260101')  # 无接口权限
    # stk_shock.run()

    # ========== 基本�?==========
    income = Income(start='20080101')
    safe_run(income, "income")

    balance = Balance(start='20080101')
    safe_run(balance, "balance")

    cashflow = Cashflow(start='20080101')
    safe_run(cashflow, "cashflow")

    forecast = Forecast(start='20080101')
    safe_run(forecast, "forecast")

    express = Express(start='20080101')
    safe_run(express, "express")

    fina_indicator = FinaIndicator(start='20080101')
    safe_run(fina_indicator, "fina_indicator")

    # ========== 资金流向 ==========
    money_flow = StockMoneyFlow(start='20130101')
    safe_run(money_flow, "money_flow")

    top_list = StockTopList(start='20130101')
    safe_run(top_list, "top_list")

    top_inst = StockTopinst(start='20130101')
    safe_run(top_inst, "top_inst")

    # ========== 指数 ==========
    index_info = IndexInfo()
    safe_run(index_info, "index_info")

    index_daily_loader = IndexDailyLoader()
    safe_run(index_daily_loader, "index_daily_loader")

    index_classify = IndexClassify()
    safe_run(index_classify, "index_classify")

    index_member = IndexMember()
    safe_run(index_member, "index_member")

    index_weight = IndexWeight()
    safe_run(index_weight, "index_weight")

    # ========== 债券 ==========
    cb_basic = CbBasic()
    safe_run(cb_basic, "cb_basic")
    cb_daily = CbDaily(start='20200101')
    safe_run(cb_daily, "cb_daily")
    cb_issue = CbIssue()
    safe_run(cb_issue, "cb_issue")
    cb_rate = CbRate()
    safe_run(cb_rate, "cb_rate")
    cb_rating = CbRating()
    safe_run(cb_rating, "cb_rating")

    # ========== 可转债补充数据 ==========
    cb_call = CbCall()
    safe_run(cb_call, "cb_call")
    cb_share = CbShare()
    safe_run(cb_share, "cb_share")

    # ========== 全球经济日历 ==========
    eco_cal = EcoCal()
    safe_run(eco_cal, "eco_cal")

    # ========== 期货 ==========
    fut_basic = FutBasic()
    safe_run(fut_basic, "fut_basic")
    fut_daily = FutDaily(start='20180101')
    safe_run(fut_daily, "fut_daily")
    fut_holding = FutHolding(start='20180101')
    safe_run(fut_holding, "fut_holding")
    fut_wsr = FutWsr(start='20180101')
    safe_run(fut_wsr, "fut_wsr")
    fut_mapping = FutMapping(start='20180101')
    safe_run(fut_mapping, "fut_mapping")
    fut_settle = FutSettle(start='20180101')
    safe_run(fut_settle, "fut_settle")

    # ========== 现货 ==========
    sge_basic = SgeBasic()
    safe_run(sge_basic, "sge_basic")
    nh_index_daily = NhIndexDaily()
    safe_run(nh_index_daily, "nh_index_daily")
    spot_sge = SpotSge(start='20220101')
    safe_run(spot_sge, "spot_sge")

    # ========== 宏观经济 ==========
    money_supply = MoneySupply()
    safe_run(money_supply, "money_supply")

    cpi = Cpi()
    safe_run(cpi, "cpi")

    ppi = Ppi()
    safe_run(ppi, "ppi")

    pmi = Pmi()
    safe_run(pmi, "pmi")

    gdp = Gdp()
    safe_run(gdp, "gdp")

    social_finance = SocialFinance()
    safe_run(social_finance, "social_finance")

    lpr = Lpr()
    safe_run(lpr, "lpr")

    cn_schedule = CnSchedule()
    safe_run(cn_schedule, "cn_schedule")
    hibor = Hibor()
    safe_run(hibor, "hibor")
    libor = Libor()
    safe_run(libor, "libor")
    shibor = Shibor()
    safe_run(shibor, "shibor")
    shibor_quote = ShiborQuote()
    safe_run(shibor_quote, "shibor_quote")
    gz_index = GzIndex()
    safe_run(gz_index, "gz_index")
    wz_index = WzIndex()
    safe_run(wz_index, "wz_index")
    us_trycr = UsTrycr()
    safe_run(us_trycr, "us_trycr")
    us_tycr = UsTycr()
    safe_run(us_tycr, "us_tycr")

    print('Done!')