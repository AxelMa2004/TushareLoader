# tushare — MCP 工具文档

> 自动生成 | 工具总数: 258 | 生成时间: 2026-06-15 00:25

---

## 目录

- [沪深股票](#沪深股票) (120 个工具)
- [股票数据](#股票数据) (4 个工具)
- [指数](#指数) (7 个工具)
- [指数专题](#指数专题) (13 个工具)
- [ETF专题](#ETF专题) (9 个工具)
- [公募基金](#公募基金) (8 个工具)
- [期货](#期货) (5 个工具)
- [期货数据](#期货数据) (6 个工具)
- [期权](#期权) (3 个工具)
- [期权数据](#期权数据) (1 个工具)
- [港股](#港股) (4 个工具)
- [港股数据](#港股数据) (8 个工具)
- [美股](#美股) (3 个工具)
- [美股数据](#美股数据) (6 个工具)
- [债券](#债券) (12 个工具)
- [债券专题](#债券专题) (5 个工具)
- [宏观经济](#宏观经济) (19 个工具)
- [行业经济](#行业经济) (8 个工具)
- [外汇](#外汇) (1 个工具)
- [外汇数据](#外汇数据) (1 个工具)
- [另类数据](#另类数据) (4 个工具)
- [大模型语料专题数据](#大模型语料专题数据) (6 个工具)
- [现货](#现货) (1 个工具)
- [现货数据](#现货数据) (1 个工具)
- [财富管理](#财富管理) (1 个工具)
- [小佩数据](#小佩数据) (2 个工具)

---

## 沪深股票

共 120 个工具

### slb_len_mm
**分类**: 沪深股票 > 两融及转融通 > 做市借券交易汇总(停）-做市借券交易汇总

**说明**: /数据接口/沪深股票/两融及转融通/做市借券交易汇总(停）-做市借券交易汇总

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, ope_inv, lent_qnt, cls_inv, end_bal 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `ope_inv` | (默认返回) |
| `lent_qnt` | (默认返回) |
| `cls_inv` | (默认返回) |
| `end_bal` | (默认返回) |

---

### margin_detail
**分类**: 沪深股票 > 两融及转融通 > 融资融券交易明细-获取沪深两市每日融资融券明细

**说明**: /数据接口/沪深股票/两融及转融通/融资融券交易明细-获取沪深两市每日融资融券明细

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, rzye, rqye, rzmre, rqyl, rzche, rqchl, rqmcl, rzrqye 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `rzye` | (默认返回) |
| `rqye` | (默认返回) |
| `rzmre` | (默认返回) |
| `rqyl` | (默认返回) |
| `rzche` | (默认返回) |
| `rqchl` | (默认返回) |
| `rqmcl` | (默认返回) |
| `rzrqye` | (默认返回) |

---

### margin
**分类**: 沪深股票 > 两融及转融通 > 融资融券交易汇总-获取融资融券每日交易汇总数据

**说明**: /数据接口/沪深股票/两融及转融通/融资融券交易汇总-获取融资融券每日交易汇总数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange_id` | string | 否 | 交易所代码（SSE上交所SZSE深交所BSE北交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, exchange_id, rzye, rzmre, rzche, rqye, rqmcl, rzrqye, rqyl 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `exchange_id` | (默认返回) |
| `rzye` | (默认返回) |
| `rzmre` | (默认返回) |
| `rzche` | (默认返回) |
| `rqye` | (默认返回) |
| `rqmcl` | (默认返回) |
| `rzrqye` | (默认返回) |
| `rqyl` | (默认返回) |

---

### margin_secs
**分类**: 沪深股票 > 两融及转融通 > 融资融券标的（盘前）-获取沪深京三大交易所融资融券标的（包括ETF），每天盘前更新

**说明**: /数据接口/沪深股票/两融及转融通/融资融券标的（盘前）-获取沪深京三大交易所融资融券标的（包括ETF），每天盘前更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所（SSE上交所 SZSE深交所 BSE北交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, exchange 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日 |
| `ts_code` | string | 否 | 标的代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `exchange` | (默认返回) |

---

### slb_sec_detail
**分类**: 沪深股票 > 两融及转融通 > 转融券交易明细(停）-转融券交易明细

**说明**: /数据接口/沪深股票/两融及转融通/转融券交易明细(停）-转融券交易明细

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, tenor, fee_rate, lent_qnt 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `tenor` | (默认返回) |
| `fee_rate` | (默认返回) |
| `lent_qnt` | (默认返回) |

---

### slb_sec
**分类**: 沪深股票 > 两融及转融通 > 转融券交易汇总(停）-转融通转融券交易汇总

**说明**: /数据接口/沪深股票/两融及转融通/转融券交易汇总(停）-转融通转融券交易汇总

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, ope_inv, lent_qnt, cls_inv, end_bal 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `ope_inv` | (默认返回) |
| `lent_qnt` | (默认返回) |
| `cls_inv` | (默认返回) |
| `end_bal` | (默认返回) |

---

### slb_len
**分类**: 沪深股票 > 两融及转融通 > 转融资交易汇总-转融通融资汇总

**说明**: /数据接口/沪深股票/两融及转融通/转融资交易汇总-转融通融资汇总

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ob, auc_amount, repo_amount, repay_amount, cb 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ob` | (默认返回) |
| `auc_amount` | (默认返回) |
| `repo_amount` | (默认返回) |
| `repay_amount` | (默认返回) |
| `cb` | (默认返回) |

---

### stk_high_shock
**分类**: 沪深股票 > 参考数据 > 个股严重异常波动-根据证券交易所交易规则的有关规定，交易所每日发布股票交易严重异常波动情况

**说明**: /数据接口/沪深股票/参考数据/个股严重异常波动-根据证券交易所交易规则的有关规定，交易所每日发布股票交易严重异常波动情况

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD格式）示例:20260312 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, trade_market, reason, period 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期（YYYYMMDD格式）示例:20260312 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式）示例:20260312 |
| `ts_code` | string | 否 | 股票代码（可以通过stock_basic获取）示例:000001.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `trade_market` | (默认返回) |
| `reason` | (默认返回) |
| `period` | (默认返回) |

---

### stk_shock
**分类**: 沪深股票 > 参考数据 > 个股异常波动-根据证券交易所交易规则的有关规定，交易所每日发布股票交易异常波动情况

**说明**: /数据接口/沪深股票/参考数据/个股异常波动-根据证券交易所交易规则的有关规定，交易所每日发布股票交易异常波动情况

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD格式）示例:20260312 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, trade_market, reason, period 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期（YYYYMMDD格式）示例:20260312 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式）示例:20260312 |
| `ts_code` | string | 否 | 股票代码（可以通过stock_basic获取）示例:000001.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `trade_market` | (默认返回) |
| `reason` | (默认返回) |
| `period` | (默认返回) |

---

### stk_alert
**分类**: 沪深股票 > 参考数据 > 交易所重点提示证券-根据证券交易所交易规则的有关规定，交易所每日发布重点提示证券

**说明**: /数据接口/沪深股票/参考数据/交易所重点提示证券-根据证券交易所交易规则的有关规定，交易所每日发布重点提示证券

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD格式）示例:20260312 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, start_date, end_date, type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期（YYYYMMDD格式）示例:20260312 |
| `trade_date` | string | 否 | 交易所重点提示起始日期（YYYYMMDD格式）示例:20260312 |
| `ts_code` | string | 否 | 股票代码（可以通过stock_basic获取）示例:000001.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `start_date` | (默认返回) |
| `end_date` | (默认返回) |
| `type` | (默认返回) |

---

### top10_floatholders
**分类**: 沪深股票 > 参考数据 > 前十大流通股东-获取上市公司前十大流通股东数据

**说明**: /数据接口/沪深股票/参考数据/前十大流通股东-获取上市公司前十大流通股东数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, holder_name, hold_amount, hold_ratio, hold_float_ratio, hold_change, holder_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期（YYYYMMDD格式，一般为每个季度最后一天） |
| `start_date` | string | 否 | 报告期开始日期 |
| `ts_code` | string | 是 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `holder_name` | (默认返回) |
| `hold_amount` | (默认返回) |
| `hold_ratio` | (默认返回) |
| `hold_float_ratio` | (默认返回) |
| `hold_change` | (默认返回) |
| `holder_type` | (默认返回) |

---

### concept
**分类**: 沪深股票 > 参考数据 > 概念股分类表-获取概念股分类，目前只有ts一个来源，未来将逐步增加来源

**说明**: /数据接口/沪深股票/参考数据/概念股分类表-获取概念股分类，目前只有ts一个来源，未来将逐步增加来源

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: code, name, src 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `src` | string | 否 | 来源，默认为ts |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `code` | (默认返回) |
| `name` | (默认返回) |
| `src` | (默认返回) |

---

### concept_detail
**分类**: 沪深股票 > 参考数据 > 概念股明细列表-获取概念股分类明细数据

**说明**: /数据接口/沪深股票/参考数据/概念股明细列表-获取概念股分类明细数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: id, concept_name, ts_code, name 额外可选字段:   in_date: 纳入日期   out_date: 剔除日期 |
| `id` | string | 否 | 概念分类ID （id来自概念股分类接口） |
| `ts_code` | string | 否 | 股票代码  （以上参数二选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `id` | (默认返回) |
| `concept_name` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `in_date` | 纳入日期 |
| `out_date` | 剔除日期 |

---

### stk_holdernumber
**分类**: 沪深股票 > 参考数据 > 股东人数-获取上市公司股东户数数据，数据不定期公布

**说明**: /数据接口/沪深股票/参考数据/股东人数-获取上市公司股东户数数据，数据不定期公布

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 公告结束日期 |
| `enddate` | string | 否 | 截止日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, holder_num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | TS股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `holder_num` | (默认返回) |

---

### margin_target
**分类**: 沪深股票 > 参考数据 > 融资融券标的(下线)-获取全市场融资融券标的

**说明**: /数据接口/沪深股票/参考数据/融资融券标的(下线)-获取全市场融资融券标的

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, mg_type, is_new, in_date, out_date, ann_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_new` | string | 否 | 是否最新 |
| `mg_type` | string | 否 | 标的类型：B买入标的 S卖出标的 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `mg_type` | (默认返回) |
| `is_new` | (默认返回) |
| `in_date` | (默认返回) |
| `out_date` | (默认返回) |
| `ann_date` | (默认返回) |

---

### share_float
**分类**: 沪深股票 > 参考数据 > 限售股解禁-获取限售股解禁

**说明**: /数据接口/沪深股票/参考数据/限售股解禁-获取限售股解禁

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（日期格式：YYYYMMDD，下同） |
| `end_date` | string | 否 | 解禁结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, float_date, float_share, float_ratio, holder_name, share_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `float_date` | string | 否 | 解禁日期 |
| `start_date` | string | 否 | 解禁开始日期 |
| `ts_code` | string | 否 | TS股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `float_date` | (默认返回) |
| `float_share` | (默认返回) |
| `float_ratio` | (默认返回) |
| `holder_name` | (默认返回) |
| `share_type` | (默认返回) |

---

### new_share
**分类**: 沪深股票 > 基础数据 > IPO新股上市-获取新股上市列表数据

**说明**: /数据接口/沪深股票/基础数据/IPO新股上市-获取新股上市列表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 上网发行结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, sub_code, name, ipo_date, issue_date, amount, market_amount, price, pe, limit_amount, funds, ballot 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 上网发行开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `sub_code` | (默认返回) |
| `name` | (默认返回) |
| `ipo_date` | (默认返回) |
| `issue_date` | (默认返回) |
| `amount` | (默认返回) |
| `market_amount` | (默认返回) |
| `price` | (默认返回) |
| `pe` | (默认返回) |
| `limit_amount` | (默认返回) |
| `funds` | (默认返回) |
| `ballot` | (默认返回) |

---

### stock_st
**分类**: 沪深股票 > 基础数据 > ST股票列表-获取ST股票列表，可根据交易日期获取历史上每天的ST列表

**说明**: /数据接口/沪深股票/基础数据/ST股票列表-获取ST股票列表，可根据交易日期获取历史上每天的ST列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, type, type_name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始时间 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `type` | (默认返回) |
| `type_name` | (默认返回) |

---

### st
**分类**: 沪深股票 > 基础数据 > ST风险警示板股票列表-ST风险警示板股票列表

**说明**: /数据接口/沪深股票/基础数据/ST风险警示板股票列表-ST风险警示板股票列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, pub_date, imp_date, st_tpye, st_reason, st_explain 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `imp_date` | string | 否 | 实施日期 |
| `pub_date` | string | 否 | 发布日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pub_date` | (默认返回) |
| `imp_date` | (默认返回) |
| `st_tpye` | (默认返回) |
| `st_reason` | (默认返回) |
| `st_explain` | (默认返回) |

---

### stock_company
**分类**: 沪深股票 > 基础数据 > 上市公司基本信息-获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取

**说明**: /数据接口/沪深股票/基础数据/上市公司基本信息-获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 否 | 交易所代码 ，SSE上交所 SZSE深交所 BSE北交所 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, com_name, com_id, exchange, chairman, manager, secretary, reg_capital, setup_date, province, city, website, email, employees 额外可选字段:   office: 办公室   introduction: 公司介绍   main_business: 主要业务及产品   business_scope: 经营范围 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `com_name` | (默认返回) |
| `com_id` | (默认返回) |
| `exchange` | (默认返回) |
| `chairman` | (默认返回) |
| `manager` | (默认返回) |
| `secretary` | (默认返回) |
| `reg_capital` | (默认返回) |
| `setup_date` | (默认返回) |
| `province` | (默认返回) |
| `city` | (默认返回) |
| `website` | (默认返回) |
| `email` | (默认返回) |
| `employees` | (默认返回) |
| `office` | 办公室 |
| `introduction` | 公司介绍 |
| `main_business` | 主要业务及产品 |
| `business_scope` | 经营范围 |

---

### stk_managers
**分类**: 沪深股票 > 基础数据 > 上市公司管理层-获取上市公司管理层

**说明**: /数据接口/沪深股票/基础数据/上市公司管理层-获取上市公司管理层

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（YYYYMMDD格式，下同） |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, name, gender, lev, title, edu, national, birthday, begin_date, end_date 额外可选字段:   resume: 个人简历 |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | 股票代码，支持单个或多个股票输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `name` | (默认返回) |
| `gender` | (默认返回) |
| `lev` | (默认返回) |
| `title` | (默认返回) |
| `edu` | (默认返回) |
| `national` | (默认返回) |
| `birthday` | (默认返回) |
| `begin_date` | (默认返回) |
| `end_date` | (默认返回) |
| `resume` | 个人简历 |

---

### trade_cal
**分类**: 沪深股票 > 基础数据 > 交易日历-获取各大交易所交易日历数据,默认提取的是上交所

**说明**: /数据接口/沪深股票/基础数据/交易日历-获取各大交易所交易日历数据,默认提取的是上交所

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: exchange, cal_date, is_open, pretrade_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_open` | string | 否 | 是否交易 '0'休市 '1'交易 |
| `start_date` | string | 否 | 开始日期 （格式：YYYYMMDD 下同） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `exchange` | (默认返回) |
| `cal_date` | (默认返回) |
| `is_open` | (默认返回) |
| `pretrade_date` | (默认返回) |

---

### bse_mapping
**分类**: 沪深股票 > 基础数据 > 北交所新旧代码对照-获取北交所股票代码变更后新旧代码映射表数据

**说明**: /数据接口/沪深股票/基础数据/北交所新旧代码对照-获取北交所股票代码变更后新旧代码映射表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: name, o_code, n_code, list_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `n_code` | string | 否 | 新代码 |
| `o_code` | string | 否 | 旧代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `name` | (默认返回) |
| `o_code` | (默认返回) |
| `n_code` | (默认返回) |
| `list_date` | (默认返回) |

---

### stk_premarket
**分类**: 沪深股票 > 基础数据 > 每日股本（盘前）-每日开盘前获取当日股票的股本情况，包括总股本和流通股本，涨跌停价格等。

**说明**: /数据接口/沪深股票/基础数据/每日股本（盘前）-每日开盘前获取当日股票的股本情况，包括总股本和流通股本，涨跌停价格等。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, total_share, float_share, pre_close, up_limit, down_limit 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `pre_close` | (默认返回) |
| `up_limit` | (默认返回) |
| `down_limit` | (默认返回) |

---

### stock_hsgt
**分类**: 沪深股票 > 基础数据 > 沪深港通股票列表-获取沪深港通股票列表

**说明**: /数据接口/沪深股票/基础数据/沪深港通股票列表-获取沪深港通股票列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, type, name, type_name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始时间 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD） |
| `ts_code` | string | 否 | 股票代码 |
| `type` | string | 是 | 类型（参考下表） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `type` | (默认返回) |
| `name` | (默认返回) |
| `type_name` | (默认返回) |

---

### hs_const
**分类**: 沪深股票 > 基础数据 > 沪深股通成分股-获取沪股通、深股通成分数据

**说明**: /数据接口/沪深股票/基础数据/沪深股通成分股-获取沪股通、深股通成分数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, hs_type, in_date, out_date, is_new 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `hs_type` | string | 是 | 类型SH沪股通SZ深股通 |
| `is_new` | string | 否 | 是否最新 1 是 0 否 (默认1) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `hs_type` | (默认返回) |
| `in_date` | (默认返回) |
| `out_date` | (默认返回) |
| `is_new` | (默认返回) |

---

### stk_rewards
**分类**: 沪深股票 > 基础数据 > 管理层薪酬和持股-获取上市公司管理层薪酬和持股

**说明**: /数据接口/沪深股票/基础数据/管理层薪酬和持股-获取上市公司管理层薪酬和持股

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, name, title, reward, hold_vol 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | TS股票代码，支持单个或多个代码输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `name` | (默认返回) |
| `title` | (默认返回) |
| `reward` | (默认返回) |
| `hold_vol` | (默认返回) |

---

### stock_basic
**分类**: 沪深股票 > 基础数据 > 股票列表-获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

**说明**: /数据接口/沪深股票/基础数据/股票列表-获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 否 | 交易所 SSE上交所 SZSE深交所 BSE北交所 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, symbol, name, area, industry, cnspell, market, list_date, act_name, act_ent_type 额外可选字段:   is_hs: 是否沪深港通标的，N否 H沪股通 S深股通   enname: 英文全称   exchange: 交易所代码   fullname: 股票全称   curr_type: 交易货币   delist_date: 退市日期   list_st... |
| `is_hs` | string | 否 | 是否沪深港通标的，N否 H沪股通 S深股通 |
| `list_status` | string | 否 | 上市状态 L上市 D退市 P暂停上市 G过会未交易，默认是L |
| `market` | string | 否 | 市场类别 （主板/创业板/科创板/CDR/北交所） |
| `name` | string | 否 | 名称 |
| `ts_code` | string | 否 | TS股票代码(格式说明) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `symbol` | (默认返回) |
| `name` | (默认返回) |
| `area` | (默认返回) |
| `industry` | (默认返回) |
| `cnspell` | (默认返回) |
| `market` | (默认返回) |
| `list_date` | (默认返回) |
| `act_name` | (默认返回) |
| `act_ent_type` | (默认返回) |
| `is_hs` | 是否沪深港通标的，N否 H沪股通 S深股通 |
| `enname` | 英文全称 |
| `exchange` | 交易所代码 |
| `fullname` | 股票全称 |
| `curr_type` | 交易货币 |
| `delist_date` | 退市日期 |
| `list_status` | 上市状态 L上市 D退市 G过会未交易 P暂停上市 |

---

### bak_basic
**分类**: 沪深股票 > 基础数据 > 股票历史列表-获取备用基础列表，数据从2016年开始

**说明**: /数据接口/沪深股票/基础数据/股票历史列表-获取备用基础列表，数据从2016年开始

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, industry, area, pe, float_share, total_share, total_assets, liquid_assets, fixed_assets, reserved, reserved_pershare, eps, bvps, pb, list_date, undp, per_undp, rev_yoy, profit_yoy, gpr, npr, holder_n... |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `industry` | (默认返回) |
| `area` | (默认返回) |
| `pe` | (默认返回) |
| `float_share` | (默认返回) |
| `total_share` | (默认返回) |
| `total_assets` | (默认返回) |
| `liquid_assets` | (默认返回) |
| `fixed_assets` | (默认返回) |
| `reserved` | (默认返回) |
| `reserved_pershare` | (默认返回) |
| `eps` | (默认返回) |
| `bvps` | (默认返回) |
| `pb` | (默认返回) |
| `list_date` | (默认返回) |
| `undp` | (默认返回) |
| `per_undp` | (默认返回) |
| `rev_yoy` | (默认返回) |
| `profit_yoy` | (默认返回) |
| `gpr` | (默认返回) |
| `npr` | (默认返回) |
| `holder_num` | (默认返回) |

---

### namechange
**分类**: 沪深股票 > 基础数据 > 股票曾用名-历史名称变更记录

**说明**: /数据接口/沪深股票/基础数据/股票曾用名-历史名称变更记录

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, start_date, end_date, ann_date, change_reason 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `start_date` | (默认返回) |
| `end_date` | (默认返回) |
| `ann_date` | (默认返回) |
| `change_reason` | (默认返回) |

---

### top10_holders
**分类**: 沪深股票 > 市场参考数据 > 前十大股东-获取上市公司前十大股东数据，包括持有数量和比例等信息

**说明**: /数据接口/沪深股票/市场参考数据/前十大股东-获取上市公司前十大股东数据，包括持有数量和比例等信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, holder_name, hold_amount, hold_ratio, hold_float_ratio, hold_change, holder_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期（YYYYMMDD格式，一般为每个季度最后一天） |
| `start_date` | string | 否 | 报告期开始日期 |
| `ts_code` | string | 是 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `holder_name` | (默认返回) |
| `hold_amount` | (默认返回) |
| `hold_ratio` | (默认返回) |
| `hold_float_ratio` | (默认返回) |
| `hold_change` | (默认返回) |
| `holder_type` | (默认返回) |

---

### block_trade
**分类**: 沪深股票 > 市场参考数据 > 大宗交易-大宗交易

**说明**: /数据接口/沪深股票/市场参考数据/大宗交易-大宗交易

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, price, vol, amount, buyer, seller 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | TS代码（股票代码和日期至少输入一个参数） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `price` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `buyer` | (默认返回) |
| `seller` | (默认返回) |

---

### stk_holdertrade
**分类**: 沪深股票 > 市场参考数据 > 股东增减持-获取上市公司增减持数据，了解重要股东近期及历史上的股份增减变化

**说明**: /数据接口/沪深股票/市场参考数据/股东增减持-获取上市公司增减持数据，了解重要股东近期及历史上的股份增减变化

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, holder_name, holder_type, in_de, change_vol, change_ratio, after_share, after_ratio, avg_price, total_share 额外可选字段:   begin_date: 增减持开始日期   close_date: 增减持结束日期 |
| `holder_type` | string | 否 | 股东类型C公司P个人G高管 |
| `start_date` | string | 否 | 公告开始日期 |
| `trade_type` | string | 否 | 交易类型IN增持DE减持 |
| `ts_code` | string | 否 | TS股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `holder_name` | (默认返回) |
| `holder_type` | (默认返回) |
| `in_de` | (默认返回) |
| `change_vol` | (默认返回) |
| `change_ratio` | (默认返回) |
| `after_share` | (默认返回) |
| `after_ratio` | (默认返回) |
| `avg_price` | (默认返回) |
| `total_share` | (默认返回) |
| `begin_date` | 增减持开始日期 |
| `close_date` | 增减持结束日期 |

---

### pledge_detail
**分类**: 沪深股票 > 市场参考数据 > 股权质押明细数据-获取股票质押明细数据

**说明**: /数据接口/沪深股票/市场参考数据/股权质押明细数据-获取股票质押明细数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, holder_name, pledge_amount, start_date, end_date, is_release, release_date, pledgor, holding_amount, pledged_amount, p_total_ratio, h_total_ratio, is_buyback 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `holder_name` | (默认返回) |
| `pledge_amount` | (默认返回) |
| `start_date` | (默认返回) |
| `end_date` | (默认返回) |
| `is_release` | (默认返回) |
| `release_date` | (默认返回) |
| `pledgor` | (默认返回) |
| `holding_amount` | (默认返回) |
| `pledged_amount` | (默认返回) |
| `p_total_ratio` | (默认返回) |
| `h_total_ratio` | (默认返回) |
| `is_buyback` | (默认返回) |

---

### pledge_stat
**分类**: 沪深股票 > 市场参考数据 > 股权质押统计数据-获取股票质押统计数据

**说明**: /数据接口/沪深股票/市场参考数据/股权质押统计数据-获取股票质押统计数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 截止日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, pledge_count, unrest_pledge, rest_pledge, total_share, pledge_ratio 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `pledge_count` | (默认返回) |
| `unrest_pledge` | (默认返回) |
| `rest_pledge` | (默认返回) |
| `total_share` | (默认返回) |
| `pledge_ratio` | (默认返回) |

---

### repurchase
**分类**: 沪深股票 > 市场参考数据 > 股票回购-获取上市公司回购股票数据

**说明**: /数据接口/沪深股票/市场参考数据/股票回购-获取上市公司回购股票数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（任意填参数，如果都不填，单次默认返回2000条） |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, proc, exp_date, vol, amount, high_limit, low_limit 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 公告开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `proc` | (默认返回) |
| `exp_date` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `high_limit` | (默认返回) |
| `low_limit` | (默认返回) |

---

### stk_account
**分类**: 沪深股票 > 市场参考数据 > 股票开户数据（停）-获取股票账户开户数据，统计周期为一周

**说明**: /数据接口/沪深股票/市场参考数据/股票开户数据（停）-获取股票账户开户数据，统计周期为一周

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, weekly_new, total, weekly_hold, weekly_trade 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `weekly_new` | (默认返回) |
| `total` | (默认返回) |
| `weekly_hold` | (默认返回) |
| `weekly_trade` | (默认返回) |

---

### stk_account_old
**分类**: 沪深股票 > 市场参考数据 > 股票开户数据（旧）-获取股票账户开户数据旧版格式数据，数据从2008年1月开始，到2015年5月29，新数据请通过[股票开户数据](https: > tushare.pro > document > 2?doc_id=164)获取。

**说明**: /数据接口/沪深股票/市场参考数据/股票开户数据（旧）-获取股票账户开户数据旧版格式数据，数据从2008年1月开始，到2015年5月29，新数据请通过[股票开户数据](https://tushare.pro/document/2?doc_id=164)获取。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, new_sh, new_sz, active_sh, active_sz, total_sh, total_sz, trade_sh, trade_sz 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `new_sh` | (默认返回) |
| `new_sz` | (默认返回) |
| `active_sh` | (默认返回) |
| `active_sz` | (默认返回) |
| `total_sh` | (默认返回) |
| `total_sz` | (默认返回) |
| `trade_sh` | (默认返回) |
| `trade_sz` | (默认返回) |

---

### dc_hot
**分类**: 沪深股票 > 打板专题数据 > 东方财富App热榜-获取东方财富App热榜数据，包括A股市场、ETF基金、港股市场、美股市场等等，每日盘中提取4次，收盘后4次，最晚22点提取一次。

**说明**: /数据接口/沪深股票/打板专题数据/东方财富App热榜-获取东方财富App热榜数据，包括A股市场、ETF基金、港股市场、美股市场等等，每日盘中提取4次，收盘后4次，最晚22点提取一次。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, data_type, ts_code, ts_name, rank, pct_change, current_price, rank_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `hot_type` | string | 否 | 热点类型(人气榜、飙升榜) |
| `is_new` | string | 否 | 是否最新（默认Y，如果为N则为盘中和盘后阶段采集，具体时间可参考rank_time字段，状态N每小时更新一次，状态Y更新时间为22：30） |
| `market` | string | 否 | 类型(A股市场、ETF基金、港股市场、美股市场) |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `data_type` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_name` | (默认返回) |
| `rank` | (默认返回) |
| `pct_change` | (默认返回) |
| `current_price` | (默认返回) |
| `rank_time` | (默认返回) |

---

### dc_member
**分类**: 沪深股票 > 打板专题数据 > 东方财富概念成分-获取东方财富板块每日成分数据，可以根据概念板块代码和交易日期，获取历史成分

**说明**: /数据接口/沪深股票/打板专题数据/东方财富概念成分-获取东方财富板块每日成分数据，可以根据概念板块代码和交易日期，获取历史成分

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `con_code` | string | 否 | 成分股票代码 |
| `end_date` | string | 否 | 结束日期（YYYYMMDD格式） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, con_code, name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期（YYYYMMDD格式） |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式） |
| `ts_code` | string | 否 | 板块指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `con_code` | (默认返回) |
| `name` | (默认返回) |

---

### dc_index
**分类**: 沪深股票 > 打板专题数据 > 东方财富概念板块-获取东方财富每个交易日的概念板块数据，支持按日期查询

**说明**: /数据接口/沪深股票/打板专题数据/东方财富概念板块-获取东方财富每个交易日的概念板块数据，支持按日期查询

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, leading, leading_code, pct_change, leading_pct, total_mv, turnover_rate, up_num, down_num, idx_type, level 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `idx_type` | string | 是 | 板块类型(行业板块、概念板块、地域板块) |
| `name` | string | 否 | 板块名称（例如：人形机器人） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 指数代码（支持多个代码同时输入，用逗号分隔） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `leading` | (默认返回) |
| `leading_code` | (默认返回) |
| `pct_change` | (默认返回) |
| `leading_pct` | (默认返回) |
| `total_mv` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `up_num` | (默认返回) |
| `down_num` | (默认返回) |
| `idx_type` | (默认返回) |
| `level` | (默认返回) |

---

### dc_daily
**分类**: 沪深股票 > 打板专题数据 > 东财概念和行业指数行情-获取东财概念板块、行业指数板块、地域板块行情数据，历史数据开始于2020年

**说明**: /数据接口/沪深股票/打板专题数据/东财概念和行业指数行情-获取东财概念板块、行业指数板块、地域板块行情数据，历史数据开始于2020年

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, change, pct_change, vol, amount, swing, turnover_rate 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `idx_type` | string | 否 | 板块类型： 概念板块、行业板块、地域板块 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(格式：YYYYMMDD下同） |
| `ts_code` | string | 否 | 板块代码（格式：xxxxx.DC) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `swing` | (默认返回) |
| `turnover_rate` | (默认返回) |

---

### dc_concept
**分类**: 沪深股票 > 打板专题数据 > 东财题材库-获取东财概念题材列表，每天盘后更新

**说明**: /数据接口/沪深股票/打板专题数据/东财题材库-获取东财概念题材列表，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: theme_code, trade_date, name, pct_change, hot, sort, strength, z_t_num, main_change, lead_stock, lead_stock_code, lead_stock_pct_change 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 题材名称 |
| `theme_code` | string | 否 | 题材代码(xxxxxx.DC格式) |
| `trade_date` | string | 否 | 交易日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `theme_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `pct_change` | (默认返回) |
| `hot` | (默认返回) |
| `sort` | (默认返回) |
| `strength` | (默认返回) |
| `z_t_num` | (默认返回) |
| `main_change` | (默认返回) |
| `lead_stock` | (默认返回) |
| `lead_stock_code` | (默认返回) |
| `lead_stock_pct_change` | (默认返回) |

---

### dc_concept_cons
**分类**: 沪深股票 > 打板专题数据 > 东财题材成分-获取东方财富概念题材的成分股，每天盘后更新

**说明**: /数据接口/沪深股票/打板专题数据/东财题材成分-获取东方财富概念题材的成分股，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, theme_code, industry_code, industry, reason, hot_num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `theme_code` | string | 否 | 题材代码 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `theme_code` | (默认返回) |
| `industry_code` | (默认返回) |
| `industry` | (默认返回) |
| `reason` | (默认返回) |
| `hot_num` | (默认返回) |

---

### ths_hot
**分类**: 沪深股票 > 打板专题数据 > 同花顺App热榜数-获取同花顺App热榜数据，包括热股、概念板块、ETF、可转债、港美股等等，每日盘中提取4次，收盘后4次，最晚22点提取一次。

**说明**: /数据接口/沪深股票/打板专题数据/同花顺App热榜数-获取同花顺App热榜数据，包括热股、概念板块、ETF、可转债、港美股等等，每日盘中提取4次，收盘后4次，最晚22点提取一次。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, data_type, ts_code, ts_name, rank, pct_change, current_price, concept, rank_reason, hot, rank_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_new` | string | 否 | 是否最新（默认Y，如果为N则为盘中和盘后阶段采集，具体时间可参考rank_time字段，状态N每小时更新一次，状态Y更新时间为22：30） |
| `market` | string | 否 | 热榜类型(热股、ETF、可转债、行业板块、概念板块、期货、港股、热基、美股) |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `data_type` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_name` | (默认返回) |
| `rank` | (默认返回) |
| `pct_change` | (默认返回) |
| `current_price` | (默认返回) |
| `concept` | (默认返回) |
| `rank_reason` | (默认返回) |
| `hot` | (默认返回) |
| `rank_time` | (默认返回) |

---

### ths_daily
**分类**: 沪深股票 > 打板专题数据 > 同花顺概念和行业指数行情-获取同花顺板块指数行情

**说明**: /数据接口/沪深股票/打板专题数据/同花顺概念和行业指数行情-获取同花顺板块指数行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, avg_price, change, pct_change, vol, turnover_rate 额外可选字段:   float_mv: 流通市值（元）   total_mv: 总市值（元） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `avg_price` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `float_mv` | 流通市值（元） |
| `total_mv` | 总市值（元） |

---

### limit_list_ths
**分类**: 沪深股票 > 打板专题数据 > 同花顺涨跌停榜单-获取同花顺每日涨跌停榜单数据，历史数据从20231101开始提供，增量每天16点左右更新

**说明**: /数据接口/沪深股票/打板专题数据/同花顺涨跌停榜单-获取同花顺每日涨跌停榜单数据，历史数据从20231101开始提供，增量每天16点左右更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, price, pct_chg, open_num, lu_desc, limit_type, tag, status, limit_order, limit_amount, turnover_rate, free_float, lu_limit_order, limit_up_suc_rate, turnover, market_type 额外可选字段:   rise_rate: 涨速   su... |
| `limit_type` | string | 否 | 涨停池、连扳池、冲刺涨停、炸板池、跌停池，默认：涨停池 |
| `market` | string | 否 | HS-沪深主板 GEM-创业板 STAR-科创板 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `price` | (默认返回) |
| `pct_chg` | (默认返回) |
| `open_num` | (默认返回) |
| `lu_desc` | (默认返回) |
| `limit_type` | (默认返回) |
| `tag` | (默认返回) |
| `status` | (默认返回) |
| `limit_order` | (默认返回) |
| `limit_amount` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `free_float` | (默认返回) |
| `lu_limit_order` | (默认返回) |
| `limit_up_suc_rate` | (默认返回) |
| `turnover` | (默认返回) |
| `market_type` | (默认返回) |
| `rise_rate` | 涨速 |
| `sum_float` | 总市值（亿元） |
| `last_ld_time` | 最后跌停时间 |
| `last_lu_time` | 最后涨停时间 |
| `first_ld_time` | 首次跌停时间 |
| `first_lu_time` | 首次涨停时间 |

---

### ths_member
**分类**: 沪深股票 > 打板专题数据 > 同花顺行业概念成分-获取同花顺概念板块成分列表

**说明**: /数据接口/沪深股票/打板专题数据/同花顺行业概念成分-获取同花顺概念板块成分列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `con_code` | string | 否 | 股票代码 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, con_code, con_name 额外可选字段:   is_new: 是否最新Y是N否   weight: 权重(暂无)   in_date: 纳入日期(暂无)   out_date: 剔除日期(暂无) |
| `ts_code` | string | 否 | 板块指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `con_code` | (默认返回) |
| `con_name` | (默认返回) |
| `is_new` | 是否最新Y是N否 |
| `weight` | 权重(暂无) |
| `in_date` | 纳入日期(暂无) |
| `out_date` | 剔除日期(暂无) |

---

### ths_index
**分类**: 沪深股票 > 打板专题数据 > 同花顺行业概念板块-获取同花顺板块指数，包括概念、行业、特色指数。

**说明**: /数据接口/沪深股票/打板专题数据/同花顺行业概念板块-获取同花顺板块指数，包括概念、行业、特色指数。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 否 | 市场类型A-a股 HK-港股 US-美股 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, count, exchange, list_date, type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | 指数代码 |
| `type` | string | 否 | 指数类型 N-概念指数 I-行业指数 R-地域指数 S-同花顺特色指数 ST-同花顺风格指数 TH-同花顺主题指数 BB-同花顺宽基指数 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `count` | (默认返回) |
| `exchange` | (默认返回) |
| `list_date` | (默认返回) |
| `type` | (默认返回) |

---

### hm_list
**分类**: 沪深股票 > 打板专题数据 > 市场游资最全名录-获取游资分类名录信息

**说明**: /数据接口/沪深股票/打板专题数据/市场游资最全名录-获取游资分类名录信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: name, desc, orgs 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 游资名称 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `name` | (默认返回) |
| `desc` | (默认返回) |
| `orgs` | (默认返回) |

---

### stk_auction
**分类**: 沪深股票 > 打板专题数据 > 开盘竞价成交（当日）-获取当日个股和ETF的集合竞价成交情况，每天9点25~29分之间可以获取当日的集合竞价成交数据

**说明**: /数据接口/沪深股票/打板专题数据/开盘竞价成交（当日）-获取当日个股和ETF的集合竞价成交情况，每天9点25~29分之间可以获取当日的集合竞价成交数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, vol, price, amount, pre_close, turnover_rate, volume_ratio, float_share 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `vol` | (默认返回) |
| `price` | (默认返回) |
| `amount` | (默认返回) |
| `pre_close` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `volume_ratio` | (默认返回) |
| `float_share` | (默认返回) |

---

### kpl_list
**分类**: 沪深股票 > 打板专题数据 > 榜单数据（开盘啦）-获取开盘啦涨停、跌停、炸板等榜单数据

**说明**: /数据接口/沪深股票/打板专题数据/榜单数据（开盘啦）-获取开盘啦涨停、跌停、炸板等榜单数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, lu_time, ld_time, open_time, last_time, lu_desc, tag, theme, net_change, bid_amount, status, bid_change, bid_turnover, lu_bid_vol, pct_chg, bid_pct_chg, rt_pct_chg, limit_order, amount, turnover_rate... |
| `start_date` | string | 否 | 开始日期 |
| `tag` | string | 否 | 板单类型（涨停/炸板/跌停/自然涨停/竞价，默认为涨停) |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `lu_time` | (默认返回) |
| `ld_time` | (默认返回) |
| `open_time` | (默认返回) |
| `last_time` | (默认返回) |
| `lu_desc` | (默认返回) |
| `tag` | (默认返回) |
| `theme` | (默认返回) |
| `net_change` | (默认返回) |
| `bid_amount` | (默认返回) |
| `status` | (默认返回) |
| `bid_change` | (默认返回) |
| `bid_turnover` | (默认返回) |
| `lu_bid_vol` | (默认返回) |
| `pct_chg` | (默认返回) |
| `bid_pct_chg` | (默认返回) |
| `rt_pct_chg` | (默认返回) |
| `limit_order` | (默认返回) |
| `amount` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `free_float` | (默认返回) |
| `lu_limit_order` | (默认返回) |

---

### limit_cpt_list
**分类**: 沪深股票 > 打板专题数据 > 涨停最强板块统计-获取每天涨停股票最多最强的概念板块，可以分析强势板块的轮动，判断资金动向

**说明**: /数据接口/沪深股票/打板专题数据/涨停最强板块统计-获取每天涨停股票最多最强的概念板块，可以分析强势板块的轮动，判断资金动向

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, days, up_stat, cons_nums, up_nums, pct_chg, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | 板块代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `days` | (默认返回) |
| `up_stat` | (默认返回) |
| `cons_nums` | (默认返回) |
| `up_nums` | (默认返回) |
| `pct_chg` | (默认返回) |
| `rank` | (默认返回) |

---

### limit_step
**分类**: 沪深股票 > 打板专题数据 > 涨停股票连板天梯-获取每天连板个数晋级的股票，可以分析出每天连续涨停进阶个数，判断强势热度

**说明**: /数据接口/沪深股票/打板专题数据/涨停股票连板天梯-获取每天连板个数晋级的股票，可以分析出每天连续涨停进阶个数，判断强势热度

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, nums 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `nums` | string | 否 | 连板次数，支持多个输入，例如nums='2,3' |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `nums` | (默认返回) |

---

### limit_list_d
**分类**: 沪深股票 > 打板专题数据 > 涨跌停和炸板数据-获取A股每日涨跌停、炸板数据情况，数据从2020年开始（不提供ST股票的统计）

**说明**: /数据接口/沪深股票/打板专题数据/涨跌停和炸板数据-获取A股每日涨跌停、炸板数据情况，数据从2020年开始（不提供ST股票的统计）

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所（SH上交所SZ深交所BJ北交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, industry, name, close, pct_chg, amount, limit_amount, float_mv, total_mv, turnover_ratio, fd_amount, first_time, last_time, open_times, up_stat, limit_times, limit 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `limit_type` | string | 否 | 涨跌停类型（U涨停D跌停Z炸板） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `industry` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `pct_chg` | (默认返回) |
| `amount` | (默认返回) |
| `limit_amount` | (默认返回) |
| `float_mv` | (默认返回) |
| `total_mv` | (默认返回) |
| `turnover_ratio` | (默认返回) |
| `fd_amount` | (默认返回) |
| `first_time` | (默认返回) |
| `last_time` | (默认返回) |
| `open_times` | (默认返回) |
| `up_stat` | (默认返回) |
| `limit_times` | (默认返回) |
| `limit` | (默认返回) |

---

### hm_detail
**分类**: 沪深股票 > 打板专题数据 > 游资交易每日明细-获取每日游资交易明细，数据开始于2022年8。游资分类名录，请点击游资名录

**说明**: /数据接口/沪深股票/打板专题数据/游资交易每日明细-获取每日游资交易明细，数据开始于2022年8。游资分类名录，请点击游资名录

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期(YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, ts_name, buy_amount, sell_amount, net_amount, hm_name, hm_orgs 额外可选字段:   tag: 标签 |
| `hm_name` | string | 否 | 游资名称 |
| `start_date` | string | 否 | 开始日期(YYYYMMDD) |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_name` | (默认返回) |
| `buy_amount` | (默认返回) |
| `sell_amount` | (默认返回) |
| `net_amount` | (默认返回) |
| `hm_name` | (默认返回) |
| `hm_orgs` | (默认返回) |
| `tag` | 标签 |

---

### cls_stock_shock
**分类**: 沪深股票 > 打板专题数据 > 财联社-个股异动-获取财联社市场风向标-涨停-连板-炸板-跌停池数据

**说明**: /数据接口/沪深股票/打板专题数据/财联社-个股异动-获取财联社市场风向标-涨停-连板-炸板-跌停池数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, type, type_name, change, lu_num, reason, plate, is_st, time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `type` | (默认返回) |
| `type_name` | (默认返回) |
| `change` | (默认返回) |
| `lu_num` | (默认返回) |
| `reason` | (默认返回) |
| `plate` | (默认返回) |
| `is_st` | (默认返回) |
| `time` | (默认返回) |

---

### cls_index
**分类**: 沪深股票 > 打板专题数据 > 财联社-板块-获取财联社每个交易日的概念板块数据，支持按日期查询

**说明**: /数据接口/沪深股票/打板专题数据/财联社-板块-获取财联社每个交易日的概念板块数据，支持按日期查询

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, category, trade_date, name, ud_ratio, net_amount, limit_up_num, limit_down_num, plate_change, leading_code, leading, change 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 板块名称（例如：人形机器人） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 指数代码（支持多个代码同时输入，用逗号分隔） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `category` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `ud_ratio` | (默认返回) |
| `net_amount` | (默认返回) |
| `limit_up_num` | (默认返回) |
| `limit_down_num` | (默认返回) |
| `plate_change` | (默认返回) |
| `leading_code` | (默认返回) |
| `leading` | (默认返回) |
| `change` | (默认返回) |

---

### cls_market_shock
**分类**: 沪深股票 > 打板专题数据 > 财联社-板块异动-财联社-板块异动

**说明**: /数据接口/沪深股票/打板专题数据/财联社-板块异动-财联社-板块异动

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, c_time, trade_date, name, status 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 板块代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `c_time` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `status` | (默认返回) |

---

### cls_member
**分类**: 沪深股票 > 打板专题数据 > 财联社-板块成分-获取财联社板块每日成分数据，可以根据概念板块代码和交易日期，获取历史成分

**说明**: /数据接口/沪深股票/打板专题数据/财联社-板块成分-获取财联社板块每日成分数据，可以根据概念板块代码和交易日期，获取历史成分

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, plate_code, trade_date, name, is_core, change, net_amount, weight, head_num, float_mv, price, desc 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `plate_code` | string | 否 | 板块指数代码 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式） |
| `ts_code` | string | 否 | 成分股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `plate_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `is_core` | (默认返回) |
| `change` | (默认返回) |
| `net_amount` | (默认返回) |
| `weight` | (默认返回) |
| `head_num` | (默认返回) |
| `float_mv` | (默认返回) |
| `price` | (默认返回) |
| `desc` | (默认返回) |

---

### tdx_index
**分类**: 沪深股票 > 打板专题数据 > 通达信板块信息-获取通达信板块基础信息，包括概念板块、行业、风格、地域等

**说明**: /数据接口/沪深股票/打板专题数据/通达信板块信息-获取通达信板块基础信息，包括概念板块、行业、风格、地域等

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, idx_type, idx_count, total_share, float_share, total_mv, float_mv 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `idx_type` | string | 否 | 板块类型：概念板块、行业板块、风格板块、地区板块 |
| `trade_date` | string | 否 | 交易日期(格式：YYYYMMDD） |
| `ts_code` | string | 否 | 板块代码：xxxxxx.TDX |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `idx_type` | (默认返回) |
| `idx_count` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `total_mv` | (默认返回) |
| `float_mv` | (默认返回) |

---

### tdx_member
**分类**: 沪深股票 > 打板专题数据 > 通达信板块成分-获取通达信各板块成分股信息

**说明**: /数据接口/沪深股票/打板专题数据/通达信板块成分-获取通达信各板块成分股信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `con_code` | string | 否 | 成分股票代码 |
| `end_date` | string | 否 | 结束日期：（YYYYMMDD格式） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, con_code, con_name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期：（YYYYMMDD格式） |
| `trade_date` | string | 否 | 交易日期：（YYYYMMDD格式） |
| `ts_code` | string | 否 | 板块代码：xxxxxx.TDX |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `con_code` | (默认返回) |
| `con_name` | (默认返回) |

---

### tdx_daily
**分类**: 沪深股票 > 打板专题数据 > 通达信板块行情-获取通达信各板块行情，包括成交和估值等数据

**说明**: /数据接口/沪深股票/打板专题数据/通达信板块行情-获取通达信各板块行情，包括成交和估值等数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_change, vol, amount, rise, vol_ratio, turnover_rate, swing, up_num, down_num, limit_up_num, limit_down_num, lu_days, 3day, 5day, 10day, 20day, 60day, mtd, ytd... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期，格式YYYYMMDD,下同 |
| `ts_code` | string | 否 | 板块代码：xxxxxx.TDX |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `rise` | (默认返回) |
| `vol_ratio` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `swing` | (默认返回) |
| `up_num` | (默认返回) |
| `down_num` | (默认返回) |
| `limit_up_num` | (默认返回) |
| `limit_down_num` | (默认返回) |
| `lu_days` | (默认返回) |
| `mtd` | (默认返回) |
| `ytd` | (默认返回) |
| `pe` | (默认返回) |
| `pb` | (默认返回) |
| `float_mv` | (默认返回) |
| `ab_total_mv` | (默认返回) |
| `float_share` | (默认返回) |
| `total_share` | (默认返回) |
| `bm_buy_net` | (默认返回) |
| `bm_buy_ratio` | (默认返回) |
| `bm_net` | (默认返回) |
| `bm_ratio` | (默认返回) |

---

### jygs_stock_shock
**分类**: 沪深股票 > 打板专题数据 > 韭研公社板块个股异动-获取韭研公社个股异动数据

**说明**: /数据接口/沪深股票/打板专题数据/韭研公社板块个股异动-获取韭研公社个股异动数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, latest, lu_time, num, reason, pct_change, concept_name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `latest` | (默认返回) |
| `lu_time` | (默认返回) |
| `num` | (默认返回) |
| `reason` | (默认返回) |
| `pct_change` | (默认返回) |
| `concept_name` | (默认返回) |

---

### kpl_concept_cons
**分类**: 沪深股票 > 打板专题数据 > 题材成分（开盘啦）-获取开盘啦概念题材的成分股

**说明**: /数据接口/沪深股票/打板专题数据/题材成分（开盘啦）-获取开盘啦概念题材的成分股

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `con_code` | string | 否 | 成分代码（xxxxxx.SH格式） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, con_name, con_code, trade_date, desc, hot_num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式） |
| `ts_code` | string | 否 | 题材代码（xxxxxx.KP格式） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `con_name` | (默认返回) |
| `con_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `desc` | (默认返回) |
| `hot_num` | (默认返回) |

---

### kpl_concept
**分类**: 沪深股票 > 打板专题数据 > 题材数据（开盘啦）-获取开盘啦概念题材列表，每天盘后更新

**说明**: /数据接口/沪深股票/打板专题数据/题材数据（开盘啦）-获取开盘啦概念题材列表，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, z_t_num, up_num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 题材名称 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式） |
| `ts_code` | string | 否 | 题材代码（xxxxxx.KP格式） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `z_t_num` | (默认返回) |
| `up_num` | (默认返回) |

---

### top_inst
**分类**: 沪深股票 > 打板专题数据 > 龙虎榜机构交易单-龙虎榜机构成交明细

**说明**: /数据接口/沪深股票/打板专题数据/龙虎榜机构交易单-龙虎榜机构成交明细

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, exalter, side, buy, buy_rate, sell, sell_rate, net_buy, reason 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `trade_date` | string | 是 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `exalter` | (默认返回) |
| `side` | (默认返回) |
| `buy` | (默认返回) |
| `buy_rate` | (默认返回) |
| `sell` | (默认返回) |
| `sell_rate` | (默认返回) |
| `net_buy` | (默认返回) |
| `reason` | (默认返回) |

---

### top_list
**分类**: 沪深股票 > 打板专题数据 > 龙虎榜每日统计单-龙虎榜每日交易明细

**说明**: /数据接口/沪深股票/打板专题数据/龙虎榜每日统计单-龙虎榜每日交易明细

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, close, pct_change, turnover_rate, amount, l_sell, l_buy, l_amount, net_amount, net_rate, amount_rate, float_values, reason 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `trade_date` | string | 是 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `pct_change` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `amount` | (默认返回) |
| `l_sell` | (默认返回) |
| `l_buy` | (默认返回) |
| `l_amount` | (默认返回) |
| `net_amount` | (默认返回) |
| `net_rate` | (默认返回) |
| `amount_rate` | (默认返回) |
| `float_values` | (默认返回) |
| `reason` | (默认返回) |

---

### stk_ah_comparison
**分类**: 沪深股票 > 特色数据 > AH股比价-AH股比价数据，可根据交易日期获取历史

**说明**: /数据接口/沪深股票/特色数据/AH股比价-AH股比价数据，可根据交易日期获取历史

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: hk_code, ts_code, trade_date, hk_name, hk_pct_chg, hk_close, name, close, pct_chg, ah_comparison, ah_premium 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `hk_code` | string | 否 | 港股股票代码（xxxxx.HK) |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD下同） |
| `ts_code` | string | 否 | A股票代码(xxxxxx.SH/SZ/BJ) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `hk_code` | (默认返回) |
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `hk_name` | (默认返回) |
| `hk_pct_chg` | (默认返回) |
| `hk_close` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `pct_chg` | (默认返回) |
| `ah_comparison` | (默认返回) |
| `ah_premium` | (默认返回) |

---

### ccass_hold_detail
**分类**: 沪深股票 > 特色数据 > 中央结算系统持股明细-获取中央结算系统机构席位持股明细，数据覆盖**全历史**，根据交易所披露时间，当日数据在下一交易日早上9点前完成

**说明**: /数据接口/沪深股票/特色数据/中央结算系统持股明细-获取中央结算系统机构席位持股明细，数据覆盖**全历史**，根据交易所披露时间，当日数据在下一交易日早上9点前完成

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, col_participant_id, col_participant_name, col_shareholding, col_shareholding_percent 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `hk_code` | string | 否 | 港交所代码 （e.g. 95009） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 股票代码 (e.g. 605009.SH) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `col_participant_id` | (默认返回) |
| `col_participant_name` | (默认返回) |
| `col_shareholding` | (默认返回) |
| `col_shareholding_percent` | (默认返回) |

---

### ccass_hold
**分类**: 沪深股票 > 特色数据 > 中央结算系统持股统计-获取中央结算系统持股汇总数据，覆盖全部历史数据，根据交易所披露时间，当日数据在下一交易日早上9点前完成入库

**说明**: /数据接口/沪深股票/特色数据/中央结算系统持股统计-获取中央结算系统持股汇总数据，覆盖全部历史数据，根据交易所披露时间，当日数据在下一交易日早上9点前完成入库

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, shareholding, hold_nums, hold_ratio 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `hk_code` | string | 否 | 港交所代码 （e.g. 95009） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 股票代码 (e.g. 605009.SH) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `shareholding` | (默认返回) |
| `hold_nums` | (默认返回) |
| `hold_ratio` | (默认返回) |

---

### broker_recommend
**分类**: 沪深股票 > 特色数据 > 券商月度金股-获取券商月度金股，一般1日~3日内更新当月数据

**说明**: /数据接口/沪深股票/特色数据/券商月度金股-获取券商月度金股，一般1日~3日内更新当月数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, broker, ts_code, name 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `month` | string | 是 | 月度（YYYYMM） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `broker` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |

---

### report_rc
**分类**: 沪深股票 > 特色数据 > 券商盈利预测数据-获取券商（卖方）每天研报的盈利预测数据，数据从2010年开始，每晚19~22点更新当日数据

**说明**: /数据接口/沪深股票/特色数据/券商盈利预测数据-获取券商（卖方）每天研报的盈利预测数据，数据从2010年开始，每晚19~22点更新当日数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, report_date, report_title, report_type, classify, org_name, author_name, quarter, op_rt, op_pr, tp, np, eps, pe, rd, roe, ev_ebitda, rating, max_price, min_price 额外可选字段:   imp_dg: 机构关注度   create_time: TS数据更新时间 |
| `report_date` | string | 否 | 报告日期 |
| `start_date` | string | 否 | 报告开始日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `report_date` | (默认返回) |
| `report_title` | (默认返回) |
| `report_type` | (默认返回) |
| `classify` | (默认返回) |
| `org_name` | (默认返回) |
| `author_name` | (默认返回) |
| `quarter` | (默认返回) |
| `op_rt` | (默认返回) |
| `op_pr` | (默认返回) |
| `tp` | (默认返回) |
| `np` | (默认返回) |
| `eps` | (默认返回) |
| `pe` | (默认返回) |
| `rd` | (默认返回) |
| `roe` | (默认返回) |
| `ev_ebitda` | (默认返回) |
| `rating` | (默认返回) |
| `max_price` | (默认返回) |
| `min_price` | (默认返回) |
| `imp_dg` | 机构关注度 |
| `create_time` | TS数据更新时间 |

---

### stk_surv
**分类**: 沪深股票 > 特色数据 > 机构调研数据-获取上市公司机构调研记录数据

**说明**: /数据接口/沪深股票/特色数据/机构调研数据-获取上市公司机构调研记录数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 调研结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, surv_date, fund_visitors, rece_place, rece_mode, rece_org, org_type, comp_rece 额外可选字段:   content: 调研内容 |
| `start_date` | string | 否 | 调研开始日期 |
| `trade_date` | string | 否 | 调研日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `surv_date` | (默认返回) |
| `fund_visitors` | (默认返回) |
| `rece_place` | (默认返回) |
| `rece_mode` | (默认返回) |
| `rece_org` | (默认返回) |
| `org_type` | (默认返回) |
| `comp_rece` | (默认返回) |
| `content` | 调研内容 |

---

### cyq_chips
**分类**: 沪深股票 > 特色数据 > 每日筹码分布-获取A股每日的筹码分布情况，提供各价位占比，数据从2018年开始，每天18~19点之间更新当日数据

**说明**: /数据接口/沪深股票/特色数据/每日筹码分布-获取A股每日的筹码分布情况，提供各价位占比，数据从2018年开始，每天18~19点之间更新当日数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, price, percent 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `price` | (默认返回) |
| `percent` | (默认返回) |

---

### cyq_perf
**分类**: 沪深股票 > 特色数据 > 每日筹码及胜率-获取A股每日筹码平均成本和胜率情况，每天18~19点左右更新，数据从2018年开始

**说明**: /数据接口/沪深股票/特色数据/每日筹码及胜率-获取A股每日筹码平均成本和胜率情况，每天18~19点左右更新，数据从2018年开始

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, his_low, his_high, cost_5pct, cost_15pct, cost_50pct, cost_85pct, cost_95pct, weight_avg, winner_rate 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `his_low` | (默认返回) |
| `his_high` | (默认返回) |
| `cost_5pct` | (默认返回) |
| `cost_15pct` | (默认返回) |
| `cost_50pct` | (默认返回) |
| `cost_85pct` | (默认返回) |
| `cost_95pct` | (默认返回) |
| `weight_avg` | (默认返回) |
| `winner_rate` | (默认返回) |

---

### hk_hold
**分类**: 沪深股票 > 特色数据 > 沪深股通持股明细-获取沪深港股通持股明细，数据来源港交所。

**说明**: /数据接口/沪深股票/特色数据/沪深股通持股明细-获取沪深港股通持股明细，数据来源港交所。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `code` | string | 否 | 交易所代码 |
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 类型：SH沪股通（北向）SZ深股通（北向）HK港股通（南向持股） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: code, trade_date, ts_code, name, vol, ratio, exchange 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `code` | (默认返回) |
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `vol` | (默认返回) |
| `ratio` | (默认返回) |
| `exchange` | (默认返回) |

---

### stk_nineturn
**分类**: 沪深股票 > 特色数据 > 神奇九转指标-神奇九转（又称“九转序列”）是一种基于技术分析的股票趋势反转指标，其思想来源于技术分析大师汤姆·迪马克（Tom DeMark）的TD序列。该指标的核心功能是通过识别股价在上涨或下跌过程中连续9天的特定走势，来判断股价的潜在反转点，从而帮助投资者提高抄底和逃顶的成功率，日线级别配合60min的九转效果更好，数据从20230101开始。

**说明**: /数据接口/沪深股票/特色数据/神奇九转指标-神奇九转（又称“九转序列”）是一种基于技术分析的股票趋势反转指标，其思想来源于技术分析大师汤姆·迪马克（Tom DeMark）的TD序列。该指标的核心功能是通过识别股价在上涨或下跌过程中连续9天的特定走势，来判断股价的潜在反转点，从而帮助投资者提高抄底和逃顶的成功率，日线级别配合60min的九转效果更好，数据从20230101开始。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, freq, open, high, low, close, vol, amount, up_count, down_count, nine_up_turn, nine_down_turn 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 否 | 频率(日daily) |
| `start_date` | string | 否 | 开始时间 |
| `trade_date` | string | 否 | 交易日期 （格式：YYYY-MM-DD HH:MM:SS) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `freq` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `up_count` | (默认返回) |
| `down_count` | (默认返回) |
| `nine_up_turn` | (默认返回) |
| `nine_down_turn` | (默认返回) |

---

### stk_auction_o
**分类**: 沪深股票 > 特色数据 > 股票开盘集合竞价数据-股票开盘9:30集合竞价数据，每天盘后更新

**说明**: /数据接口/沪深股票/特色数据/股票开盘集合竞价数据-股票开盘9:30集合竞价数据，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期(YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, vol, amount, vwap 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期(YYYYMMDD) |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `vwap` | (默认返回) |

---

### stk_factor_pro
**分类**: 沪深股票 > 特色数据 > 股票技术面因子(专业版）-获取股票每日技术面因子数据，用于跟踪股票当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，_qfq表示前复权 _hfq表示后复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

**说明**: /数据接口/沪深股票/特色数据/股票技术面因子(专业版）-获取股票每日技术面因子数据，用于跟踪股票当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，_qfq表示前复权 _hfq表示后复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, open_hfq, open_qfq, high, high_hfq, high_qfq, low, low_hfq, low_qfq, close, close_hfq, close_qfq, pre_close, change, pct_chg, vol, amount, turnover_rate, turnover_rate_f, volume_ratio, pe, pe_ttm, pb... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(格式：yyyymmdd，下同) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `open_hfq` | (默认返回) |
| `open_qfq` | (默认返回) |
| `high` | (默认返回) |
| `high_hfq` | (默认返回) |
| `high_qfq` | (默认返回) |
| `low` | (默认返回) |
| `low_hfq` | (默认返回) |
| `low_qfq` | (默认返回) |
| `close` | (默认返回) |
| `close_hfq` | (默认返回) |
| `close_qfq` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `turnover_rate_f` | (默认返回) |
| `volume_ratio` | (默认返回) |
| `pe` | (默认返回) |
| `pe_ttm` | (默认返回) |
| `pb` | (默认返回) |
| `ps` | (默认返回) |
| `ps_ttm` | (默认返回) |
| `dv_ratio` | (默认返回) |
| `dv_ttm` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `free_share` | (默认返回) |
| `total_mv` | (默认返回) |
| `circ_mv` | (默认返回) |
| `adj_factor` | (默认返回) |
| `asi_bfq` | (默认返回) |
| `asi_hfq` | (默认返回) |
| `asi_qfq` | (默认返回) |
| `asit_bfq` | (默认返回) |
| `asit_hfq` | (默认返回) |
| `asit_qfq` | (默认返回) |
| `atr_bfq` | (默认返回) |
| `atr_hfq` | (默认返回) |
| `atr_qfq` | (默认返回) |
| `bbi_bfq` | (默认返回) |
| `bbi_hfq` | (默认返回) |
| `bbi_qfq` | (默认返回) |
| `bias1_bfq` | (默认返回) |
| `bias1_hfq` | (默认返回) |
| `bias1_qfq` | (默认返回) |
| `bias2_bfq` | (默认返回) |
| `bias2_hfq` | (默认返回) |
| `bias2_qfq` | (默认返回) |
| `bias3_bfq` | (默认返回) |
| `bias3_hfq` | (默认返回) |
| `bias3_qfq` | (默认返回) |
| `boll_lower_bfq` | (默认返回) |
| `boll_lower_hfq` | (默认返回) |
| `boll_lower_qfq` | (默认返回) |
| `boll_mid_bfq` | (默认返回) |
| `boll_mid_hfq` | (默认返回) |
| `boll_mid_qfq` | (默认返回) |
| `boll_upper_bfq` | (默认返回) |
| `boll_upper_hfq` | (默认返回) |
| `boll_upper_qfq` | (默认返回) |
| `brar_ar_bfq` | (默认返回) |
| `brar_ar_hfq` | (默认返回) |
| `brar_ar_qfq` | (默认返回) |
| `brar_br_bfq` | (默认返回) |
| `brar_br_hfq` | (默认返回) |
| `brar_br_qfq` | (默认返回) |
| `cci_bfq` | (默认返回) |
| `cci_hfq` | (默认返回) |
| `cci_qfq` | (默认返回) |
| `cr_bfq` | (默认返回) |
| `cr_hfq` | (默认返回) |
| `cr_qfq` | (默认返回) |
| `dfma_dif_bfq` | (默认返回) |
| `dfma_dif_hfq` | (默认返回) |
| `dfma_dif_qfq` | (默认返回) |
| `dfma_difma_bfq` | (默认返回) |
| `dfma_difma_hfq` | (默认返回) |
| `dfma_difma_qfq` | (默认返回) |
| `dmi_adx_bfq` | (默认返回) |
| `dmi_adx_hfq` | (默认返回) |
| `dmi_adx_qfq` | (默认返回) |
| `dmi_adxr_bfq` | (默认返回) |
| `dmi_adxr_hfq` | (默认返回) |
| `dmi_adxr_qfq` | (默认返回) |
| `dmi_mdi_bfq` | (默认返回) |
| `dmi_mdi_hfq` | (默认返回) |
| `dmi_mdi_qfq` | (默认返回) |
| `dmi_pdi_bfq` | (默认返回) |
| `dmi_pdi_hfq` | (默认返回) |
| `dmi_pdi_qfq` | (默认返回) |
| `downdays` | (默认返回) |
| `updays` | (默认返回) |
| `dpo_bfq` | (默认返回) |
| `dpo_hfq` | (默认返回) |
| `dpo_qfq` | (默认返回) |
| `madpo_bfq` | (默认返回) |
| `madpo_hfq` | (默认返回) |
| `madpo_qfq` | (默认返回) |
| `ema_bfq_10` | (默认返回) |
| `ema_bfq_20` | (默认返回) |
| `ema_bfq_250` | (默认返回) |
| `ema_bfq_30` | (默认返回) |
| `ema_bfq_5` | (默认返回) |
| `ema_bfq_60` | (默认返回) |
| `ema_bfq_90` | (默认返回) |
| `ema_hfq_10` | (默认返回) |
| `ema_hfq_20` | (默认返回) |
| `ema_hfq_250` | (默认返回) |
| `ema_hfq_30` | (默认返回) |
| `ema_hfq_5` | (默认返回) |
| `ema_hfq_60` | (默认返回) |
| `ema_hfq_90` | (默认返回) |
| `ema_qfq_10` | (默认返回) |
| `ema_qfq_20` | (默认返回) |
| `ema_qfq_250` | (默认返回) |
| `ema_qfq_30` | (默认返回) |
| `ema_qfq_5` | (默认返回) |
| `ema_qfq_60` | (默认返回) |
| `ema_qfq_90` | (默认返回) |
| `emv_bfq` | (默认返回) |
| `emv_hfq` | (默认返回) |
| `emv_qfq` | (默认返回) |
| `maemv_bfq` | (默认返回) |
| `maemv_hfq` | (默认返回) |
| `maemv_qfq` | (默认返回) |
| `expma_12_bfq` | (默认返回) |
| `expma_12_hfq` | (默认返回) |
| `expma_12_qfq` | (默认返回) |
| `expma_50_bfq` | (默认返回) |
| `expma_50_hfq` | (默认返回) |
| `expma_50_qfq` | (默认返回) |
| `kdj_bfq` | (默认返回) |
| `kdj_hfq` | (默认返回) |
| `kdj_qfq` | (默认返回) |
| `kdj_d_bfq` | (默认返回) |
| `kdj_d_hfq` | (默认返回) |
| `kdj_d_qfq` | (默认返回) |
| `kdj_k_bfq` | (默认返回) |
| `kdj_k_hfq` | (默认返回) |
| `kdj_k_qfq` | (默认返回) |
| `ktn_down_bfq` | (默认返回) |
| `ktn_down_hfq` | (默认返回) |
| `ktn_down_qfq` | (默认返回) |
| `ktn_mid_bfq` | (默认返回) |
| `ktn_mid_hfq` | (默认返回) |
| `ktn_mid_qfq` | (默认返回) |
| `ktn_upper_bfq` | (默认返回) |
| `ktn_upper_hfq` | (默认返回) |
| `ktn_upper_qfq` | (默认返回) |
| `lowdays` | (默认返回) |
| `topdays` | (默认返回) |
| `ma_bfq_10` | (默认返回) |
| `ma_bfq_20` | (默认返回) |
| `ma_bfq_250` | (默认返回) |
| `ma_bfq_30` | (默认返回) |
| `ma_bfq_5` | (默认返回) |
| `ma_bfq_60` | (默认返回) |
| `ma_bfq_90` | (默认返回) |
| `ma_hfq_10` | (默认返回) |
| `ma_hfq_20` | (默认返回) |
| `ma_hfq_250` | (默认返回) |
| `ma_hfq_30` | (默认返回) |
| `ma_hfq_5` | (默认返回) |
| `ma_hfq_60` | (默认返回) |
| `ma_hfq_90` | (默认返回) |
| `ma_qfq_10` | (默认返回) |
| `ma_qfq_20` | (默认返回) |
| `ma_qfq_250` | (默认返回) |
| `ma_qfq_30` | (默认返回) |
| `ma_qfq_5` | (默认返回) |
| `ma_qfq_60` | (默认返回) |
| `ma_qfq_90` | (默认返回) |
| `macd_bfq` | (默认返回) |
| `macd_hfq` | (默认返回) |
| `macd_qfq` | (默认返回) |
| `macd_dea_bfq` | (默认返回) |
| `macd_dea_hfq` | (默认返回) |
| `macd_dea_qfq` | (默认返回) |
| `macd_dif_bfq` | (默认返回) |
| `macd_dif_hfq` | (默认返回) |
| `macd_dif_qfq` | (默认返回) |
| `mass_bfq` | (默认返回) |
| `mass_hfq` | (默认返回) |
| `mass_qfq` | (默认返回) |
| `ma_mass_bfq` | (默认返回) |
| `ma_mass_hfq` | (默认返回) |
| `ma_mass_qfq` | (默认返回) |
| `mfi_bfq` | (默认返回) |
| `mfi_hfq` | (默认返回) |
| `mfi_qfq` | (默认返回) |
| `mtm_bfq` | (默认返回) |
| `mtm_hfq` | (默认返回) |
| `mtm_qfq` | (默认返回) |
| `mtmma_bfq` | (默认返回) |
| `mtmma_hfq` | (默认返回) |
| `mtmma_qfq` | (默认返回) |
| `obv_bfq` | (默认返回) |
| `obv_hfq` | (默认返回) |
| `obv_qfq` | (默认返回) |
| `psy_bfq` | (默认返回) |
| `psy_hfq` | (默认返回) |
| `psy_qfq` | (默认返回) |
| `psyma_bfq` | (默认返回) |
| `psyma_hfq` | (默认返回) |
| `psyma_qfq` | (默认返回) |
| `roc_bfq` | (默认返回) |
| `roc_hfq` | (默认返回) |
| `roc_qfq` | (默认返回) |
| `maroc_bfq` | (默认返回) |
| `maroc_hfq` | (默认返回) |
| `maroc_qfq` | (默认返回) |
| `rsi_bfq_12` | (默认返回) |
| `rsi_bfq_24` | (默认返回) |
| `rsi_bfq_6` | (默认返回) |
| `rsi_hfq_12` | (默认返回) |
| `rsi_hfq_24` | (默认返回) |
| `rsi_hfq_6` | (默认返回) |
| `rsi_qfq_12` | (默认返回) |
| `rsi_qfq_24` | (默认返回) |
| `rsi_qfq_6` | (默认返回) |
| `taq_down_bfq` | (默认返回) |
| `taq_down_hfq` | (默认返回) |
| `taq_down_qfq` | (默认返回) |
| `taq_mid_bfq` | (默认返回) |
| `taq_mid_hfq` | (默认返回) |
| `taq_mid_qfq` | (默认返回) |
| `taq_up_bfq` | (默认返回) |
| `taq_up_hfq` | (默认返回) |
| `taq_up_qfq` | (默认返回) |
| `trix_bfq` | (默认返回) |
| `trix_hfq` | (默认返回) |
| `trix_qfq` | (默认返回) |
| `trma_bfq` | (默认返回) |
| `trma_hfq` | (默认返回) |
| `trma_qfq` | (默认返回) |
| `vr_bfq` | (默认返回) |
| `vr_hfq` | (默认返回) |
| `vr_qfq` | (默认返回) |
| `wr_bfq` | (默认返回) |
| `wr_hfq` | (默认返回) |
| `wr_qfq` | (默认返回) |
| `wr1_bfq` | (默认返回) |
| `wr1_hfq` | (默认返回) |
| `wr1_qfq` | (默认返回) |
| `xsii_td1_bfq` | (默认返回) |
| `xsii_td1_hfq` | (默认返回) |
| `xsii_td1_qfq` | (默认返回) |
| `xsii_td2_bfq` | (默认返回) |
| `xsii_td2_hfq` | (默认返回) |
| `xsii_td2_qfq` | (默认返回) |
| `xsii_td3_bfq` | (默认返回) |
| `xsii_td3_hfq` | (默认返回) |
| `xsii_td3_qfq` | (默认返回) |
| `xsii_td4_bfq` | (默认返回) |
| `xsii_td4_hfq` | (默认返回) |
| `xsii_td4_qfq` | (默认返回) |

---

### stk_factor
**分类**: 沪深股票 > 特色数据 > 股票技术面因子-获取股票每日技术面因子数据，用于跟踪股票当前走势情况，数据由Tushare社区自产，覆盖全历史

**说明**: /数据接口/沪深股票/特色数据/股票技术面因子-获取股票每日技术面因子数据，用于跟踪股票当前走势情况，数据由Tushare社区自产，覆盖全历史

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_change, vol, amount, adj_factor, open_hfq, open_qfq, close_hfq, close_qfq, high_hfq, high_qfq, low_hfq, low_qfq, pre_close_hfq, pre_close_qfq, macd_dif, macd_... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （yyyymmdd，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `adj_factor` | (默认返回) |
| `open_hfq` | (默认返回) |
| `open_qfq` | (默认返回) |
| `close_hfq` | (默认返回) |
| `close_qfq` | (默认返回) |
| `high_hfq` | (默认返回) |
| `high_qfq` | (默认返回) |
| `low_hfq` | (默认返回) |
| `low_qfq` | (默认返回) |
| `pre_close_hfq` | (默认返回) |
| `pre_close_qfq` | (默认返回) |
| `macd_dif` | (默认返回) |
| `macd_dea` | (默认返回) |
| `macd` | (默认返回) |
| `kdj_k` | (默认返回) |
| `kdj_d` | (默认返回) |
| `kdj_j` | (默认返回) |
| `rsi_6` | (默认返回) |
| `rsi_12` | (默认返回) |
| `rsi_24` | (默认返回) |
| `boll_upper` | (默认返回) |
| `boll_mid` | (默认返回) |
| `boll_lower` | (默认返回) |
| `cci` | (默认返回) |

---

### stk_auction_c
**分类**: 沪深股票 > 特色数据 > 股票收盘集合竞价数据-股票收盘15:00集合竞价数据，每天盘后更新

**说明**: /数据接口/沪深股票/特色数据/股票收盘集合竞价数据-股票收盘15:00集合竞价数据，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期(YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, vol, amount, vwap 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期(YYYYMMDD) |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `vwap` | (默认返回) |

---

### rt_min_daily
**分类**: 沪深股票 > 行情数据 > A股实时分钟-日累计-获取A股当日盘中历史分钟数据，可以提取单只股票当日开盘以来的所有分钟数据

**说明**: /数据接口/沪深股票/行情数据/A股实时分钟-日累计-获取A股当日盘中历史分钟数据，可以提取单只股票当日开盘以来的所有分钟数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, freq, time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 频度：1MIN,5MIN,15MIN,30MIN,60MIN |
| `ts_code` | string | 是 | 股票代码，如：600000.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `freq` | (默认返回) |
| `time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### suspend
**分类**: 沪深股票 > 行情数据 > 停复牌信息(停)-获取股票每日停复牌信息

**说明**: /数据接口/沪深股票/行情数据/停复牌信息(停)-获取股票每日停复牌信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, suspend_date, resume_date, ann_date, suspend_reason, reason_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `resume_date` | string | 否 | 复牌日期(三选一) |
| `suspend_date` | string | 否 | 停牌日期(三选一) |
| `ts_code` | string | 否 | 股票代码(三选一) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `suspend_date` | (默认返回) |
| `resume_date` | (默认返回) |
| `ann_date` | (默认返回) |
| `suspend_reason` | (默认返回) |
| `reason_type` | (默认返回) |

---

### stk_mins
**分类**: 沪深股票 > 行情数据 > 历史分钟-获取A股分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK和 http Restful API两种方式

**说明**: /数据接口/沪深股票/行情数据/历史分钟-获取A股分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 格式：2023-08-25 19:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1min/5min/15min/30min/60min） |
| `start_date` | string | 否 | 开始日期 格式：2023-08-25 09:00:00 |
| `ts_code` | string | 是 | 股票代码，e.g. 600000.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### daily
**分类**: 沪深股票 > 行情数据 > 历史日线-获取股票行情数据，或通过[**通用行情接口**]( https: > tushare.pro > document > 2?doc_id=109)获取数据，包含了前后复权数据

**说明**: /数据接口/沪深股票/行情数据/历史日线-获取股票行情数据，或通过[**通用行情接口**]( https://tushare.pro/document/2?doc_id=109)获取数据，包含了前后复权数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期(YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期(YYYYMMDD) |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 否 | 股票代码（支持多个股票同时提取，逗号分隔） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### stk_week_month_adj
**分类**: 沪深股票 > 行情数据 > 周 > 月线复权行情(每日更新)-股票周 > 月线行情(复权--每日更新)

**说明**: /数据接口/沪深股票/行情数据/周/月线复权行情(每日更新)-股票周/月线行情(复权--每日更新)

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束交易日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, end_date, freq, open, high, low, close, pre_close, open_qfq, high_qfq, low_qfq, close_qfq, open_hfq, high_hfq, low_hfq, close_hfq, vol, amount, change, pct_chg 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 频率week周，month月 |
| `start_date` | string | 否 | 开始交易日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，每周或每月最后一天的日期） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `end_date` | (默认返回) |
| `freq` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `open_qfq` | (默认返回) |
| `high_qfq` | (默认返回) |
| `low_qfq` | (默认返回) |
| `close_qfq` | (默认返回) |
| `open_hfq` | (默认返回) |
| `high_hfq` | (默认返回) |
| `low_hfq` | (默认返回) |
| `close_hfq` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |

---

### stk_weekly_monthly
**分类**: 沪深股票 > 行情数据 > 周 > 月线行情(每日更新)-股票周 > 月线行情(每日更新)

**说明**: /数据接口/沪深股票/行情数据/周/月线行情(每日更新)-股票周/月线行情(每日更新)

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束交易日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, end_date, freq, open, high, low, close, pre_close, vol, amount, change, pct_chg 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 频率week周，month月 |
| `start_date` | string | 否 | 开始交易日期 |
| `trade_date` | string | 否 | 交易日期(格式：YYYYMMDD，每周或每月最后一天的日期） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `end_date` | (默认返回) |
| `freq` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |

---

### weekly
**分类**: 沪深股票 > 行情数据 > 周线行情-获取A股周线行情，本接口每周最后一个交易日更新，如需要使用每天更新的周线数据，请使用[日度更新的周线行情接口](https: > tushare.pro > document > 2?doc_id=336)。

**说明**: /数据接口/沪深股票/行情数据/周线行情-获取A股周线行情，本接口每周最后一个交易日更新，如需要使用每天更新的周线数据，请使用[日度更新的周线行情接口](https://tushare.pro/document/2?doc_id=336)。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （每周最后一个交易日期，YYYYMMDD格式） |
| `ts_code` | string | 否 | TS代码 （ts_code,trade_date两个参数任选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### bak_daily
**分类**: 沪深股票 > 行情数据 > 备用行情-获取备用行情，包括特定的行情指标(数据从2017年中左右开始，早期有几天数据缺失，近期正常)

**说明**: /数据接口/沪深股票/行情数据/备用行情-获取备用行情，包括特定的行情指标(数据从2017年中左右开始，早期有几天数据缺失，近期正常)

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, pct_change, close, change, open, high, low, pre_close, vol_ratio, turn_over, swing, vol, amount, selling, buying, total_share, float_share, pe, industry, area, float_mv, total_mv, avg_price, strength... |
| `limit` | string | 否 | 最大行数 |
| `offset` | string | 否 | 开始行数 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `pct_change` | (默认返回) |
| `close` | (默认返回) |
| `change` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `vol_ratio` | (默认返回) |
| `turn_over` | (默认返回) |
| `swing` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `selling` | (默认返回) |
| `buying` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `pe` | (默认返回) |
| `industry` | (默认返回) |
| `area` | (默认返回) |
| `float_mv` | (默认返回) |
| `total_mv` | (默认返回) |
| `avg_price` | (默认返回) |
| `strength` | (默认返回) |
| `activity` | (默认返回) |
| `avg_turnover` | (默认返回) |
| `attack` | (默认返回) |
| `interval_3` | (默认返回) |
| `interval_6` | (默认返回) |

---

### adj_factor
**分类**: 沪深股票 > 行情数据 > 复权因子-本接口由Tushare自行生产，获取股票复权因子，可提取单只股票全部历史复权因子，也可以提取单日全部股票的复权因子。

**说明**: /数据接口/沪深股票/行情数据/复权因子-本接口由Tushare自行生产，获取股票复权因子，可提取单只股票全部历史复权因子，也可以提取单日全部股票的复权因子。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, adj_factor 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD，下同) |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `adj_factor` | (默认返回) |

---

### rt_min
**分类**: 沪深股票 > 行情数据 > 实时分钟-获取全A股票实时分钟数据，包括1~60min

**说明**: /数据接口/沪深股票/行情数据/实时分钟-获取全A股票实时分钟数据，包括1~60min

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 1MIN,5MIN,15MIN,30MIN,60MIN （大写） |
| `ts_code` | string | 是 | 支持单个和多个：600000.SH 或者 600000.SH,000001.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### rt_k
**分类**: 沪深股票 > 行情数据 > 实时日线-获取实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情

**说明**: /数据接口/沪深股票/行情数据/实时日线-获取实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, pre_close, high, open, low, close, vol, amount, num 额外可选字段:   ask_price1: 委托卖盘（元）   bid_price1: 委托买盘（元）   trade_time: 交易时间   ask_volume1: 委托卖盘（股）   bid_volume1: 委托买盘（股） |
| `ts_code` | string | 是 | 支持通配符方式，e.g. 所有上交所股票：6\*.SH、所有创业板股票3\*.SZ、所有科创板股票688*.SH，或单个股票600000.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pre_close` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `num` | (默认返回) |
| `ask_price1` | 委托卖盘（元） |
| `bid_price1` | 委托买盘（元） |
| `trade_time` | 交易时间 |
| `ask_volume1` | 委托卖盘（股） |
| `bid_volume1` | 委托买盘（股） |

---

### monthly
**分类**: 沪深股票 > 行情数据 > 月线行情-获取A股月线数据

**说明**: /数据接口/沪深股票/行情数据/月线行情-获取A股月线数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （每月最后一个交易日日期，YYYYMMDD格式） |
| `ts_code` | string | 否 | TS代码 （ts_code,trade_date两个参数任选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### suspend_d
**分类**: 沪深股票 > 行情数据 > 每日停复牌信息-按日期方式获取股票每日停复牌信息

**说明**: /数据接口/沪深股票/行情数据/每日停复牌信息-按日期方式获取股票每日停复牌信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 停复牌查询结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, suspend_timing, suspend_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 停复牌查询开始日期 |
| `suspend_type` | string | 否 | 停复牌类型：S-停牌,R-复牌 |
| `trade_date` | string | 否 | 交易日日期 |
| `ts_code` | string | 否 | 股票代码(可输入多值) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `suspend_timing` | (默认返回) |
| `suspend_type` | (默认返回) |

---

### daily_basic
**分类**: 沪深股票 > 行情数据 > 每日指标-获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。单次请求最大返回6000条数据，可按日线循环提取全部历史。

**说明**: /数据接口/沪深股票/行情数据/每日指标-获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。单次请求最大返回6000条数据，可按日线循环提取全部历史。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期(YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, turnover_rate, turnover_rate_f, volume_ratio, pe, pe_ttm, pb, ps, ps_ttm, dv_ratio, dv_ttm, total_share, float_share, free_share, total_mv, circ_mv 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期(YYYYMMDD) |
| `trade_date` | string | 否 | 交易日期 （二选一） |
| `ts_code` | string | 是 | 股票代码（二选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `turnover_rate_f` | (默认返回) |
| `volume_ratio` | (默认返回) |
| `pe` | (默认返回) |
| `pe_ttm` | (默认返回) |
| `pb` | (默认返回) |
| `ps` | (默认返回) |
| `ps_ttm` | (默认返回) |
| `dv_ratio` | (默认返回) |
| `dv_ttm` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `free_share` | (默认返回) |
| `total_mv` | (默认返回) |
| `circ_mv` | (默认返回) |

---

### stk_limit
**分类**: 沪深股票 > 行情数据 > 每日涨跌停价格-获取全市场（包含A > B股和基金）每日涨跌停价格，包括涨停价格，跌停价格等，每个交易日8点40左右更新当日股票涨跌停价格。

**说明**: /数据接口/沪深股票/行情数据/每日涨跌停价格-获取全市场（包含A/B股和基金）每日涨跌停价格，包括涨停价格，跌停价格等，每个交易日8点40左右更新当日股票涨跌停价格。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, up_limit, down_limit 额外可选字段:   pre_close: 昨日收盘价 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `up_limit` | (默认返回) |
| `down_limit` | (默认返回) |
| `pre_close` | 昨日收盘价 |

---

### limit_list
**分类**: 沪深股票 > 行情数据 > 每日涨跌停统计-获取每日涨跌停股票统计，包括封闭时间和打开次数等数据，帮助用户快速定位近期强（弱）势股，以及研究超短线策略。

**说明**: /数据接口/沪深股票/行情数据/每日涨跌停统计-获取每日涨跌停股票统计，包括封闭时间和打开次数等数据，帮助用户快速定位近期强（弱）势股，以及研究超短线策略。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 YYYYMMDD格式 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, close, pct_chg, amp, fc_ratio, fl_ratio, fd_amount, first_time, last_time, open_times, strth, limit 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `limit_type` | string | 否 | 涨跌停类型：U涨停D跌停 |
| `start_date` | string | 否 | 开始日期 YYYYMMDD格式 |
| `trade_date` | string | 否 | 交易日期 YYYYMMDD格式，支持单个或多日期输入 |
| `ts_code` | string | 否 | 股票代码 （支持单个或多个股票输入） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `pct_chg` | (默认返回) |
| `amp` | (默认返回) |
| `fc_ratio` | (默认返回) |
| `fl_ratio` | (默认返回) |
| `fd_amount` | (默认返回) |
| `first_time` | (默认返回) |
| `last_time` | (默认返回) |
| `open_times` | (默认返回) |
| `strth` | (默认返回) |
| `limit` | (默认返回) |

---

### hsgt_top10
**分类**: 沪深股票 > 行情数据 > 沪深股通十大成交股-获取沪股通、深股通每日前十大成交详细数据，每天18~20点之间完成当日更新

**说明**: /数据接口/沪深股票/行情数据/沪深股通十大成交股-获取沪股通、深股通每日前十大成交详细数据，每天18~20点之间完成当日更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, close, change, rank, market_type, amount, net_amount, buy, sell 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `market_type` | string | 否 | 市场类型（1：沪市 3：深市） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（二选一） |
| `ts_code` | string | 否 | 股票代码（二选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `change` | (默认返回) |
| `rank` | (默认返回) |
| `market_type` | (默认返回) |
| `amount` | (默认返回) |
| `net_amount` | (默认返回) |
| `buy` | (默认返回) |
| `sell` | (默认返回) |

---

### ggt_top10
**分类**: 沪深股票 > 行情数据 > 港股通十大成交股-获取港股通每日成交数据，其中包括沪市、深市详细数据，每天18~20点之间完成当日更新

**说明**: /数据接口/沪深股票/行情数据/港股通十大成交股-获取港股通每日成交数据，其中包括沪市、深市详细数据，每天18~20点之间完成当日更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, close, p_change, rank, market_type, amount, net_amount, sh_amount, sh_net_amount, sh_buy, sh_sell, sz_amount, sz_net_amount, sz_buy, sz_sell 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `market_type` | string | 否 | 市场类型 2：港股通（沪） 4：港股通（深） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（二选一） |
| `ts_code` | string | 否 | 股票代码（二选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `close` | (默认返回) |
| `p_change` | (默认返回) |
| `rank` | (默认返回) |
| `market_type` | (默认返回) |
| `amount` | (默认返回) |
| `net_amount` | (默认返回) |
| `sh_amount` | (默认返回) |
| `sh_net_amount` | (默认返回) |
| `sh_buy` | (默认返回) |
| `sh_sell` | (默认返回) |
| `sz_amount` | (默认返回) |
| `sz_net_amount` | (默认返回) |
| `sz_buy` | (默认返回) |
| `sz_sell` | (默认返回) |

---

### ggt_daily
**分类**: 沪深股票 > 行情数据 > 港股通每日成交统计-获取港股通每日成交信息，数据从2014年开始

**说明**: /数据接口/沪深股票/行情数据/港股通每日成交统计-获取港股通每日成交信息，数据从2014年开始

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, buy_amount, buy_volume, sell_amount, sell_volume 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （格式YYYYMMDD，下同。支持单日和多日输入） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `buy_amount` | (默认返回) |
| `buy_volume` | (默认返回) |
| `sell_amount` | (默认返回) |
| `sell_volume` | (默认返回) |

---

### ggt_monthly
**分类**: 沪深股票 > 行情数据 > 港股通每月成交统计-港股通每月成交信息，数据从2014年开始

**说明**: /数据接口/沪深股票/行情数据/港股通每月成交统计-港股通每月成交信息，数据从2014年开始

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_month` | string | 否 | 结束月度 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, day_buy_amt, day_buy_vol, day_sell_amt, day_sell_vol, total_buy_amt, total_buy_vol, total_sell_amt, total_sell_vol 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `month` | string | 否 | 月度（格式YYYYMM，下同，支持多个输入） |
| `start_month` | string | 否 | 开始月度 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `day_buy_amt` | (默认返回) |
| `day_buy_vol` | (默认返回) |
| `day_sell_amt` | (默认返回) |
| `day_sell_vol` | (默认返回) |
| `total_buy_amt` | (默认返回) |
| `total_buy_vol` | (默认返回) |
| `total_sell_amt` | (默认返回) |
| `total_sell_vol` | (默认返回) |

---

### express
**分类**: 沪深股票 > 财务数据 > 业绩快报-获取上市公司业绩快报

**说明**: /数据接口/沪深股票/财务数据/业绩快报-获取上市公司业绩快报

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, revenue, operate_profit, total_profit, n_income, total_assets, total_hldr_eqy_exc_min_int, diluted_eps, diluted_roe, yoy_net_profit, bps, yoy_sales, yoy_op, yoy_tp, yoy_dedu_np, yoy_eps, yoy_roe, g... |
| `period` | string | 否 | 报告期(每个季度最后一天的日期,比如20171231表示年报，20170630半年报，20170930三季报) |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `revenue` | (默认返回) |
| `operate_profit` | (默认返回) |
| `total_profit` | (默认返回) |
| `n_income` | (默认返回) |
| `total_assets` | (默认返回) |
| `total_hldr_eqy_exc_min_int` | (默认返回) |
| `diluted_eps` | (默认返回) |
| `diluted_roe` | (默认返回) |
| `yoy_net_profit` | (默认返回) |
| `bps` | (默认返回) |
| `yoy_sales` | (默认返回) |
| `yoy_op` | (默认返回) |
| `yoy_tp` | (默认返回) |
| `yoy_dedu_np` | (默认返回) |
| `yoy_eps` | (默认返回) |
| `yoy_roe` | (默认返回) |
| `growth_assets` | (默认返回) |
| `yoy_equity` | (默认返回) |
| `growth_bps` | (默认返回) |
| `or_last_year` | (默认返回) |
| `op_last_year` | (默认返回) |
| `tp_last_year` | (默认返回) |
| `np_last_year` | (默认返回) |
| `eps_last_year` | (默认返回) |
| `open_net_assets` | (默认返回) |
| `open_bps` | (默认返回) |
| `perf_summary` | (默认返回) |
| `is_audit` | (默认返回) |
| `remark` | (默认返回) |

---

### forecast
**分类**: 沪深股票 > 财务数据 > 业绩预告-获取业绩预告数据

**说明**: /数据接口/沪深股票/财务数据/业绩预告-获取业绩预告数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 (二选一) |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, type, p_change_min, p_change_max, net_profit_min, net_profit_max, last_parent_net, first_ann_date, summary, change_reason 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期(每个季度最后一天的日期，比如20171231表示年报，20170630半年报，20170930三季报) |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | 股票代码(二选一) |
| `type` | string | 否 | 预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `type` | (默认返回) |
| `p_change_min` | (默认返回) |
| `p_change_max` | (默认返回) |
| `net_profit_min` | (默认返回) |
| `net_profit_max` | (默认返回) |
| `last_parent_net` | (默认返回) |
| `first_ann_date` | (默认返回) |
| `summary` | (默认返回) |
| `change_reason` | (默认返回) |

---

### fina_mainbz
**分类**: 沪深股票 > 财务数据 > 主营业务构成-获得上市公司主营业务构成，分地区和产品两种方式

**说明**: /数据接口/沪深股票/财务数据/主营业务构成-获得上市公司主营业务构成，分地区和产品两种方式

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, bz_item, bz_sales, bz_profit, bz_cost, curr_type, update_flag 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期(每个季度最后一天的日期,比如20171231表示年报) |
| `start_date` | string | 否 | 报告期开始日期 |
| `ts_code` | string | 是 | 股票代码 |
| `type` | string | 否 | 类型：P按产品 D按地区 I按行业（请输入大写字母P或者D） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `bz_item` | (默认返回) |
| `bz_sales` | (默认返回) |
| `bz_profit` | (默认返回) |
| `bz_cost` | (默认返回) |
| `curr_type` | (默认返回) |
| `update_flag` | (默认返回) |

---

### dividend
**分类**: 沪深股票 > 财务数据 > 分红送股数据-分红送股数据

**说明**: /数据接口/沪深股票/财务数据/分红送股数据-分红送股数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日 |
| `ex_date` | string | 否 | 除权除息日 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, ann_date, div_proc, stk_div, stk_bo_rate, stk_co_rate, cash_div, cash_div_tax, record_date, ex_date, pay_date, div_listdate, imp_ann_date 额外可选字段:   base_date: 基准日   base_share: 基准股本（万） |
| `imp_ann_date` | string | 否 | 实施公告日 |
| `record_date` | string | 否 | 股权登记日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `ann_date` | (默认返回) |
| `div_proc` | (默认返回) |
| `stk_div` | (默认返回) |
| `stk_bo_rate` | (默认返回) |
| `stk_co_rate` | (默认返回) |
| `cash_div` | (默认返回) |
| `cash_div_tax` | (默认返回) |
| `record_date` | (默认返回) |
| `ex_date` | (默认返回) |
| `pay_date` | (默认返回) |
| `div_listdate` | (默认返回) |
| `imp_ann_date` | (默认返回) |
| `base_date` | 基准日 |
| `base_share` | 基准股本（万） |

---

### income
**分类**: 沪深股票 > 财务数据 > 利润表-获取上市公司财务利润表数据

**说明**: /数据接口/沪深股票/财务数据/利润表-获取上市公司财务利润表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（YYYYMMDD格式，下同） |
| `comp_type` | string | 否 | 公司类型（1一般工商业2银行3保险4证券） |
| `end_date` | string | 否 | 公告日结束日期 |
| `f_ann_date` | string | 否 | 实际公告日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, f_ann_date, end_date, report_type, comp_type, end_type, basic_eps, diluted_eps, total_revenue, revenue, int_income, prem_earned, comm_income, n_commis_income, n_oth_income, n_oth_b_income, prem_income, out_p... |
| `period` | string | 否 | 报告期(每个季度最后一天的日期，比如20171231表示年报，20170630半年报，20170930三季报) |
| `report_type` | string | 否 | 报告类型，参考文档最下方说明 |
| `start_date` | string | 否 | 公告日开始日期 |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `f_ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `report_type` | (默认返回) |
| `comp_type` | (默认返回) |
| `end_type` | (默认返回) |
| `basic_eps` | (默认返回) |
| `diluted_eps` | (默认返回) |
| `total_revenue` | (默认返回) |
| `revenue` | (默认返回) |
| `int_income` | (默认返回) |
| `prem_earned` | (默认返回) |
| `comm_income` | (默认返回) |
| `n_commis_income` | (默认返回) |
| `n_oth_income` | (默认返回) |
| `n_oth_b_income` | (默认返回) |
| `prem_income` | (默认返回) |
| `out_prem` | (默认返回) |
| `une_prem_reser` | (默认返回) |
| `reins_income` | (默认返回) |
| `n_sec_tb_income` | (默认返回) |
| `n_sec_uw_income` | (默认返回) |
| `n_asset_mg_income` | (默认返回) |
| `oth_b_income` | (默认返回) |
| `fv_value_chg_gain` | (默认返回) |
| `invest_income` | (默认返回) |
| `ass_invest_income` | (默认返回) |
| `forex_gain` | (默认返回) |
| `total_cogs` | (默认返回) |
| `oper_cost` | (默认返回) |
| `int_exp` | (默认返回) |
| `comm_exp` | (默认返回) |
| `biz_tax_surchg` | (默认返回) |
| `sell_exp` | (默认返回) |
| `admin_exp` | (默认返回) |
| `fin_exp` | (默认返回) |
| `assets_impair_loss` | (默认返回) |
| `prem_refund` | (默认返回) |
| `compens_payout` | (默认返回) |
| `reser_insur_liab` | (默认返回) |
| `div_payt` | (默认返回) |
| `reins_exp` | (默认返回) |
| `oper_exp` | (默认返回) |
| `compens_payout_refu` | (默认返回) |
| `insur_reser_refu` | (默认返回) |
| `reins_cost_refund` | (默认返回) |
| `other_bus_cost` | (默认返回) |
| `operate_profit` | (默认返回) |
| `non_oper_income` | (默认返回) |
| `non_oper_exp` | (默认返回) |
| `nca_disploss` | (默认返回) |
| `total_profit` | (默认返回) |
| `income_tax` | (默认返回) |
| `n_income` | (默认返回) |
| `n_income_attr_p` | (默认返回) |
| `minority_gain` | (默认返回) |
| `oth_compr_income` | (默认返回) |
| `t_compr_income` | (默认返回) |
| `compr_inc_attr_p` | (默认返回) |
| `compr_inc_attr_m_s` | (默认返回) |
| `ebit` | (默认返回) |
| `ebitda` | (默认返回) |
| `insurance_exp` | (默认返回) |
| `undist_profit` | (默认返回) |
| `distable_profit` | (默认返回) |
| `rd_exp` | (默认返回) |
| `fin_exp_int_exp` | (默认返回) |
| `fin_exp_int_inc` | (默认返回) |
| `transfer_surplus_rese` | (默认返回) |
| `transfer_housing_imprest` | (默认返回) |
| `transfer_oth` | (默认返回) |
| `adj_lossgain` | (默认返回) |
| `withdra_legal_surplus` | (默认返回) |
| `withdra_legal_pubfund` | (默认返回) |
| `withdra_biz_devfund` | (默认返回) |
| `withdra_rese_fund` | (默认返回) |
| `withdra_oth_ersu` | (默认返回) |
| `workers_welfare` | (默认返回) |
| `distr_profit_shrhder` | (默认返回) |
| `prfshare_payable_dvd` | (默认返回) |
| `comshare_payable_dvd` | (默认返回) |
| `capit_comstock_div` | (默认返回) |
| `update_flag` | (默认返回) |
| `oth_income` | 其他收益 |
| `total_opcost` | 营业总成本（二） |
| `end_net_profit` | 终止经营净利润 |
| `credit_impa_loss` | 信用减值损失 |
| `asset_disp_income` | 资产处置收益 |
| `amodcost_fin_assets` | 以摊余成本计量的金融资产终止确认收益 |
| `continued_net_profit` | 持续经营净利润 |
| `oth_impair_loss_assets` | 其他资产减值损失 |
| `net_after_nr_lp_correct` | 扣除非经常性损益后的净利润（更正前） |
| `net_expo_hedging_benefits` | 净敞口套期收益 |

---

### cashflow
**分类**: 沪深股票 > 财务数据 > 现金流量表-获取上市公司现金流量表

**说明**: /数据接口/沪深股票/财务数据/现金流量表-获取上市公司现金流量表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（YYYYMMDD格式，下同） |
| `comp_type` | string | 否 | 公司类型：1一般工商业 2银行 3保险 4证券 |
| `end_date` | string | 否 | 公告日结束日期 |
| `f_ann_date` | string | 否 | 实际公告日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, f_ann_date, end_date, comp_type, report_type, end_type, net_profit, finan_exp, c_fr_sale_sg, recp_tax_rends, n_depos_incr_fi, n_incr_loans_cb, n_inc_borr_oth_fi, prem_fr_orig_contr, n_incr_insured_dep, n_rei... |
| `is_calc` | integer | 否 | 是否计算报表 |
| `period` | string | 否 | 报告期(每个季度最后一天的日期，比如20171231表示年报，20170630半年报，20170930三季报) |
| `report_type` | string | 否 | 报告类型：见下方详细说明 |
| `start_date` | string | 否 | 公告日开始日期 |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `f_ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `comp_type` | (默认返回) |
| `report_type` | (默认返回) |
| `end_type` | (默认返回) |
| `net_profit` | (默认返回) |
| `finan_exp` | (默认返回) |
| `c_fr_sale_sg` | (默认返回) |
| `recp_tax_rends` | (默认返回) |
| `n_depos_incr_fi` | (默认返回) |
| `n_incr_loans_cb` | (默认返回) |
| `n_inc_borr_oth_fi` | (默认返回) |
| `prem_fr_orig_contr` | (默认返回) |
| `n_incr_insured_dep` | (默认返回) |
| `n_reinsur_prem` | (默认返回) |
| `n_incr_disp_tfa` | (默认返回) |
| `ifc_cash_incr` | (默认返回) |
| `n_incr_disp_faas` | (默认返回) |
| `n_incr_loans_oth_bank` | (默认返回) |
| `n_cap_incr_repur` | (默认返回) |
| `c_fr_oth_operate_a` | (默认返回) |
| `c_inf_fr_operate_a` | (默认返回) |
| `c_paid_goods_s` | (默认返回) |
| `c_paid_to_for_empl` | (默认返回) |
| `c_paid_for_taxes` | (默认返回) |
| `n_incr_clt_loan_adv` | (默认返回) |
| `n_incr_dep_cbob` | (默认返回) |
| `c_pay_claims_orig_inco` | (默认返回) |
| `pay_handling_chrg` | (默认返回) |
| `pay_comm_insur_plcy` | (默认返回) |
| `oth_cash_pay_oper_act` | (默认返回) |
| `st_cash_out_act` | (默认返回) |
| `n_cashflow_act` | (默认返回) |
| `oth_recp_ral_inv_act` | (默认返回) |
| `c_disp_withdrwl_invest` | (默认返回) |
| `c_recp_return_invest` | (默认返回) |
| `n_recp_disp_fiolta` | (默认返回) |
| `n_recp_disp_sobu` | (默认返回) |
| `stot_inflows_inv_act` | (默认返回) |
| `c_pay_acq_const_fiolta` | (默认返回) |
| `c_paid_invest` | (默认返回) |
| `n_disp_subs_oth_biz` | (默认返回) |
| `oth_pay_ral_inv_act` | (默认返回) |
| `n_incr_pledge_loan` | (默认返回) |
| `stot_out_inv_act` | (默认返回) |
| `n_cashflow_inv_act` | (默认返回) |
| `c_recp_borrow` | (默认返回) |
| `proc_issue_bonds` | (默认返回) |
| `oth_cash_recp_ral_fnc_act` | (默认返回) |
| `stot_cash_in_fnc_act` | (默认返回) |
| `free_cashflow` | (默认返回) |
| `c_prepay_amt_borr` | (默认返回) |
| `c_pay_dist_dpcp_int_exp` | (默认返回) |
| `incl_dvd_profit_paid_sc_ms` | (默认返回) |
| `oth_cashpay_ral_fnc_act` | (默认返回) |
| `stot_cashout_fnc_act` | (默认返回) |
| `n_cash_flows_fnc_act` | (默认返回) |
| `eff_fx_flu_cash` | (默认返回) |
| `n_incr_cash_cash_equ` | (默认返回) |
| `c_cash_equ_beg_period` | (默认返回) |
| `c_cash_equ_end_period` | (默认返回) |
| `c_recp_cap_contrib` | (默认返回) |
| `incl_cash_rec_saims` | (默认返回) |
| `uncon_invest_loss` | (默认返回) |
| `prov_depr_assets` | (默认返回) |
| `depr_fa_coga_dpba` | (默认返回) |
| `amort_intang_assets` | (默认返回) |
| `lt_amort_deferred_exp` | (默认返回) |
| `decr_deferred_exp` | (默认返回) |
| `incr_acc_exp` | (默认返回) |
| `loss_disp_fiolta` | (默认返回) |
| `loss_scr_fa` | (默认返回) |
| `loss_fv_chg` | (默认返回) |
| `invest_loss` | (默认返回) |
| `decr_def_inc_tax_assets` | (默认返回) |
| `incr_def_inc_tax_liab` | (默认返回) |
| `decr_inventories` | (默认返回) |
| `decr_oper_payable` | (默认返回) |
| `incr_oper_payable` | (默认返回) |
| `others` | (默认返回) |
| `im_net_cashflow_oper_act` | (默认返回) |
| `conv_debt_into_cap` | (默认返回) |
| `conv_copbonds_due_within_1y` | (默认返回) |
| `fa_fnc_leases` | (默认返回) |
| `im_n_incr_cash_equ` | (默认返回) |
| `net_dism_capital_add` | (默认返回) |
| `net_cash_rece_sec` | (默认返回) |
| `credit_impa_loss` | (默认返回) |
| `use_right_asset_dep` | (默认返回) |
| `oth_loss_asset` | (默认返回) |
| `end_bal_cash` | (默认返回) |
| `beg_bal_cash` | (默认返回) |
| `end_bal_cash_equ` | (默认返回) |
| `beg_bal_cash_equ` | (默认返回) |
| `update_flag` | (默认返回) |

---

### fina_audit
**分类**: 沪深股票 > 财务数据 > 财务审计意见-获取上市公司定期财务审计意见数据

**说明**: /数据接口/沪深股票/财务数据/财务审计意见-获取上市公司定期财务审计意见数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, audit_result, audit_fees, audit_agency, audit_sign 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期(每个季度最后一天的日期,比如20171231表示年报) |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `audit_result` | (默认返回) |
| `audit_fees` | (默认返回) |
| `audit_agency` | (默认返回) |
| `audit_sign` | (默认返回) |

---

### fina_indicator
**分类**: 沪深股票 > 财务数据 > 财务指标数据-获取上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回100条记录，可通过设置日期多次请求获取更多数据。

**说明**: /数据接口/沪深股票/财务数据/财务指标数据-获取上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回100条记录，可通过设置日期多次请求获取更多数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, eps, dt_eps, total_revenue_ps, revenue_ps, capital_rese_ps, surplus_rese_ps, undist_profit_ps, extra_item, profit_dedt, gross_margin, current_ratio, quick_ratio, cash_ratio, ar_turn, ca_turn, fa_tu... |
| `period` | string | 否 | 报告期(每个季度最后一天的日期,比如20171231表示年报) |
| `start_date` | string | 否 | 报告期开始日期 |
| `ts_code` | string | 是 | TS股票代码,e.g. 600001.SH/000001.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `eps` | (默认返回) |
| `dt_eps` | (默认返回) |
| `total_revenue_ps` | (默认返回) |
| `revenue_ps` | (默认返回) |
| `capital_rese_ps` | (默认返回) |
| `surplus_rese_ps` | (默认返回) |
| `undist_profit_ps` | (默认返回) |
| `extra_item` | (默认返回) |
| `profit_dedt` | (默认返回) |
| `gross_margin` | (默认返回) |
| `current_ratio` | (默认返回) |
| `quick_ratio` | (默认返回) |
| `cash_ratio` | (默认返回) |
| `ar_turn` | (默认返回) |
| `ca_turn` | (默认返回) |
| `fa_turn` | (默认返回) |
| `assets_turn` | (默认返回) |
| `op_income` | (默认返回) |
| `ebit` | (默认返回) |
| `ebitda` | (默认返回) |
| `fcff` | (默认返回) |
| `fcfe` | (默认返回) |
| `current_exint` | (默认返回) |
| `noncurrent_exint` | (默认返回) |
| `interestdebt` | (默认返回) |
| `netdebt` | (默认返回) |
| `tangible_asset` | (默认返回) |
| `working_capital` | (默认返回) |
| `networking_capital` | (默认返回) |
| `invest_capital` | (默认返回) |
| `retained_earnings` | (默认返回) |
| `diluted2_eps` | (默认返回) |
| `bps` | (默认返回) |
| `ocfps` | (默认返回) |
| `retainedps` | (默认返回) |
| `cfps` | (默认返回) |
| `ebit_ps` | (默认返回) |
| `fcff_ps` | (默认返回) |
| `fcfe_ps` | (默认返回) |
| `netprofit_margin` | (默认返回) |
| `grossprofit_margin` | (默认返回) |
| `cogs_of_sales` | (默认返回) |
| `expense_of_sales` | (默认返回) |
| `profit_to_gr` | (默认返回) |
| `saleexp_to_gr` | (默认返回) |
| `adminexp_of_gr` | (默认返回) |
| `finaexp_of_gr` | (默认返回) |
| `impai_ttm` | (默认返回) |
| `gc_of_gr` | (默认返回) |
| `op_of_gr` | (默认返回) |
| `ebit_of_gr` | (默认返回) |
| `roe` | (默认返回) |
| `roe_waa` | (默认返回) |
| `roe_dt` | (默认返回) |
| `roa` | (默认返回) |
| `npta` | (默认返回) |
| `roic` | (默认返回) |
| `roe_yearly` | (默认返回) |
| `roa2_yearly` | (默认返回) |
| `debt_to_assets` | (默认返回) |
| `assets_to_eqt` | (默认返回) |
| `dp_assets_to_eqt` | (默认返回) |
| `ca_to_assets` | (默认返回) |
| `nca_to_assets` | (默认返回) |
| `tbassets_to_totalassets` | (默认返回) |
| `int_to_talcap` | (默认返回) |
| `eqt_to_talcapital` | (默认返回) |
| `currentdebt_to_debt` | (默认返回) |
| `longdeb_to_debt` | (默认返回) |
| `ocf_to_shortdebt` | (默认返回) |
| `debt_to_eqt` | (默认返回) |
| `eqt_to_debt` | (默认返回) |
| `eqt_to_interestdebt` | (默认返回) |
| `tangibleasset_to_debt` | (默认返回) |
| `tangasset_to_intdebt` | (默认返回) |
| `tangibleasset_to_netdebt` | (默认返回) |
| `ocf_to_debt` | (默认返回) |
| `turn_days` | (默认返回) |
| `roa_yearly` | (默认返回) |
| `roa_dp` | (默认返回) |
| `fixed_assets` | (默认返回) |
| `profit_to_op` | (默认返回) |
| `q_saleexp_to_gr` | (默认返回) |
| `q_gc_to_gr` | (默认返回) |
| `q_roe` | (默认返回) |
| `q_dt_roe` | (默认返回) |
| `q_npta` | (默认返回) |
| `q_ocf_to_sales` | (默认返回) |
| `basic_eps_yoy` | (默认返回) |
| `dt_eps_yoy` | (默认返回) |
| `cfps_yoy` | (默认返回) |
| `op_yoy` | (默认返回) |
| `ebt_yoy` | (默认返回) |
| `netprofit_yoy` | (默认返回) |
| `dt_netprofit_yoy` | (默认返回) |
| `ocf_yoy` | (默认返回) |
| `roe_yoy` | (默认返回) |
| `bps_yoy` | (默认返回) |
| `assets_yoy` | (默认返回) |
| `eqt_yoy` | (默认返回) |
| `tr_yoy` | (默认返回) |
| `or_yoy` | (默认返回) |
| `q_sales_yoy` | (默认返回) |
| `q_op_qoq` | (默认返回) |
| `equity_yoy` | (默认返回) |
| `daa` | 折旧与摊销 |
| `q_eps` | 每股收益(单季度) |
| `rd_exp` | 研发费用 |
| `roe_avg` | 平均净资产收益率(增发条件) |
| `inv_turn` | 存货周转率 |
| `q_gr_qoq` | 营业总收入环比增长率(%)(单季度) |
| `q_gr_yoy` | 营业总收入同比增长率(%)(单季度) |
| `q_op_yoy` | 营业利润同比增长率(%)(单季度) |
| `ocf_to_or` | 经营活动产生的现金流量净额/营业收入 |
| `op_to_ebt` | 营业利润／利润总额 |
| `nop_to_ebt` | 非营业利润／利润总额 |
| `op_to_debt` | 营业利润／负债合计 |
| `q_dtprofit` | 扣除非经常损益后的单季度净利润 |
| `q_op_to_gr` | 营业利润／营业总收入(单季度) |
| `q_opincome` | 经营活动单季度净收益 |
| `tax_to_ebt` | 所得税/利润总额 |
| `arturn_days` | 应收账款周转天数 |
| `q_ocf_to_or` | 经营活动产生的现金流量净额／经营活动净收益(单季度) |
| `q_sales_qoq` | 营业收入环比增长率(%)(单季度) |
| `roic_yearly` | 年化投入资本回报率 |
| `update_flag` | 更新标识 |
| `invturn_days` | 存货周转天数 |
| `q_profit_qoq` | 净利润环比增长率(%)(单季度) |
| `q_profit_yoy` | 净利润同比增长率(%)(单季度) |
| `non_op_profit` | 非营业利润 |
| `ocf_to_profit` | 经营活动产生的现金流量净额／营业利润 |
| `op_to_liqdebt` | 营业利润／流动负债 |
| `total_fa_trun` | 固定资产合计周转率 |
| `ebitda_to_debt` | 息税折旧摊销前利润/负债合计 |
| `interst_income` | 利息费用 |
| `ocf_to_netdebt` | 经营活动产生的现金流量净额/净债务 |
| `q_exp_to_sales` | 销售期间费用率(单季度) |
| `q_investincome` | 价值变动单季度净收益 |
| `q_profit_to_gr` | 净利润／营业总收入(单季度) |
| `cash_to_liqdebt` | 货币资金／流动负债 |
| `ocf_to_opincome` | 经营活动产生的现金流量净额/经营活动净收益 |
| `opincome_of_ebt` | 经营活动净收益/利润总额 |
| `q_finaexp_to_gr` | 财务费用／营业总收入 (单季度) |
| `q_netprofit_qoq` | 归属母公司股东的净利润环比增长率(%)(单季度) |
| `q_netprofit_yoy` | 归属母公司股东的净利润同比增长率(%)(单季度) |
| `salescash_to_or` | 销售商品提供劳务收到的现金/营业收入 |
| `ebit_to_interest` | 已获利息倍数(EBIT/利息费用) |
| `q_adminexp_to_gr` | 管理费用／营业总收入 (单季度) |
| `capitalized_to_da` | 资本支出/折旧和摊销 |
| `profit_prefin_exp` | 扣除财务费用前营业利润 |
| `q_gsprofit_margin` | 销售毛利率(单季度) |
| `q_opincome_to_ebt` | 经营活动净收益／利润总额(单季度) |
| `q_salescash_to_or` | 销售商品提供劳务收到的现金／营业收入(单季度) |
| `dtprofit_to_profit` | 扣除非经常损益后的净利润/净利润 |
| `n_op_profit_of_ebt` | 营业外收支净额/利润总额 |
| `q_impair_to_gr_ttm` | 资产减值损失／营业总收入(单季度) |
| `q_netprofit_margin` | 销售净利率(单季度) |
| `valuechange_income` | 价值变动净收益 |
| `investincome_of_ebt` | 价值变动净收益/利润总额 |
| `ocf_to_interestdebt` | 经营活动产生的现金流量净额/带息债务 |
| `q_dtprofit_to_profit` | 扣除非经常损益后的净利润／净利润(单季度) |
| `q_investincome_to_ebt` | 价值变动净收益／利润总额(单季度) |
| `longdebt_to_workingcapital` | 长期债务与营运资金比率 |
| `cash_to_liqdebt_withinterest` | 货币资金／带息流动负债 |

---

### disclosure_date
**分类**: 沪深股票 > 财务数据 > 财报披露日期表-获取财报披露计划日期

**说明**: /数据接口/沪深股票/财务数据/财报披露日期表-获取财报披露计划日期

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `actual_date` | string | 否 | 实际披露日期 |
| `ann_date` | string | 否 | 最新披露公告日 |
| `end_date` | string | 否 | 财报周期（每个季度最后一天的日期，比如20181231表示2018年年报，20180630表示中报) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, pre_date, actual_date 额外可选字段:   modify_date: 披露日期修正记录 |
| `pre_date` | string | 否 | 计划披露日期 |
| `ts_code` | string | 否 | TS股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `pre_date` | (默认返回) |
| `actual_date` | (默认返回) |
| `modify_date` | 披露日期修正记录 |

---

### balancesheet
**分类**: 沪深股票 > 财务数据 > 资产负债表-获取上市公司资产负债表

**说明**: /数据接口/沪深股票/财务数据/资产负债表-获取上市公司资产负债表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期(YYYYMMDD格式，下同) |
| `comp_type` | string | 否 | 公司类型：1一般工商业 2银行 3保险 4证券 |
| `end_date` | string | 否 | 公告日结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, f_ann_date, end_date, report_type, comp_type, end_type, total_share, cap_rese, undistr_porfit, surplus_rese, special_rese, money_cap, trad_asset, notes_receiv, accounts_receiv, oth_receiv, prepayment, div_re... |
| `period` | string | 否 | 报告期(每个季度最后一天的日期，比如20171231表示年报，20170630半年报，20170930三季报) |
| `report_type` | string | 否 | 报告类型：见下方详细说明 |
| `start_date` | string | 否 | 公告日开始日期 |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `f_ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `report_type` | (默认返回) |
| `comp_type` | (默认返回) |
| `end_type` | (默认返回) |
| `total_share` | (默认返回) |
| `cap_rese` | (默认返回) |
| `undistr_porfit` | (默认返回) |
| `surplus_rese` | (默认返回) |
| `special_rese` | (默认返回) |
| `money_cap` | (默认返回) |
| `trad_asset` | (默认返回) |
| `notes_receiv` | (默认返回) |
| `accounts_receiv` | (默认返回) |
| `oth_receiv` | (默认返回) |
| `prepayment` | (默认返回) |
| `div_receiv` | (默认返回) |
| `int_receiv` | (默认返回) |
| `inventories` | (默认返回) |
| `amor_exp` | (默认返回) |
| `nca_within_1y` | (默认返回) |
| `sett_rsrv` | (默认返回) |
| `loanto_oth_bank_fi` | (默认返回) |
| `premium_receiv` | (默认返回) |
| `reinsur_receiv` | (默认返回) |
| `reinsur_res_receiv` | (默认返回) |
| `pur_resale_fa` | (默认返回) |
| `oth_cur_assets` | (默认返回) |
| `total_cur_assets` | (默认返回) |
| `fa_avail_for_sale` | (默认返回) |
| `htm_invest` | (默认返回) |
| `lt_eqt_invest` | (默认返回) |
| `invest_real_estate` | (默认返回) |
| `time_deposits` | (默认返回) |
| `oth_assets` | (默认返回) |
| `lt_rec` | (默认返回) |
| `fix_assets` | (默认返回) |
| `cip` | (默认返回) |
| `const_materials` | (默认返回) |
| `fixed_assets_disp` | (默认返回) |
| `produc_bio_assets` | (默认返回) |
| `oil_and_gas_assets` | (默认返回) |
| `intan_assets` | (默认返回) |
| `r_and_d` | (默认返回) |
| `goodwill` | (默认返回) |
| `lt_amor_exp` | (默认返回) |
| `defer_tax_assets` | (默认返回) |
| `decr_in_disbur` | (默认返回) |
| `oth_nca` | (默认返回) |
| `total_nca` | (默认返回) |
| `cash_reser_cb` | (默认返回) |
| `depos_in_oth_bfi` | (默认返回) |
| `prec_metals` | (默认返回) |
| `deriv_assets` | (默认返回) |
| `rr_reins_une_prem` | (默认返回) |
| `rr_reins_outstd_cla` | (默认返回) |
| `rr_reins_lins_liab` | (默认返回) |
| `rr_reins_lthins_liab` | (默认返回) |
| `refund_depos` | (默认返回) |
| `ph_pledge_loans` | (默认返回) |
| `refund_cap_depos` | (默认返回) |
| `indep_acct_assets` | (默认返回) |
| `client_depos` | (默认返回) |
| `client_prov` | (默认返回) |
| `transac_seat_fee` | (默认返回) |
| `invest_as_receiv` | (默认返回) |
| `total_assets` | (默认返回) |
| `lt_borr` | (默认返回) |
| `st_borr` | (默认返回) |
| `cb_borr` | (默认返回) |
| `depos_ib_deposits` | (默认返回) |
| `loan_oth_bank` | (默认返回) |
| `trading_fl` | (默认返回) |
| `notes_payable` | (默认返回) |
| `acct_payable` | (默认返回) |
| `adv_receipts` | (默认返回) |
| `sold_for_repur_fa` | (默认返回) |
| `comm_payable` | (默认返回) |
| `payroll_payable` | (默认返回) |
| `taxes_payable` | (默认返回) |
| `int_payable` | (默认返回) |
| `div_payable` | (默认返回) |
| `oth_payable` | (默认返回) |
| `acc_exp` | (默认返回) |
| `deferred_inc` | (默认返回) |
| `st_bonds_payable` | (默认返回) |
| `payable_to_reinsurer` | (默认返回) |
| `rsrv_insur_cont` | (默认返回) |
| `acting_trading_sec` | (默认返回) |
| `acting_uw_sec` | (默认返回) |
| `non_cur_liab_due_1y` | (默认返回) |
| `oth_cur_liab` | (默认返回) |
| `total_cur_liab` | (默认返回) |
| `bond_payable` | (默认返回) |
| `lt_payable` | (默认返回) |
| `specific_payables` | (默认返回) |
| `estimated_liab` | (默认返回) |
| `defer_tax_liab` | (默认返回) |
| `defer_inc_non_cur_liab` | (默认返回) |
| `oth_ncl` | (默认返回) |
| `total_ncl` | (默认返回) |
| `depos_oth_bfi` | (默认返回) |
| `deriv_liab` | (默认返回) |
| `depos` | (默认返回) |
| `agency_bus_liab` | (默认返回) |
| `oth_liab` | (默认返回) |
| `prem_receiv_adva` | (默认返回) |
| `depos_received` | (默认返回) |
| `ph_invest` | (默认返回) |
| `reser_une_prem` | (默认返回) |
| `reser_outstd_claims` | (默认返回) |
| `reser_lins_liab` | (默认返回) |
| `reser_lthins_liab` | (默认返回) |
| `indept_acc_liab` | (默认返回) |
| `pledge_borr` | (默认返回) |
| `indem_payable` | (默认返回) |
| `policy_div_payable` | (默认返回) |
| `total_liab` | (默认返回) |
| `treasury_share` | (默认返回) |
| `ordin_risk_reser` | (默认返回) |
| `forex_differ` | (默认返回) |
| `invest_loss_unconf` | (默认返回) |
| `minority_int` | (默认返回) |
| `total_hldr_eqy_exc_min_int` | (默认返回) |
| `total_hldr_eqy_inc_min_int` | (默认返回) |
| `total_liab_hldr_eqy` | (默认返回) |
| `lt_payroll_payable` | (默认返回) |
| `oth_comp_income` | (默认返回) |
| `oth_eqt_tools` | (默认返回) |
| `oth_eqt_tools_p_shr` | (默认返回) |
| `lending_funds` | (默认返回) |
| `acc_receivable` | (默认返回) |
| `st_fin_payable` | (默认返回) |
| `payables` | (默认返回) |
| `hfs_assets` | (默认返回) |
| `hfs_sales` | (默认返回) |
| `cost_fin_assets` | (默认返回) |
| `fair_value_fin_assets` | (默认返回) |
| `cip_total` | (默认返回) |
| `oth_pay_total` | (默认返回) |
| `long_pay_total` | (默认返回) |
| `debt_invest` | (默认返回) |
| `oth_debt_invest` | (默认返回) |
| `contract_assets` | (默认返回) |
| `contract_liab` | (默认返回) |
| `accounts_receiv_bill` | (默认返回) |
| `accounts_pay` | (默认返回) |
| `oth_rcv_total` | (默认返回) |
| `fix_assets_total` | (默认返回) |
| `update_flag` | (默认返回) |
| `lease_liab` | 租赁负债 |
| `oth_eq_invest` | 其他权益工具投资(元) |
| `oth_eq_ppbond` | 其他权益工具:永续债(元) |
| `receiv_financing` | 应收款项融资 |
| `use_right_assets` | 使用权资产 |
| `oth_illiq_fin_assets` | 其他非流动金融资产(元) |

---

### moneyflow
**分类**: 沪深股票 > 资金流向数据 > 个股资金流向-获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向，数据开始于2010年。

**说明**: /数据接口/沪深股票/资金流向数据/个股资金流向-获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向，数据开始于2010年。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, buy_sm_vol, buy_sm_amount, sell_sm_vol, sell_sm_amount, buy_md_vol, buy_md_amount, sell_md_vol, sell_md_amount, buy_lg_vol, buy_lg_amount, sell_lg_vol, sell_lg_amount, buy_elg_vol, buy_elg_amount, sell_elg... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 （股票和时间参数至少输入一个） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `buy_sm_vol` | (默认返回) |
| `buy_sm_amount` | (默认返回) |
| `sell_sm_vol` | (默认返回) |
| `sell_sm_amount` | (默认返回) |
| `buy_md_vol` | (默认返回) |
| `buy_md_amount` | (默认返回) |
| `sell_md_vol` | (默认返回) |
| `sell_md_amount` | (默认返回) |
| `buy_lg_vol` | (默认返回) |
| `buy_lg_amount` | (默认返回) |
| `sell_lg_vol` | (默认返回) |
| `sell_lg_amount` | (默认返回) |
| `buy_elg_vol` | (默认返回) |
| `buy_elg_amount` | (默认返回) |
| `sell_elg_vol` | (默认返回) |
| `sell_elg_amount` | (默认返回) |
| `net_mf_vol` | (默认返回) |
| `net_mf_amount` | (默认返回) |

---

### moneyflow_dc
**分类**: 沪深股票 > 资金流向数据 > 个股资金流向（DC）-获取东方财富个股资金流向数据，每日盘后更新，数据开始于20230911

**说明**: /数据接口/沪深股票/资金流向数据/个股资金流向（DC）-获取东方财富个股资金流向数据，每日盘后更新，数据开始于20230911

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, pct_change, close, net_amount, net_amount_rate, buy_elg_amount, buy_elg_amount_rate, buy_lg_amount, buy_lg_amount_rate, buy_md_amount, buy_md_amount_rate, buy_sm_amount, buy_sm_amount_rate 额外可选字段:   ... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pct_change` | (默认返回) |
| `close` | (默认返回) |
| `net_amount` | (默认返回) |
| `net_amount_rate` | (默认返回) |
| `buy_elg_amount` | (默认返回) |
| `buy_elg_amount_rate` | (默认返回) |
| `buy_lg_amount` | (默认返回) |
| `buy_lg_amount_rate` | (默认返回) |
| `buy_md_amount` | (默认返回) |
| `buy_md_amount_rate` | (默认返回) |
| `buy_sm_amount` | (默认返回) |
| `buy_sm_amount_rate` | (默认返回) |

---

### moneyflow_ths
**分类**: 沪深股票 > 资金流向数据 > 个股资金流向（THS）-获取同花顺个股资金流向数据，每日盘后更新

**说明**: /数据接口/沪深股票/资金流向数据/个股资金流向（THS）-获取同花顺个股资金流向数据，每日盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, pct_change, latest, net_amount, net_d5_amount, buy_lg_amount, buy_lg_amount_rate, buy_md_amount, buy_md_amount_rate, buy_sm_amount, buy_sm_amount_rate 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pct_change` | (默认返回) |
| `latest` | (默认返回) |
| `net_amount` | (默认返回) |
| `net_d5_amount` | (默认返回) |
| `buy_lg_amount` | (默认返回) |
| `buy_lg_amount_rate` | (默认返回) |
| `buy_md_amount` | (默认返回) |
| `buy_md_amount_rate` | (默认返回) |
| `buy_sm_amount` | (默认返回) |
| `buy_sm_amount_rate` | (默认返回) |

---

### moneyflow_mkt_dc
**分类**: 沪深股票 > 资金流向数据 > 大盘资金流向（DC）-获取东方财富大盘资金流向数据，每日盘后更新

**说明**: /数据接口/沪深股票/资金流向数据/大盘资金流向（DC）-获取东方财富大盘资金流向数据，每日盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, close_sh, pct_change_sh, close_sz, pct_change_sz, net_amount, net_amount_rate, buy_elg_amount, buy_elg_amount_rate, buy_lg_amount, buy_lg_amount_rate, buy_md_amount, buy_md_amount_rate, buy_sm_amount, buy_sm_amount... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `close_sh` | (默认返回) |
| `pct_change_sh` | (默认返回) |
| `close_sz` | (默认返回) |
| `pct_change_sz` | (默认返回) |
| `net_amount` | (默认返回) |
| `net_amount_rate` | (默认返回) |
| `buy_elg_amount` | (默认返回) |
| `buy_elg_amount_rate` | (默认返回) |
| `buy_lg_amount` | (默认返回) |
| `buy_lg_amount_rate` | (默认返回) |
| `buy_md_amount` | (默认返回) |
| `buy_md_amount_rate` | (默认返回) |
| `buy_sm_amount` | (默认返回) |
| `buy_sm_amount_rate` | (默认返回) |

---

### moneyflow_ind_dc
**分类**: 沪深股票 > 资金流向数据 > 板块资金流向（DC）-获取东方财富板块资金流向，每天盘后更新

**说明**: /数据接口/沪深股票/资金流向数据/板块资金流向（DC）-获取东方财富板块资金流向，每天盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `content_type` | string | 否 | 资金类型(行业、概念、地域) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, content_type, ts_code, name, pct_change, close, net_amount, net_amount_rate, buy_elg_amount, buy_elg_amount_rate, buy_lg_amount, buy_lg_amount_rate, buy_md_amount, buy_md_amount_rate, buy_sm_amount, buy_sm_amount_r... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `content_type` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pct_change` | (默认返回) |
| `close` | (默认返回) |
| `net_amount` | (默认返回) |
| `net_amount_rate` | (默认返回) |
| `buy_elg_amount` | (默认返回) |
| `buy_elg_amount_rate` | (默认返回) |
| `buy_lg_amount` | (默认返回) |
| `buy_lg_amount_rate` | (默认返回) |
| `buy_md_amount` | (默认返回) |
| `buy_md_amount_rate` | (默认返回) |
| `buy_sm_amount` | (默认返回) |
| `buy_sm_amount_rate` | (默认返回) |
| `buy_sm_amount_stock` | (默认返回) |
| `rank` | (默认返回) |

---

### moneyflow_cnt_ths
**分类**: 沪深股票 > 资金流向数据 > 板块资金流向（THS)-获取同花顺概念板块每日资金流向

**说明**: /数据接口/沪深股票/资金流向数据/板块资金流向（THS)-获取同花顺概念板块每日资金流向

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, lead_stock, close_price, pct_change, industry_index, company_num, pct_change_stock, net_buy_amount, net_sell_amount, net_amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(格式：YYYYMMDD，下同) |
| `ts_code` | string | 否 | 代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `lead_stock` | (默认返回) |
| `close_price` | (默认返回) |
| `pct_change` | (默认返回) |
| `industry_index` | (默认返回) |
| `company_num` | (默认返回) |
| `pct_change_stock` | (默认返回) |
| `net_buy_amount` | (默认返回) |
| `net_sell_amount` | (默认返回) |
| `net_amount` | (默认返回) |

---

### moneyflow_hsgt
**分类**: 沪深股票 > 资金流向数据 > 沪深港通资金流向-获取沪股通、深股通、港股通每日资金流向数据，每次最多返回300条记录，总量不限制。

**说明**: /数据接口/沪深股票/资金流向数据/沪深港通资金流向-获取沪股通、深股通、港股通每日资金流向数据，每次最多返回300条记录，总量不限制。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ggt_ss, ggt_sz, hgt, sgt, north_money, south_money 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 (二选一) |
| `trade_date` | string | 否 | 交易日期 (二选一) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ggt_ss` | (默认返回) |
| `ggt_sz` | (默认返回) |
| `hgt` | (默认返回) |
| `sgt` | (默认返回) |
| `north_money` | (默认返回) |
| `south_money` | (默认返回) |

---

### moneyflow_ind_ths
**分类**: 沪深股票 > 资金流向数据 > 行业资金流向（THS）-获取同花顺行业资金流向，每日盘后更新

**说明**: /数据接口/沪深股票/资金流向数据/行业资金流向（THS）-获取同花顺行业资金流向，每日盘后更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, industry, lead_stock, close, pct_change, company_num, pct_change_stock, close_price, net_buy_amount, net_sell_amount, net_amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `industry` | (默认返回) |
| `lead_stock` | (默认返回) |
| `close` | (默认返回) |
| `pct_change` | (默认返回) |
| `company_num` | (默认返回) |
| `pct_change_stock` | (默认返回) |
| `close_price` | (默认返回) |
| `net_buy_amount` | (默认返回) |
| `net_sell_amount` | (默认返回) |
| `net_amount` | (默认返回) |

---

## 股票数据

共 4 个工具

### p_save
**分类**: 股票数据 > 自选股组合 > 自选股组合保存-创建或修改自选股组合

**说明**: /数据接口/股票数据/自选股组合/自选股组合保存-创建或修改自选股组合

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `desc` | string | 否 | 组合描述 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: id, ts_code, ts_type, name, desc, weight, create_time, update_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `items` | array | 是 | 成份列表 |
| `name` | string | 是 | 组合名称 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `id` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_type` | (默认返回) |
| `name` | (默认返回) |
| `desc` | (默认返回) |
| `weight` | (默认返回) |
| `create_time` | (默认返回) |
| `update_time` | (默认返回) |

---

### p_delete
**分类**: 股票数据 > 自选股组合 > 自选股组合删除-删除自选股组合

**说明**: /数据接口/股票数据/自选股组合/自选股组合删除-删除自选股组合

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: status 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | integer | 是 | 组合名称 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `status` | (默认返回) |

---

### p_get
**分类**: 股票数据 > 自选股组合 > 自选股组合成分查询-查询组合的成分列表

**说明**: /数据接口/股票数据/自选股组合/自选股组合成分查询-查询组合的成分列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: id, ts_code, ts_type, name, desc, weight, create_time, update_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 是 | 组合名称 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `id` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_type` | (默认返回) |
| `name` | (默认返回) |
| `desc` | (默认返回) |
| `weight` | (默认返回) |
| `create_time` | (默认返回) |
| `update_time` | (默认返回) |

---

### p_list
**分类**: 股票数据 > 自选股组合 > 自选股组合查询-自选股组合查询，不加参数查询出所以自定义组合

**说明**: /数据接口/股票数据/自选股组合/自选股组合查询-自选股组合查询，不加参数查询出所以自定义组合

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: id, name, desc, create_time, update_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 组合名称 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `id` | (默认返回) |
| `name` | (默认返回) |
| `desc` | (默认返回) |
| `create_time` | (默认返回) |
| `update_time` | (默认返回) |

---

## 指数

共 7 个工具

### ci_daily
**分类**: 指数 > 中信行业指数日行情-获取中信行业指数日线行情

**说明**: /数据接口/指数/中信行业指数日行情-获取中信行业指数日线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, low, high, close, pre_close, change, pct_change, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 行业代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `high` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### index_dailybasic
**分类**: 指数 > 大盘指数每日指标-目前只提供上证综指，深证成指，上证50，中证500，中小板指，创业板指的每日指标数据

**说明**: /数据接口/指数/大盘指数每日指标-目前只提供上证综指，深证成指，上证50，中证500，中小板指，创业板指的每日指标数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, total_mv, float_mv, total_share, float_share, free_share, turnover_rate, turnover_rate_f, pe, pe_ttm, pb 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （格式：YYYYMMDD，比如20181018，下同） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `total_mv` | (默认返回) |
| `float_mv` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `free_share` | (默认返回) |
| `turnover_rate` | (默认返回) |
| `turnover_rate_f` | (默认返回) |
| `pe` | (默认返回) |
| `pe_ttm` | (默认返回) |
| `pb` | (默认返回) |

---

### index_basic
**分类**: 指数 > 指数基本信息-获取指数基础信息。

**说明**: /数据接口/指数/指数基本信息-获取指数基础信息。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `category` | string | 否 | 指数类别 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, fullname, market, publisher, index_type, category, base_date, base_point, list_date, weight_rule, desc, exp_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `market` | string | 否 | 交易所或服务商(默认SSE) |
| `name` | string | 否 | 指数简称 |
| `publisher` | string | 否 | 发布商 |
| `ts_code` | string | 否 | 指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `fullname` | (默认返回) |
| `market` | (默认返回) |
| `publisher` | (默认返回) |
| `index_type` | (默认返回) |
| `category` | (默认返回) |
| `base_date` | (默认返回) |
| `base_point` | (默认返回) |
| `list_date` | (默认返回) |
| `weight_rule` | (默认返回) |
| `desc` | (默认返回) |
| `exp_date` | (默认返回) |

---

### idx_factor_pro
**分类**: 指数 > 指数技术面因子(专业版)-获取指数每日技术面因子数据，用于跟踪指数当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估，指数包括大盘指数 申万行业指数 中信指数

**说明**: /数据接口/指数/指数技术面因子(专业版)-获取指数每日技术面因子数据，用于跟踪指数当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估，指数包括大盘指数 申万行业指数 中信指数

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, high, low, close, pre_close, change, pct_change, vol, amount, asi_bfq, asit_bfq, atr_bfq, bbi_bfq, bias1_bfq, bias2_bfq, bias3_bfq, boll_lower_bfq, boll_mid_bfq, boll_upper_bfq, brar_ar_bfq, brar_br_... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 指数代码(大盘指数 申万指数 中信指数) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `asi_bfq` | (默认返回) |
| `asit_bfq` | (默认返回) |
| `atr_bfq` | (默认返回) |
| `bbi_bfq` | (默认返回) |
| `bias1_bfq` | (默认返回) |
| `bias2_bfq` | (默认返回) |
| `bias3_bfq` | (默认返回) |
| `boll_lower_bfq` | (默认返回) |
| `boll_mid_bfq` | (默认返回) |
| `boll_upper_bfq` | (默认返回) |
| `brar_ar_bfq` | (默认返回) |
| `brar_br_bfq` | (默认返回) |
| `cci_bfq` | (默认返回) |
| `cr_bfq` | (默认返回) |
| `dfma_dif_bfq` | (默认返回) |
| `dfma_difma_bfq` | (默认返回) |
| `dmi_adx_bfq` | (默认返回) |
| `dmi_adxr_bfq` | (默认返回) |
| `dmi_mdi_bfq` | (默认返回) |
| `dmi_pdi_bfq` | (默认返回) |
| `downdays` | (默认返回) |
| `updays` | (默认返回) |
| `dpo_bfq` | (默认返回) |
| `madpo_bfq` | (默认返回) |
| `ema_bfq_10` | (默认返回) |
| `ema_bfq_20` | (默认返回) |
| `ema_bfq_250` | (默认返回) |
| `ema_bfq_30` | (默认返回) |
| `ema_bfq_5` | (默认返回) |
| `ema_bfq_60` | (默认返回) |
| `ema_bfq_90` | (默认返回) |
| `emv_bfq` | (默认返回) |
| `maemv_bfq` | (默认返回) |
| `expma_12_bfq` | (默认返回) |
| `expma_50_bfq` | (默认返回) |
| `kdj_bfq` | (默认返回) |
| `kdj_d_bfq` | (默认返回) |
| `kdj_k_bfq` | (默认返回) |
| `ktn_down_bfq` | (默认返回) |
| `ktn_mid_bfq` | (默认返回) |
| `ktn_upper_bfq` | (默认返回) |
| `lowdays` | (默认返回) |
| `topdays` | (默认返回) |
| `ma_bfq_10` | (默认返回) |
| `ma_bfq_20` | (默认返回) |
| `ma_bfq_250` | (默认返回) |
| `ma_bfq_30` | (默认返回) |
| `ma_bfq_5` | (默认返回) |
| `ma_bfq_60` | (默认返回) |
| `ma_bfq_90` | (默认返回) |
| `macd_bfq` | (默认返回) |
| `macd_dea_bfq` | (默认返回) |
| `macd_dif_bfq` | (默认返回) |
| `mass_bfq` | (默认返回) |
| `ma_mass_bfq` | (默认返回) |
| `mfi_bfq` | (默认返回) |
| `mtm_bfq` | (默认返回) |
| `mtmma_bfq` | (默认返回) |
| `obv_bfq` | (默认返回) |
| `psy_bfq` | (默认返回) |
| `psyma_bfq` | (默认返回) |
| `roc_bfq` | (默认返回) |
| `maroc_bfq` | (默认返回) |
| `rsi_bfq_12` | (默认返回) |
| `rsi_bfq_24` | (默认返回) |
| `rsi_bfq_6` | (默认返回) |
| `taq_down_bfq` | (默认返回) |
| `taq_mid_bfq` | (默认返回) |
| `taq_up_bfq` | (默认返回) |
| `trix_bfq` | (默认返回) |
| `trma_bfq` | (默认返回) |
| `vr_bfq` | (默认返回) |
| `wr_bfq` | (默认返回) |
| `wr1_bfq` | (默认返回) |
| `xsii_td1_bfq` | (默认返回) |
| `xsii_td2_bfq` | (默认返回) |
| `xsii_td3_bfq` | (默认返回) |
| `xsii_td4_bfq` | (默认返回) |

---

### index_monthly
**分类**: 指数 > 指数月线行情-获取指数月线行情,每月更新一次

**说明**: /数据接口/指数/指数月线行情-获取指数月线行情,每月更新一次

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_chg 额外可选字段:   vol:    amount:  |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |

---

### index_classify
**分类**: 指数 > 申万行业分类-获取申万行业分类，可以获取申万2014年版本（28个一级分类，104个二级分类，227个三级分类）和2021年本版（31个一级分类，134个二级分类，346个三级分类）列表信息

**说明**: /数据接口/指数/申万行业分类-获取申万行业分类，可以获取申万2014年版本（28个一级分类，104个二级分类，227个三级分类）和2021年本版（31个一级分类，134个二级分类，346个三级分类）列表信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: index_code, industry_name, parent_code, level, industry_code, is_pub 额外可选字段:   src: 行业分类（SW申万） |
| `index_code` | string | 否 | 指数代码 |
| `level` | string | 否 | 行业分级（L1/L2/L3） |
| `parent_code` | string | 否 | 父级代码（一级为0） |
| `src` | string | 否 | 指数来源（SW2014：申万2014年版本，SW2021：申万2021年版本） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `index_code` | (默认返回) |
| `industry_name` | (默认返回) |
| `parent_code` | (默认返回) |
| `level` | (默认返回) |
| `industry_code` | (默认返回) |
| `is_pub` | (默认返回) |
| `src` | 行业分类（SW申万） |

---

### index_member
**分类**: 指数 > 申万行业成分-申万行业成分

**说明**: /数据接口/指数/申万行业成分-申万行业成分

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: index_code, con_code, in_date, out_date, is_new 额外可选字段:   con_name: 成分股票名称   index_name: 指数名称 |
| `index_code` | string | 否 | 指数代码 |
| `is_new` | string | 否 | 是否最新 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `index_code` | (默认返回) |
| `con_code` | (默认返回) |
| `in_date` | (默认返回) |
| `out_date` | (默认返回) |
| `is_new` | (默认返回) |
| `con_name` | 成分股票名称 |
| `index_name` | 指数名称 |

---

## 指数专题

共 13 个工具

### ci_index_member
**分类**: 指数专题 > 中信行业成分-按三级分类提取中信行业成分，可提供某个分类的所有成分，也可按股票代码提取所属分类，参数灵活

**说明**: /数据接口/指数专题/中信行业成分-按三级分类提取中信行业成分，可提供某个分类的所有成分，也可按股票代码提取所属分类，参数灵活

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: l1_code, l1_name, l2_code, l2_name, l3_code, l3_name, ts_code, name, in_date, out_date, is_new 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_new` | string | 否 | 是否最新（默认为“Y是”） |
| `l1_code` | string | 否 | 一级行业代码 |
| `l2_code` | string | 否 | 二级行业代码 |
| `l3_code` | string | 否 | 三级行业代码 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `l1_code` | (默认返回) |
| `l1_name` | (默认返回) |
| `l2_code` | (默认返回) |
| `l2_name` | (默认返回) |
| `l3_code` | (默认返回) |
| `l3_name` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `in_date` | (默认返回) |
| `out_date` | (默认返回) |
| `is_new` | (默认返回) |

---

### index_global
**分类**: 指数专题 > 国际主要指数-获取国际主要指数日线行情

**说明**: /数据接口/指数专题/国际主要指数-获取国际主要指数日线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, close, high, low, pre_close, change, pct_chg, swing, vol 额外可选字段:   amount: 成交额 （大部分无此项数据） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期，YYYYMMDD格式，下同 |
| `ts_code` | string | 否 | TS指数代码，见下表 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `swing` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | 成交额 （大部分无此项数据） |

---

### rt_idx_k
**分类**: 指数专题 > 实时日线-获取交易所指数实时日线行情，支持按代码或代码通配符一次性提取全部交易所指数实时日k线行情

**说明**: /数据接口/指数专题/实时日线-获取交易所指数实时日线行情，支持按代码或代码通配符一次性提取全部交易所指数实时日k线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_time, close, pre_close, high, open, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | 指数代码，支持通配符方式，e.g. 0\*.SH、3\*.SZ、000001.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_time` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### idx_mins
**分类**: 指数专题 > 指数历史分钟-获取交易所指数分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK和 http Restful API两种方式

**说明**: /数据接口/指数专题/指数历史分钟-获取交易所指数分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 格式：2023-08-25 19:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1min/5min/15min/30min/60min） |
| `start_date` | string | 否 | 开始日期 格式：2023-08-25 09:00:00 |
| `ts_code` | string | 是 | 指数代码，e.g. 000001.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### index_weekly
**分类**: 指数专题 > 指数周线行情-获取指数周线行情

**说明**: /数据接口/指数专题/指数周线行情-获取指数周线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### rt_idx_min
**分类**: 指数专题 > 指数实时分钟-获取交易所指数实时分钟数据，包括1~60min

**说明**: /数据接口/指数专题/指数实时分钟-获取交易所指数实时分钟数据，包括1~60min

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 1MIN,5MIN,15MIN,30MIN,60MIN （大写） |
| `ts_code` | string | 是 | 支持单个和多个：000001.SH 或者 000001.SH,399300.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### index_weight
**分类**: 指数专题 > 指数成分和权重-获取各类指数成分和权重，**月度数据** ，建议输入参数里开始日期和结束日分别输入当月第一天和最后一天的日期。

**说明**: /数据接口/指数专题/指数成分和权重-获取各类指数成分和权重，**月度数据** ，建议输入参数里开始日期和结束日分别输入当月第一天和最后一天的日期。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: index_code, con_code, trade_date, weight 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `index_code` | string | 是 | 指数代码，来源指数基础信息接口 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式YYYYMMDD，下同） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `index_code` | (默认返回) |
| `con_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `weight` | (默认返回) |

---

### index_daily
**分类**: 指数专题 > 指数日线行情-获取指数每日行情，还可以通过bar接口获取。由于服务器压力，目前规则是单次调取最多取8000行记录，可以设置start和end日期补全。指数行情也可以通过[**通用行情接口**]( https: > tushare.pro > document > 2?doc_id=109)获取数据．

**说明**: /数据接口/指数专题/指数日线行情-获取指数每日行情，还可以通过bar接口获取。由于服务器压力，目前规则是单次调取最多取8000行记录，可以设置start和end日期补全。指数行情也可以通过[**通用行情接口**]( https://tushare.pro/document/2?doc_id=109)获取数据．

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 （日期格式：YYYYMMDD，下同） |
| `ts_code` | string | 是 | 指数代码，来源指数基础信息接口 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### daily_info
**分类**: 指数专题 > 沪深市场每日交易统计-获取交易所股票交易统计，包括各板块明细

**说明**: /数据接口/指数专题/沪深市场每日交易统计-获取交易所股票交易统计，包括各板块明细

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 股票市场（SH上交所 SZ深交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, ts_name, com_count, total_share, float_share, total_mv, float_mv, amount, vol, trans_count, pe, tr, exchange 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 板块代码（请参阅下方列表） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `ts_name` | (默认返回) |
| `com_count` | (默认返回) |
| `total_share` | (默认返回) |
| `float_share` | (默认返回) |
| `total_mv` | (默认返回) |
| `float_mv` | (默认返回) |
| `amount` | (默认返回) |
| `vol` | (默认返回) |
| `trans_count` | (默认返回) |
| `pe` | (默认返回) |
| `tr` | (默认返回) |
| `exchange` | (默认返回) |

---

### sz_daily_info
**分类**: 指数专题 > 深圳市场每日交易情况-获取深圳市场每日交易概况

**说明**: /数据接口/指数专题/深圳市场每日交易情况-获取深圳市场每日交易概况

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, count, amount, vol, total_share, total_mv, float_share, float_mv 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 板块代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `count` | (默认返回) |
| `amount` | (默认返回) |
| `vol` | (默认返回) |
| `total_share` | (默认返回) |
| `total_mv` | (默认返回) |
| `float_share` | (默认返回) |
| `float_mv` | (默认返回) |

---

### rt_sw_k
**分类**: 指数专题 > 申万实时行情-获取申万行业指数的最新截面数据

**说明**: /数据接口/指数专题/申万实时行情-获取申万行业指数的最新截面数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_time, close, pre_close, high, open, low, vol, amount, pct_change 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | 指数代码，如: 801005.SI；可以是逗号隔开的多个，如: 801005.SI,801001.SI |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_time` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `pct_change` | (默认返回) |

---

### index_member_all
**分类**: 指数专题 > 申万行业成分（分级）-按三级分类提取申万行业成分，可提供某个分类的所有成分，也可按股票代码提取所属分类，参数灵活

**说明**: /数据接口/指数专题/申万行业成分（分级）-按三级分类提取申万行业成分，可提供某个分类的所有成分，也可按股票代码提取所属分类，参数灵活

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: l1_code, l1_name, l2_code, l2_name, l3_code, l3_name, ts_code, name, in_date, out_date, is_new 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_new` | string | 否 | 是否最新（默认为“Y是”） |
| `l1_code` | string | 否 | 一级行业代码 |
| `l2_code` | string | 否 | 二级行业代码 |
| `l3_code` | string | 否 | 三级行业代码 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `l1_code` | (默认返回) |
| `l1_name` | (默认返回) |
| `l2_code` | (默认返回) |
| `l2_name` | (默认返回) |
| `l3_code` | (默认返回) |
| `l3_name` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `in_date` | (默认返回) |
| `out_date` | (默认返回) |
| `is_new` | (默认返回) |

---

### sw_daily
**分类**: 指数专题 > 申万行业指数日行情-获取申万行业日线行情（默认是申万2021版行情）

**说明**: /数据接口/指数专题/申万行业指数日行情-获取申万行业日线行情（默认是申万2021版行情）

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, name, open, low, high, close, change, pct_change, vol, amount, pe, pb, float_mv, total_mv 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 行业代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `name` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `high` | (默认返回) |
| `close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `pe` | (默认返回) |
| `pb` | (默认返回) |
| `float_mv` | (默认返回) |
| `total_mv` | (默认返回) |

---

## ETF专题

共 9 个工具

### mkt_idx_bmk
**分类**: ETF专题 > ETF业绩比较基准-获取ETF业绩比较基准列表信息

**说明**: /数据接口/ETF专题/ETF业绩比较基准-获取ETF业绩比较基准列表信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `BMK_TYPE` | string | 否 | 基准类型：策略指数；行业主题指数；行业主题指数；宽基指数。 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, symbol, name, fullname, bmk_level, bmk_type, bmk_src, idx_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | 指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `symbol` | (默认返回) |
| `name` | (默认返回) |
| `fullname` | (默认返回) |
| `bmk_level` | (默认返回) |
| `bmk_type` | (默认返回) |
| `bmk_src` | (默认返回) |
| `idx_type` | (默认返回) |

---

### etf_share_size
**分类**: ETF专题 > ETF份额规模-获取沪深ETF每日份额和规模数据，能体现规模份额的变化，掌握ETF资金动向，同时提供每日净值和收盘价；数据指标是分批入库，建议在每日19点后提取；另外，涉及海外的ETF数据更新会晚一些属于正常情况。

**说明**: /数据接口/ETF专题/ETF份额规模-获取沪深ETF每日份额和规模数据，能体现规模份额的变化，掌握ETF资金动向，同时提供每日净值和收盘价；数据指标是分批入库，建议在每日19点后提取；另外，涉及海外的ETF数据更新会晚一些属于正常情况。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所（SSE上交所 SZSE深交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, etf_name, total_share, total_size, exchange 额外可选字段:   nav: 基金份额净值(元)   close: 收盘价（元） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 基金代码 （可从ETF基础信息接口提取） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `etf_name` | (默认返回) |
| `total_share` | (默认返回) |
| `total_size` | (默认返回) |
| `exchange` | (默认返回) |
| `nav` | 基金份额净值(元) |
| `close` | 收盘价（元） |

---

### etf_index
**分类**: ETF专题 > ETF基准指数-获取ETF基准指数列表信息

**说明**: /数据接口/ETF专题/ETF基准指数-获取ETF基准指数列表信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `base_date` | string | 否 | 指数基期（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, indx_name, indx_csname, pub_party_name, pub_date, base_date, bp, adj_circle 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `pub_date` | string | 否 | 发布日期（格式：YYYYMMDD） |
| `ts_code` | string | 否 | 指数代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `indx_name` | (默认返回) |
| `indx_csname` | (默认返回) |
| `pub_party_name` | (默认返回) |
| `pub_date` | (默认返回) |
| `base_date` | (默认返回) |
| `bp` | (默认返回) |
| `adj_circle` | (默认返回) |

---

### etf_basic
**分类**: ETF专题 > ETF基本信息-获取国内ETF基础信息，包括了QDII。数据来源与沪深交易所公开披露信息。

**说明**: /数据接口/ETF专题/ETF基本信息-获取国内ETF基础信息，包括了QDII。数据来源与沪深交易所公开披露信息。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 否 | 交易所（SH上交所 SZ深交所） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, csname, extname, cname, index_code, index_name, setup_date, list_date, list_status, exchange, mgr_name, custod_name, mgt_fee, etf_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `index_code` | string | 否 | 跟踪指数代码 |
| `list_date` | string | 否 | 上市日期（格式：YYYYMMDD） |
| `list_status` | string | 否 | 上市状态（L上市 D退市 P待上市） |
| `mgr` | string | 否 | 管理人（简称，e.g.华夏基金) |
| `ts_code` | string | 否 | ETF代码（带.SZ/.SH后缀的6位数字，如：159526.SZ） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `csname` | (默认返回) |
| `extname` | (默认返回) |
| `cname` | (默认返回) |
| `index_code` | (默认返回) |
| `index_name` | (默认返回) |
| `setup_date` | (默认返回) |
| `list_date` | (默认返回) |
| `list_status` | (默认返回) |
| `exchange` | (默认返回) |
| `mgr_name` | (默认返回) |
| `custod_name` | (默认返回) |
| `mgt_fee` | (默认返回) |
| `etf_type` | (默认返回) |

---

### fund_adj
**分类**: ETF专题 > ETF复权因子-获取基金复权因子，用于计算基金复权行情

**说明**: /数据接口/ETF专题/ETF复权因子-获取基金复权因子，用于计算基金复权行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, adj_factor 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `limit` | string | 否 | 最大行数 |
| `offset` | string | 否 | 开始行数 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：yyyymmdd，下同） |
| `ts_code` | string | 否 | TS基金代码（支持多只基金输入） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `adj_factor` | (默认返回) |

---

### rt_etf_k
**分类**: ETF专题 > ETF实时日线-获取ETF实时日k线行情，支持按ETF代码或代码通配符一次性提取全部ETF实时日k线行情

**说明**: /数据接口/ETF专题/ETF实时日线-获取ETF实时日k线行情，支持按ETF代码或代码通配符一次性提取全部ETF实时日k线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, pre_close, high, open, low, close, vol, amount, num 额外可选字段:   trade_time: 交易时间   ask_volume1: 委托卖盘（股）   bid_volume1: 委托买盘（股） |
| `topic` | string | 是 | 分类参数，取上海ETF时，需要输入'HQ_FND_TICK'，参考下面例子 |
| `ts_code` | string | 是 | 支持通配符方式，e.g. 5\*.SH、15\*.SZ、159101.SZ |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `pre_close` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `num` | (默认返回) |
| `trade_time` | 交易时间 |
| `ask_volume1` | 委托卖盘（股） |
| `bid_volume1` | 委托买盘（股） |

---

### fund_daily
**分类**: ETF专题 > ETF日线行情-获取ETF行情每日收盘后成交数据，历史超过10年

**说明**: /数据接口/ETF专题/ETF日线行情-获取ETF行情每日收盘后成交数据，历史超过10年

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 基金代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### idx_anns
**分类**: ETF专题 > 指数公告-获取指数公司披露的相关公告信息，包括中证指数、国证指数、恒生指数和华证指数的及时与历史公告信息，跟踪指数最新信息和发展方向。

**说明**: /数据接口/ETF专题/指数公告-获取指数公司披露的相关公告信息，包括中证指数、国证指数、恒生指数和华证指数的及时与历史公告信息，跟踪指数最新信息和发展方向。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（YYYYMMDD格式，下同） |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ann_date, title, url, source, type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `src` | string | 否 | 信息来源（中证指数、国证指数、恒生指数、华证指数） |
| `start_date` | string | 否 | 公告开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ann_date` | (默认返回) |
| `title` | (默认返回) |
| `url` | (默认返回) |
| `source` | (默认返回) |
| `type` | (默认返回) |

---

### rt_etf_sz_iopv
**分类**: ETF专题 > 深交所ETF实时快照-ETF实时净值和申购赎回数据参考，目前只提供深市

**说明**: /数据接口/ETF专题/深交所ETF实时快照-ETF实时净值和申购赎回数据参考，目前只提供深市

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_time, ts_code, vol, num, amount, price, iopv, pre_iopv, buy_num, buy_vol, sell_num, sell_vol 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | ETF代码（默认为空，即一次全市场。支持单个和多个ETF过滤提取） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_time` | (默认返回) |
| `ts_code` | (默认返回) |
| `vol` | (默认返回) |
| `num` | (默认返回) |
| `amount` | (默认返回) |
| `price` | (默认返回) |
| `iopv` | (默认返回) |
| `pre_iopv` | (默认返回) |
| `buy_num` | (默认返回) |
| `buy_vol` | (默认返回) |
| `sell_num` | (默认返回) |
| `sell_vol` | (默认返回) |

---

## 公募基金

共 8 个工具

### fund_nav
**分类**: 公募基金 > 基金净值-获取公募基金净值数据

**说明**: /数据接口/公募基金/基金净值-获取公募基金净值数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 净值结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, nav_date, unit_nav, accum_nav, accum_div, net_asset, total_netasset, adj_nav 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `market` | string | 否 | E场内 O场外 |
| `nav_date` | string | 否 | 净值日期 （二选一） |
| `start_date` | string | 否 | 净值开始日期 |
| `ts_code` | string | 否 | TS基金代码 （二选一） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `nav_date` | (默认返回) |
| `unit_nav` | (默认返回) |
| `accum_nav` | (默认返回) |
| `accum_div` | (默认返回) |
| `net_asset` | (默认返回) |
| `total_netasset` | (默认返回) |
| `adj_nav` | (默认返回) |

---

### fund_div
**分类**: 公募基金 > 基金分红-获取公募基金分红数据

**说明**: /数据接口/公募基金/基金分红-获取公募基金分红数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日（以下参数四选一） |
| `ex_date` | string | 否 | 除息日 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, imp_anndate, base_date, div_proc, record_date, ex_date, pay_date, earpay_date, net_ex_date, div_cash, base_unit, ear_distr, ear_amount, account_date, base_year 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `pay_date` | string | 否 | 派息日 |
| `ts_code` | string | 否 | 基金代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `imp_anndate` | (默认返回) |
| `base_date` | (默认返回) |
| `div_proc` | (默认返回) |
| `record_date` | (默认返回) |
| `ex_date` | (默认返回) |
| `pay_date` | (默认返回) |
| `earpay_date` | (默认返回) |
| `net_ex_date` | (默认返回) |
| `div_cash` | (默认返回) |
| `base_unit` | (默认返回) |
| `ear_distr` | (默认返回) |
| `ear_amount` | (默认返回) |
| `account_date` | (默认返回) |
| `base_year` | (默认返回) |

---

### fund_basic
**分类**: 公募基金 > 基金列表-获取公募基金数据列表，包括场内和场外基金

**说明**: /数据接口/公募基金/基金列表-获取公募基金数据列表，包括场内和场外基金

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, management, custodian, fund_type, found_date, due_date, list_date, issue_date, delist_date, issue_amount, m_fee, c_fee, duration_year, p_value, min_amount, exp_return, benchmark, status, invest_type, type, trust... |
| `market` | string | 否 | 交易市场: E场内 O场外（默认E） |
| `status` | string | 否 | 存续状态 D摘牌 I发行 L上市中 |
| `ts_code` | string | 否 | 基金代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `management` | (默认返回) |
| `custodian` | (默认返回) |
| `fund_type` | (默认返回) |
| `found_date` | (默认返回) |
| `due_date` | (默认返回) |
| `list_date` | (默认返回) |
| `issue_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `issue_amount` | (默认返回) |
| `m_fee` | (默认返回) |
| `c_fee` | (默认返回) |
| `duration_year` | (默认返回) |
| `p_value` | (默认返回) |
| `min_amount` | (默认返回) |
| `exp_return` | (默认返回) |
| `benchmark` | (默认返回) |
| `status` | (默认返回) |
| `invest_type` | (默认返回) |
| `type` | (默认返回) |
| `trustee` | (默认返回) |
| `purc_startdate` | (默认返回) |
| `redm_startdate` | (默认返回) |
| `market` | (默认返回) |

---

### fund_factor_pro
**分类**: 公募基金 > 基金技术面因子(专业版)-获取场内基金每日技术面因子数据，用于跟踪场内基金当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

**说明**: /数据接口/公募基金/基金技术面因子(专业版)-获取场内基金每日技术面因子数据，用于跟踪场内基金当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, trade_date_doris, open, high, low, close, pre_close, change, pct_change, vol, amount, asi_bfq, asit_bfq, atr_bfq, bbi_bfq, bias1_bfq, bias2_bfq, bias3_bfq, boll_lower_bfq, boll_mid_bfq, boll_upper_bfq, bra... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 基金代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `trade_date_doris` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `asi_bfq` | (默认返回) |
| `asit_bfq` | (默认返回) |
| `atr_bfq` | (默认返回) |
| `bbi_bfq` | (默认返回) |
| `bias1_bfq` | (默认返回) |
| `bias2_bfq` | (默认返回) |
| `bias3_bfq` | (默认返回) |
| `boll_lower_bfq` | (默认返回) |
| `boll_mid_bfq` | (默认返回) |
| `boll_upper_bfq` | (默认返回) |
| `brar_ar_bfq` | (默认返回) |
| `brar_br_bfq` | (默认返回) |
| `cci_bfq` | (默认返回) |
| `cr_bfq` | (默认返回) |
| `dfma_dif_bfq` | (默认返回) |
| `dfma_difma_bfq` | (默认返回) |
| `dmi_adx_bfq` | (默认返回) |
| `dmi_adxr_bfq` | (默认返回) |
| `dmi_mdi_bfq` | (默认返回) |
| `dmi_pdi_bfq` | (默认返回) |
| `downdays` | (默认返回) |
| `updays` | (默认返回) |
| `dpo_bfq` | (默认返回) |
| `madpo_bfq` | (默认返回) |
| `ema_bfq_10` | (默认返回) |
| `ema_bfq_20` | (默认返回) |
| `ema_bfq_250` | (默认返回) |
| `ema_bfq_30` | (默认返回) |
| `ema_bfq_5` | (默认返回) |
| `ema_bfq_60` | (默认返回) |
| `ema_bfq_90` | (默认返回) |
| `emv_bfq` | (默认返回) |
| `maemv_bfq` | (默认返回) |
| `expma_12_bfq` | (默认返回) |
| `expma_50_bfq` | (默认返回) |
| `kdj_bfq` | (默认返回) |
| `kdj_d_bfq` | (默认返回) |
| `kdj_k_bfq` | (默认返回) |
| `ktn_down_bfq` | (默认返回) |
| `ktn_mid_bfq` | (默认返回) |
| `ktn_upper_bfq` | (默认返回) |
| `lowdays` | (默认返回) |
| `topdays` | (默认返回) |
| `ma_bfq_10` | (默认返回) |
| `ma_bfq_20` | (默认返回) |
| `ma_bfq_250` | (默认返回) |
| `ma_bfq_30` | (默认返回) |
| `ma_bfq_5` | (默认返回) |
| `ma_bfq_60` | (默认返回) |
| `ma_bfq_90` | (默认返回) |
| `macd_bfq` | (默认返回) |
| `macd_dea_bfq` | (默认返回) |
| `macd_dif_bfq` | (默认返回) |
| `mass_bfq` | (默认返回) |
| `ma_mass_bfq` | (默认返回) |
| `mfi_bfq` | (默认返回) |
| `mtm_bfq` | (默认返回) |
| `mtmma_bfq` | (默认返回) |
| `obv_bfq` | (默认返回) |
| `psy_bfq` | (默认返回) |
| `psyma_bfq` | (默认返回) |
| `roc_bfq` | (默认返回) |
| `maroc_bfq` | (默认返回) |
| `rsi_bfq_12` | (默认返回) |
| `rsi_bfq_24` | (默认返回) |
| `rsi_bfq_6` | (默认返回) |
| `taq_down_bfq` | (默认返回) |
| `taq_mid_bfq` | (默认返回) |
| `taq_up_bfq` | (默认返回) |
| `trix_bfq` | (默认返回) |
| `trma_bfq` | (默认返回) |
| `vr_bfq` | (默认返回) |
| `wr_bfq` | (默认返回) |
| `wr1_bfq` | (默认返回) |
| `xsii_td1_bfq` | (默认返回) |
| `xsii_td2_bfq` | (默认返回) |
| `xsii_td3_bfq` | (默认返回) |
| `xsii_td4_bfq` | (默认返回) |

---

### fund_portfolio
**分类**: 公募基金 > 基金持仓-获取公募基金持仓数据，季度更新

**说明**: /数据接口/公募基金/基金持仓-获取公募基金持仓数据，季度更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（YYYYMMDD格式） |
| `end_date` | string | 否 | 报告期结束日期（YYYYMMDD格式） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, end_date, symbol, mkv, amount, stk_mkv_ratio, stk_float_ratio 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 季度（每个季度最后一天的日期，比如20131231表示2013年年报） |
| `start_date` | string | 否 | 报告期开始日期（YYYYMMDD格式） |
| `symbol` | string | 否 | 股票代码 |
| `ts_code` | string | 否 | 基金代码 (ts_code,ann_date,period至少输入一个参数) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `end_date` | (默认返回) |
| `symbol` | (默认返回) |
| `mkv` | (默认返回) |
| `amount` | (默认返回) |
| `stk_mkv_ratio` | (默认返回) |
| `stk_float_ratio` | (默认返回) |

---

### fund_company
**分类**: 公募基金 > 基金管理人-获取公募基金管理人列表

**说明**: /数据接口/公募基金/基金管理人-获取公募基金管理人列表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: name, shortname, province, city, address, phone, office, website, chairman, manager, reg_capital, setup_date, end_date, employees, main_business, org_code, credit_code 额外可选字段:   short_enname: 英文缩写 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `name` | (默认返回) |
| `shortname` | (默认返回) |
| `province` | (默认返回) |
| `city` | (默认返回) |
| `address` | (默认返回) |
| `phone` | (默认返回) |
| `office` | (默认返回) |
| `website` | (默认返回) |
| `chairman` | (默认返回) |
| `manager` | (默认返回) |
| `reg_capital` | (默认返回) |
| `setup_date` | (默认返回) |
| `end_date` | (默认返回) |
| `employees` | (默认返回) |
| `main_business` | (默认返回) |
| `org_code` | (默认返回) |
| `credit_code` | (默认返回) |
| `short_enname` | 英文缩写 |

---

### fund_manager
**分类**: 公募基金 > 基金经理-获取公募基金经理数据，包括基金经理简历等数据

**说明**: /数据接口/公募基金/基金经理-获取公募基金经理数据，包括基金经理简历等数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期，格式：YYYYMMDD |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, name, gender, birth_year, edu, nationality, begin_date, end_date, resume 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `limit` | integer | 否 | 每页行数 |
| `name` | string | 否 | 基金经理姓名 |
| `offset` | string | 否 | 开始行数 |
| `ts_code` | string | 否 | 基金代码，支持多只基金，逗号分隔 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `name` | (默认返回) |
| `gender` | (默认返回) |
| `birth_year` | (默认返回) |
| `edu` | (默认返回) |
| `nationality` | (默认返回) |
| `begin_date` | (默认返回) |
| `end_date` | (默认返回) |
| `resume` | (默认返回) |

---

### fund_share
**分类**: 公募基金 > 基金规模-获取基金规模数据，包含上海和深圳ETF基金

**说明**: /数据接口/公募基金/基金规模-获取基金规模数据，包含上海和深圳ETF基金

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, fd_share 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `market` | string | 否 | 市场代码（SH上交所 ，SZ深交所） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS基金代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `fd_share` | (默认返回) |

---

## 期货

共 5 个工具

### fut_wsr
**分类**: 期货 > 仓单日报-获取仓单日报数据，了解各仓库 > 厂库的仓单变化

**说明**: /数据接口/期货/仓单日报-获取仓单日报数据，了解各仓库/厂库的仓单变化

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所代码 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, symbol, fut_name, warehouse, pre_vol, vol, vol_chg, unit 额外可选字段:   pd: 升贴水   area: 地区   year: 年度   brand: 品牌   grade: 等级   is_ct: 是否折算仓单   place: 产地   wh_id: 仓库编号   exchange: 交易所 |
| `start_date` | string | 否 | 开始日期(YYYYMMDD格式，下同) |
| `symbol` | string | 否 | 产品代码 |
| `trade_date` | string | 否 | 交易日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `symbol` | (默认返回) |
| `fut_name` | (默认返回) |
| `warehouse` | (默认返回) |
| `pre_vol` | (默认返回) |
| `vol` | (默认返回) |
| `vol_chg` | (默认返回) |
| `unit` | (默认返回) |
| `pd` | 升贴水 |
| `area` | 地区 |
| `year` | 年度 |
| `brand` | 品牌 |
| `grade` | 等级 |
| `is_ct` | 是否折算仓单 |
| `place` | 产地 |
| `wh_id` | 仓库编号 |
| `exchange` | 交易所 |

---

### fut_daily
**分类**: 期货 > 日线行情-期货日线行情数据

**说明**: /数据接口/期货/日线行情-期货日线行情数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所代码 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, pre_close, pre_settle, open, high, low, close, settle, change1, change2, vol, amount, oi, oi_chg 额外可选字段:   delv_settle: 交割结算价 |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 合约代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `pre_close` | (默认返回) |
| `pre_settle` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `settle` | (默认返回) |
| `change1` | (默认返回) |
| `change2` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |
| `oi_chg` | (默认返回) |
| `delv_settle` | 交割结算价 |

---

### fut_mapping
**分类**: 期货 > 期货主力与连续合约-获取期货主力（或连续）合约与月合约映射数据

**说明**: /数据接口/期货/期货主力与连续合约-获取期货主力（或连续）合约与月合约映射数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, mapping_ts_code 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | 合约代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `mapping_ts_code` | (默认返回) |

---

### fut_weekly_detail
**分类**: 期货 > 期货主要品种交易周报-获取期货交易所主要品种每周交易统计信息，数据从2010年3月开始

**说明**: /数据接口/期货/期货主要品种交易周报-获取期货交易所主要品种每周交易统计信息，数据从2010年3月开始

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_week` | string | 否 | 结束周期 |
| `exchange` | string | 否 | 交易所（请参考[交易所说明]( https://tushare.pro/document/2?doc_id=134)） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: exchange, prd, name, vol, vol_yoy, amount, amout_yoy, cumvol, cumvol_yoy, cumamt, cumamt_yoy, open_interest, interest_wow, mc_close, close_wow, week, week_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `prd` | string | 否 | 期货品种（支持多品种输入，逗号分隔） |
| `start_week` | string | 否 | 开始周期 |
| `week` | string | 否 | 周期（每年第几周，e.g. 202001 表示2020第1周） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `exchange` | (默认返回) |
| `prd` | (默认返回) |
| `name` | (默认返回) |
| `vol` | (默认返回) |
| `vol_yoy` | (默认返回) |
| `amount` | (默认返回) |
| `amout_yoy` | (默认返回) |
| `cumvol` | (默认返回) |
| `cumvol_yoy` | (默认返回) |
| `cumamt` | (默认返回) |
| `cumamt_yoy` | (默认返回) |
| `open_interest` | (默认返回) |
| `interest_wow` | (默认返回) |
| `mc_close` | (默认返回) |
| `close_wow` | (默认返回) |
| `week` | (默认返回) |
| `week_date` | (默认返回) |

---

### fut_holding
**分类**: 期货 > 每日持仓排名-获取每日成交持仓排名数据

**说明**: /数据接口/期货/每日持仓排名-获取每日成交持仓排名数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所代码 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, symbol, broker, vol, vol_chg, long_hld, long_chg, short_hld, short_chg 额外可选字段:   exchange: 交易所 |
| `start_date` | string | 否 | 开始日期(YYYYMMDD格式，下同) |
| `symbol` | string | 否 | 合约或产品代码 |
| `trade_date` | string | 否 | 交易日期 （trade_date/symbol至少输入一个参数） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `symbol` | (默认返回) |
| `broker` | (默认返回) |
| `vol` | (默认返回) |
| `vol_chg` | (默认返回) |
| `long_hld` | (默认返回) |
| `long_chg` | (默认返回) |
| `short_hld` | (默认返回) |
| `short_chg` | (默认返回) |
| `exchange` | 交易所 |

---

## 期货数据

共 6 个工具

### ft_mins
**分类**: 期货数据 > 历史分钟行情-获取全市场期货合约分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK和 http Restful API两种方式，如果需要主力合约分钟，请先通过主力[mapping](https: > tushare.pro > document > 2?doc_id=189)接口（需要有至少2000积分）获取对应的合约代码后提取分钟。

**说明**: /数据接口/期货数据/历史分钟行情-获取全市场期货合约分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式，如果需要主力合约分钟，请先通过主力[mapping](https://tushare.pro/document/2?doc_id=189)接口（需要有至少2000积分）获取对应的合约代码后提取分钟。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 格式：2023-08-25 19:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_time, open, close, high, low, vol, amount, oi 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1min/5min/15min/30min/60min） |
| `start_date` | string | 否 | 开始日期 格式：2023-08-25 09:00:00 |
| `ts_code` | string | 是 | 股票代码，e.g.CU2310.SHF |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |

---

### fut_basic
**分类**: 期货数据 > 合约信息-获取期货合约列表数据

**说明**: /数据接口/期货数据/合约信息-获取期货合约列表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 是 | 交易所代码 CFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心 GFEX-广州期货交易所 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, symbol, exchange, name, fut_code, multiplier, trade_unit, per_unit, quote_unit, quote_unit_desc, d_mode_desc, list_date, delist_date, d_month, last_ddate 额外可选字段:   trade_time_desc: 交易时间说明 |
| `fut_code` | string | 否 | 标准合约代码，如白银AG、AP鲜苹果等 |
| `fut_type` | string | 否 | 合约类型 (1 普通合约 2主力与连续合约 默认取全部) |
| `list_date` | string | 否 | 上市开始日期(格式YYYYMMDD，从某日开始以来所有合约） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `symbol` | (默认返回) |
| `exchange` | (默认返回) |
| `name` | (默认返回) |
| `fut_code` | (默认返回) |
| `multiplier` | (默认返回) |
| `trade_unit` | (默认返回) |
| `per_unit` | (默认返回) |
| `quote_unit` | (默认返回) |
| `quote_unit_desc` | (默认返回) |
| `d_mode_desc` | (默认返回) |
| `list_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `d_month` | (默认返回) |
| `last_ddate` | (默认返回) |
| `trade_time_desc` | 交易时间说明 |

---

### rt_fut_min
**分类**: 期货数据 > 实时分钟行情-获取全市场期货合约实时分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK、 http Restful API和websocket三种方式，如果需要主力合约分钟，请先通过主力[mapping](https: > tushare.pro > document > 2?doc_id=189)接口获取对应的合约代码后提取分钟。

**说明**: /数据接口/期货数据/实时分钟行情-获取全市场期货合约实时分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK、 http Restful API和websocket三种方式，如果需要主力合约分钟，请先通过主力[mapping](https://tushare.pro/document/2?doc_id=189)接口获取对应的合约代码后提取分钟。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: code, freq, time, open, close, high, low, vol, amount, oi 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1MIN/5MIN/15MIN/30MIN/60MIN） |
| `ts_code` | string | 是 | 股票代码，e.g.CU2310.SHF，支持多个合约（逗号分隔） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `code` | (默认返回) |
| `freq` | (默认返回) |
| `time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |

---

### ft_limit
**分类**: 期货数据 > 期货合约涨跌停价格-获取所有期货合约每天的涨跌停价格及最低保证金率，数据开始于2005年。

**说明**: /数据接口/期货数据/期货合约涨跌停价格-获取所有期货合约每天的涨跌停价格及最低保证金率，数据开始于2005年。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `cont` | string | 否 | 合约代码（例如：cont='CU') |
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所代码 （例如：exchange='DCE') |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, up_limit, down_limit, m_ratio, cont, exchange 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD） |
| `ts_code` | string | 否 | 合约代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `up_limit` | (默认返回) |
| `down_limit` | (默认返回) |
| `m_ratio` | (默认返回) |
| `cont` | (默认返回) |
| `exchange` | (默认返回) |

---

### fut_weekly_monthly
**分类**: 期货数据 > 期货周 > 月线行情(每日更新)-期货周 > 月线行情(每日更新)

**说明**: /数据接口/期货数据/期货周/月线行情(每日更新)-期货周/月线行情(每日更新)

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束交易日期 |
| `exchange` | string | 否 | 交易所 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, end_date, freq, open, high, low, close, pre_close, settle, pre_settle, vol, amount, oi, oi_chg, exchange, change1, change2 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 频率week周，month月 |
| `start_date` | string | 否 | 开始交易日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `end_date` | (默认返回) |
| `freq` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `settle` | (默认返回) |
| `pre_settle` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |
| `oi_chg` | (默认返回) |
| `exchange` | (默认返回) |
| `change1` | (默认返回) |
| `change2` | (默认返回) |

---

### fut_settle
**分类**: 期货数据 > 每日结算参数-获取每日结算参数数据，包括交易和交割费率等

**说明**: /数据接口/期货数据/每日结算参数-获取每日结算参数数据，包括交易和交割费率等

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所代码 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, settle, trading_fee_rate, trading_fee, delivery_fee, b_hedging_margin_rate, s_hedging_margin_rate, long_margin_rate, short_margin_rate 额外可选字段:   exchange: 交易所   offset_today_fee: 平今仓手续率 |
| `start_date` | string | 否 | 开始日期(YYYYMMDD格式，下同) |
| `trade_date` | string | 否 | 交易日期 （trade_date/ts_code至少需要输入一个参数） |
| `ts_code` | string | 否 | 合约代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `settle` | (默认返回) |
| `trading_fee_rate` | (默认返回) |
| `trading_fee` | (默认返回) |
| `delivery_fee` | (默认返回) |
| `b_hedging_margin_rate` | (默认返回) |
| `s_hedging_margin_rate` | (默认返回) |
| `long_margin_rate` | (默认返回) |
| `short_margin_rate` | (默认返回) |
| `exchange` | 交易所 |
| `offset_today_fee` | 平今仓手续率 |

---

## 期权

共 3 个工具

### ft_tick
**分类**: 期权 > TICK数据-获取期权和期货的tick数据

**说明**: /数据接口/期权/TICK数据-获取期权和期货的tick数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: symbol, trade_time, trade_ms, price, vol, amount, ask_p1, ask_v1, bid_p1, bid_v1, oi 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始时间 |
| `symbol` | string | 是 | 期货期权代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `symbol` | (默认返回) |
| `trade_time` | (默认返回) |
| `trade_ms` | (默认返回) |
| `price` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `ask_p1` | (默认返回) |
| `ask_v1` | (默认返回) |
| `bid_p1` | (默认返回) |
| `bid_v1` | (默认返回) |
| `oi` | (默认返回) |

---

### opt_mins
**分类**: 期权 > 期权分钟行情-获取全市场期权合约分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK和 http Restful API两种方式。

**说明**: /数据接口/期权/期权分钟行情-获取全市场期权合约分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 格式：2024-08-25 19:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_time, open, close, high, low, vol, amount, oi 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1min/5min/15min/30min/60min） |
| `start_date` | string | 否 | 开始日期 格式：2024-08-25 09:00:00 |
| `ts_code` | string | 是 | 股票代码，e.g：10007976.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |

---

### opt_basic
**分类**: 期权 > 期权合约信息-获取期权合约信息

**说明**: /数据接口/期权/期权合约信息-获取期权合约信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `call_put` | string | 否 | 期权类型 |
| `exchange` | string | 否 | 交易所代码 （包括上交所SSE等[交易所](https://tushare.pro/document/2?doc_id=157)） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, exchange, name, per_unit, opt_code, opt_type, call_put, exercise_type, exercise_price, s_month, maturity_date, list_price, list_date, delist_date, last_edate, last_ddate, quote_unit, min_price_chg 额外可选字段:   （所有字段均为默认返... |
| `list_date` | string | 否 | 上市交易日 |
| `opt_code` | string | 否 | 标准合约代码，OP+期货合约TS_CODE，如棕榈油2207合约，输入OPP2207.DCE |
| `ts_code` | string | 否 | TS期权代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `exchange` | (默认返回) |
| `name` | (默认返回) |
| `per_unit` | (默认返回) |
| `opt_code` | (默认返回) |
| `opt_type` | (默认返回) |
| `call_put` | (默认返回) |
| `exercise_type` | (默认返回) |
| `exercise_price` | (默认返回) |
| `s_month` | (默认返回) |
| `maturity_date` | (默认返回) |
| `list_price` | (默认返回) |
| `list_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `last_edate` | (默认返回) |
| `last_ddate` | (默认返回) |
| `quote_unit` | (默认返回) |
| `min_price_chg` | (默认返回) |

---

## 期权数据

共 1 个工具

### opt_daily
**分类**: 期权数据 > 期权日线行情-获取期权日线行情

**说明**: /数据接口/期权数据/期权日线行情-获取期权日线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `exchange` | string | 否 | 交易所(SSE/SZSE/CFFEX/DCE/SHFE/CZCE） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, exchange, pre_settle, pre_close, open, high, low, close, settle, vol, amount, oi 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | TS合约代码（输入代码或时间至少任意一个参数） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `exchange` | (默认返回) |
| `pre_settle` | (默认返回) |
| `pre_close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `settle` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |

---

## 港股

共 4 个工具

### hk_tradecal
**分类**: 港股 > 港股交易日历-获取交易日历

**说明**: /数据接口/港股/港股交易日历-获取交易日历

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: cal_date, is_open, pretrade_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_open` | string | 否 | 是否交易 &#39;0&#39;休市 &#39;1&#39;交易 |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `cal_date` | (默认返回) |
| `is_open` | (默认返回) |
| `pretrade_date` | (默认返回) |

---

### hk_mins
**分类**: 港股 > 港股分钟行情-港股分钟数据，支持1min > 5min > 15min > 30min > 60min行情，提供Python SDK和 http Restful API两种方式

**说明**: /数据接口/港股/港股分钟行情-港股分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束时间 格式：2023-03-13 19:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_time, open, close, high, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `freq` | string | 是 | 分钟频度（1min/5min/15min/30min/60min） |
| `start_date` | string | 否 | 开始日期 格式：2023-03-13 09:00:00 |
| `ts_code` | string | 是 | 股票代码，e.g.00001.HK |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_time` | (默认返回) |
| `open` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### hk_basic
**分类**: 港股 > 港股基础信息-获取港股列表信息

**说明**: /数据接口/港股/港股基础信息-获取港股列表信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, fullname, enname, cn_spell, market, list_status, list_date, delist_date, trade_unit, isin, curr_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `list_status` | string | 否 | 上市状态 L上市 D退市 P暂停上市 ，默认L |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `fullname` | (默认返回) |
| `enname` | (默认返回) |
| `cn_spell` | (默认返回) |
| `market` | (默认返回) |
| `list_status` | (默认返回) |
| `list_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `trade_unit` | (默认返回) |
| `isin` | (默认返回) |
| `curr_type` | (默认返回) |

---

### rt_hk_tick
**分类**: 港股 > 港股实时行情-获取港股实时行情

**说明**: /数据接口/港股/港股实时行情-获取港股实时行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: code, trade_time, pre_close, price, high, open, low, close, vol, amount, num 额外可选字段:   a1_p:    a1_v:    a2_p:    a2_v:    a3_p:    a3_v:    a4_p:    a4_v:    a5_p:    a5_v:    b1_p:    b1_v:    b2_p:    b2_v:    b3_p:    b3_v... |
| `ts_code` | string | 是 | 逗号隔开多个code，例如：00001.HK |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `code` | (默认返回) |
| `trade_time` | (默认返回) |
| `pre_close` | (默认返回) |
| `price` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `num` | (默认返回) |

---

## 港股数据

共 8 个工具

### hk_income
**分类**: 港股数据 > 港股利润表-获取港股上市公司财务利润表数据

**说明**: /数据接口/港股数据/港股利润表-获取港股上市公司财务利润表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始日期（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, name, ind_name, ind_value 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名（如：营业额） |
| `period` | string | 否 | 报告期(格式：YYYYMMDD） |
| `start_date` | string | 否 | 报告期开始日期（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `name` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |

---

### hk_adjfactor
**分类**: 港股数据 > 港股复权因子-获取港股每日复权因子数据，每天滚动刷新

**说明**: /数据接口/港股数据/港股复权因子-获取港股每日复权因子数据，每天滚动刷新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, cum_adjfactor, close_price 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `cum_adjfactor` | (默认返回) |
| `close_price` | (默认返回) |

---

### hk_daily_adj
**分类**: 港股数据 > 港股复权行情-获取港股复权行情，提供股票股本、市值和成交及换手多个数据指标

**说明**: /数据接口/港股数据/港股复权行情-获取港股复权行情，提供股票股本、市值和成交及换手多个数据指标

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_change, vol, amount, vwap, adj_factor, turnover_ratio, free_share, total_share, free_mv, total_mv 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期（YYYYMMDD） |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 否 | 股票代码（e.g. 00001.HK） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `vwap` | (默认返回) |
| `adj_factor` | (默认返回) |
| `turnover_ratio` | (默认返回) |
| `free_share` | (默认返回) |
| `total_share` | (默认返回) |
| `free_mv` | (默认返回) |
| `total_mv` | (默认返回) |

---

### rt_hk_k
**分类**: 港股数据 > 港股实时日线-获取港股实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情

**说明**: /数据接口/港股数据/港股实时日线-获取港股实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, pre_close, close, high, open, low, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | 支持通配符方式，e.g. 00001.HK、02*.HK |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `pre_close` | (默认返回) |
| `close` | (默认返回) |
| `high` | (默认返回) |
| `open` | (默认返回) |
| `low` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### hk_daily
**分类**: 港股数据 > 港股日线行情-获取港股每日增量和历史行情，每日18点左右更新当日数据

**说明**: /数据接口/港股数据/港股日线行情-获取港股每日增量和历史行情，每日18点左右更新当日数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### hk_cashflow
**分类**: 港股数据 > 港股现金流量表-获取港股上市公司现金流量表数据

**说明**: /数据接口/港股数据/港股现金流量表-获取港股上市公司现金流量表数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始日期（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, name, ind_name, ind_value 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名（如：新增贷款） |
| `period` | string | 否 | 报告期(格式：YYYYMMDD） |
| `start_date` | string | 否 | 报告期开始日期（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `name` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |

---

### hk_fina_indicator
**分类**: 港股数据 > 港股财务指标数据-获取港股上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回200条记录，可通过设置日期多次请求获取更多数据。

**说明**: /数据接口/港股数据/港股财务指标数据-获取港股上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回200条记录，可通过设置日期多次请求获取更多数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束日期(格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, end_date, ind_type, report_type, std_report_date, per_netcash_operate, per_oi, bps, basic_eps, diluted_eps, operate_income, operate_income_yoy, gross_profit, gross_profit_yoy, holder_profit, holder_profit_yoy, g... |
| `period` | string | 否 | 报告期(格式：YYYYMMDD） |
| `report_type` | string | 否 | 报告期类型（Q1一季报Q2半年报Q3三季报Q4年报） |
| `start_date` | string | 否 | 报告期开始日期(格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_type` | (默认返回) |
| `report_type` | (默认返回) |
| `std_report_date` | (默认返回) |
| `per_netcash_operate` | (默认返回) |
| `per_oi` | (默认返回) |
| `bps` | (默认返回) |
| `basic_eps` | (默认返回) |
| `diluted_eps` | (默认返回) |
| `operate_income` | (默认返回) |
| `operate_income_yoy` | (默认返回) |
| `gross_profit` | (默认返回) |
| `gross_profit_yoy` | (默认返回) |
| `holder_profit` | (默认返回) |
| `holder_profit_yoy` | (默认返回) |
| `gross_profit_ratio` | (默认返回) |
| `eps_ttm` | (默认返回) |
| `operate_income_qoq` | (默认返回) |
| `net_profit_ratio` | (默认返回) |
| `roe_avg` | (默认返回) |
| `gross_profit_qoq` | (默认返回) |
| `roa` | (默认返回) |
| `holder_profit_qoq` | (默认返回) |
| `roe_yearly` | (默认返回) |
| `roic_yearly` | (默认返回) |
| `total_assets` | (默认返回) |
| `total_liabilities` | (默认返回) |
| `tax_ebt` | (默认返回) |
| `ocf_sales` | (默认返回) |
| `total_parent_equity` | (默认返回) |
| `debt_asset_ratio` | (默认返回) |
| `operate_profit` | (默认返回) |
| `pretax_profit` | (默认返回) |
| `netcash_operate` | (默认返回) |
| `netcash_invest` | (默认返回) |
| `netcash_finance` | (默认返回) |
| `end_cash` | (默认返回) |
| `divi_ratio` | (默认返回) |
| `dividend_rate` | (默认返回) |
| `current_ratio` | (默认返回) |
| `common_acs` | (默认返回) |
| `currentdebt_debt` | (默认返回) |
| `issued_common_shares` | (默认返回) |
| `hk_common_shares` | (默认返回) |
| `per_shares` | (默认返回) |
| `total_market_cap` | (默认返回) |
| `hksk_market_cap` | (默认返回) |
| `pe_ttm` | (默认返回) |
| `pb_ttm` | (默认返回) |
| `report_date_sq` | (默认返回) |
| `report_type_sq` | (默认返回) |
| `operate_income_sq` | (默认返回) |
| `dps_hkd` | (默认返回) |
| `operate_income_qoq_sq` | (默认返回) |
| `net_profit_ratio_sq` | (默认返回) |
| `holder_profit_sq` | (默认返回) |
| `holder_profit_qoq_sq` | (默认返回) |
| `roe_avg_sq` | (默认返回) |
| `pe_ttm_sq` | (默认返回) |
| `pb_ttm_sq` | (默认返回) |
| `roa_sq` | (默认返回) |
| `start_date` | (默认返回) |
| `fiscal_year` | (默认返回) |
| `currency` | (默认返回) |
| `is_cny_code` | (默认返回) |
| `dps_hkd_ly` | (默认返回) |
| `org_type` | (默认返回) |
| `premium_income` | (默认返回) |
| `premium_income_yoy` | (默认返回) |
| `net_interest_income` | (默认返回) |
| `net_interest_income_yoy` | (默认返回) |
| `fee_commission_income` | (默认返回) |
| `fee_commission_income_yoy` | (默认返回) |
| `accounts_rece_tdays` | (默认返回) |
| `inventory_tdays` | (默认返回) |
| `current_assets_tdays` | (默认返回) |
| `total_assets_tdays` | (默认返回) |
| `premium_expense` | (默认返回) |
| `loan_deposit` | (默认返回) |
| `loan_equity` | (默认返回) |
| `loan_assets` | (默认返回) |
| `deposit_equity` | (默认返回) |
| `deposit_assets` | (默认返回) |
| `equity_multiplier` | (默认返回) |
| `equity_ratio` | (默认返回) |

---

### hk_balancesheet
**分类**: 港股数据 > 港股资产负债表-获取港股上市公司资产负债表

**说明**: /数据接口/港股数据/港股资产负债表-获取港股上市公司资产负债表

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始日期（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, end_date, ind_name, ind_value 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名（如：应收帐款） |
| `period` | string | 否 | 报告期(格式：YYYYMMDD） |
| `start_date` | string | 否 | 报告期开始日期（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |

---

## 美股

共 3 个工具

### us_tradecal
**分类**: 美股 > 美股交易日历-获取美股交易日历信息

**说明**: /数据接口/美股/美股交易日历-获取美股交易日历信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: cal_date, is_open, pretrade_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `is_open` | string | 否 | 是否交易 |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `cal_date` | (默认返回) |
| `is_open` | (默认返回) |
| `pretrade_date` | (默认返回) |

---

### us_basic
**分类**: 美股 > 美股基础信息-获取美股列表信息

**说明**: /数据接口/美股/美股基础信息-获取美股列表信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `classify` | string | 否 | 股票分类 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, classify, list_date, delist_date 额外可选字段:   enname: 英文名称 |
| `limit` | string | 否 | 每页最大行数 |
| `offset` | string | 否 | 开始行数 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `classify` | (默认返回) |
| `list_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `enname` | 英文名称 |

---

### us_daily
**分类**: 美股 > 美股日线行情-获取美股行情（未复权），包括全部股票全历史行情，以及重要的市场和估值指标

**说明**: /数据接口/美股/美股日线行情-获取美股行情（未复权），包括全部股票全历史行情，以及重要的市场和估值指标

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, pct_change, vol, amount, vwap 额外可选字段:   pb: PB   pe: PE   change: 涨跌额   total_mv: 总市值   turnover_ratio: 换手率 |
| `start_date` | string | 否 | 开始日期（YYYYMMDD） |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 否 | 股票代码（e.g. AAPL） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `vwap` | (默认返回) |
| `pb` | PB |
| `pe` | PE |
| `change` | 涨跌额 |
| `total_mv` | 总市值 |
| `turnover_ratio` | 换手率 |

---

## 美股数据

共 6 个工具

### us_income
**分类**: 美股数据 > 美股利润表-获取美股上市公司财务利润表数据（目前只覆盖主要美股和中概股）

**说明**: /数据接口/美股数据/美股利润表-获取美股上市公司财务利润表数据（目前只覆盖主要美股和中概股）

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始时间（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, ind_type, name, ind_name, ind_value, report_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名(如：新增借款） |
| `period` | string | 否 | 报告期（格式：YYYYMMDD，每个季度最后一天的日期，如20241231) |
| `report_type` | string | 否 | 报告期类型(Q1一季报Q2半年报Q3三季报Q4年报) |
| `start_date` | string | 否 | 报告期开始时间（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_type` | (默认返回) |
| `name` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |
| `report_type` | (默认返回) |

---

### us_adjfactor
**分类**: 美股数据 > 美股复权因子-获取美股每日复权因子数据，在每天美股收盘后滚动刷新

**说明**: /数据接口/美股数据/美股复权因子-获取美股每日复权因子数据，在每天美股收盘后滚动刷新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, exchange, cum_adjfactor, close_price 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `exchange` | (默认返回) |
| `cum_adjfactor` | (默认返回) |
| `close_price` | (默认返回) |

---

### us_daily_adj
**分类**: 美股数据 > 美股复权行情-获取美股复权行情，支持美股全市场股票，提供股本、市值、复权因子和成交信息等多个数据指标

**说明**: /数据接口/美股数据/美股复权行情-获取美股复权行情，支持美股全市场股票，提供股本、市值、复权因子和成交信息等多个数据指标

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（YYYYMMDD） |
| `exchange` | string | 否 | 交易所（NAS/NYS/OTC) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, pre_close, change, pct_change, vol, amount, vwap, adj_factor, turnover_ratio, free_share, total_share, free_mv, total_mv, exchange 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `limit` | integer | 否 | 每页行数行数 |
| `offset` | integer | 否 | 开始行数 |
| `start_date` | string | 否 | 开始日期（YYYYMMDD） |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD） |
| `ts_code` | string | 否 | 股票代码（e.g. AAPL） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `vwap` | (默认返回) |
| `adj_factor` | (默认返回) |
| `turnover_ratio` | (默认返回) |
| `free_share` | (默认返回) |
| `total_share` | (默认返回) |
| `free_mv` | (默认返回) |
| `total_mv` | (默认返回) |
| `exchange` | (默认返回) |

---

### us_cashflow
**分类**: 美股数据 > 美股现金流量表-获取美股上市公司现金流量表数据（目前只覆盖主要美股和中概股）

**说明**: /数据接口/美股数据/美股现金流量表-获取美股上市公司现金流量表数据（目前只覆盖主要美股和中概股）

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始时间（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, ind_type, name, ind_name, ind_value, report_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名(如：新增借款） |
| `period` | string | 否 | 报告期（格式：YYYYMMDD，每个季度最后一天的日期，如20241231) |
| `report_type` | string | 否 | 报告期类型(Q1一季报Q2半年报Q3三季报Q4年报) |
| `start_date` | string | 否 | 报告期开始时间（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_type` | (默认返回) |
| `name` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |
| `report_type` | (默认返回) |

---

### us_fina_indicator
**分类**: 美股数据 > 美股财务指标数据-获取美股上市公司财务指标数据，目前只覆盖主要美股和中概股。为避免服务器压力，现阶段每次请求最多返回200条记录，可通过设置日期多次请求获取更多数据。

**说明**: /数据接口/美股数据/美股财务指标数据-获取美股上市公司财务指标数据，目前只覆盖主要美股和中概股。为避免服务器压力，现阶段每次请求最多返回200条记录，可通过设置日期多次请求获取更多数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始时间（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, ind_type, security_name_abbr, accounting_standards, notice_date, start_date, std_report_date, financial_date, currency, date_type, report_type, operate_income, operate_income_yoy, gross_profit, gross_profit_... |
| `period` | string | 否 | 报告期（格式：YYYYMMDD，每个季度最后一天的日期，如20241231) |
| `report_type` | string | 否 | 报告期类型(Q1一季报Q2半年报Q3三季报Q4年报) |
| `start_date` | string | 否 | 报告期开始时间（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_type` | (默认返回) |
| `security_name_abbr` | (默认返回) |
| `accounting_standards` | (默认返回) |
| `notice_date` | (默认返回) |
| `start_date` | (默认返回) |
| `std_report_date` | (默认返回) |
| `financial_date` | (默认返回) |
| `currency` | (默认返回) |
| `date_type` | (默认返回) |
| `report_type` | (默认返回) |
| `operate_income` | (默认返回) |
| `operate_income_yoy` | (默认返回) |
| `gross_profit` | (默认返回) |
| `gross_profit_yoy` | (默认返回) |
| `parent_holder_netprofit` | (默认返回) |
| `parent_holder_netprofit_yoy` | (默认返回) |
| `basic_eps` | (默认返回) |
| `diluted_eps` | (默认返回) |
| `gross_profit_ratio` | (默认返回) |
| `net_profit_ratio` | (默认返回) |
| `accounts_rece_tr` | (默认返回) |
| `inventory_tr` | (默认返回) |
| `total_assets_tr` | (默认返回) |
| `accounts_rece_tdays` | (默认返回) |
| `inventory_tdays` | (默认返回) |
| `total_assets_tdays` | (默认返回) |
| `roe_avg` | (默认返回) |
| `roa` | (默认返回) |
| `current_ratio` | (默认返回) |
| `speed_ratio` | (默认返回) |
| `ocf_liqdebt` | (默认返回) |
| `debt_asset_ratio` | (默认返回) |
| `equity_ratio` | (默认返回) |
| `basic_eps_yoy` | (默认返回) |
| `gross_profit_ratio_yoy` | (默认返回) |
| `net_profit_ratio_yoy` | (默认返回) |
| `roe_avg_yoy` | (默认返回) |
| `roa_yoy` | (默认返回) |
| `debt_asset_ratio_yoy` | (默认返回) |
| `current_ratio_yoy` | (默认返回) |
| `speed_ratio_yoy` | (默认返回) |
| `currency_abbr` | (默认返回) |
| `total_income` | (默认返回) |
| `total_income_yoy` | (默认返回) |
| `premium_income` | (默认返回) |
| `premium_income_yoy` | (默认返回) |
| `basic_eps_cs` | (默认返回) |
| `basic_eps_cs_yoy` | (默认返回) |
| `diluted_eps_cs` | (默认返回) |
| `payout_ratio` | (默认返回) |
| `capitial_ratio` | (默认返回) |
| `roe` | (默认返回) |
| `roe_yoy` | (默认返回) |
| `debt_ratio` | (默认返回) |
| `debt_ratio_yoy` | (默认返回) |
| `net_interest_income` | (默认返回) |
| `net_interest_income_yoy` | (默认返回) |
| `diluted_eps_cs_yoy` | (默认返回) |
| `loan_loss_provision` | (默认返回) |
| `loan_loss_provision_yoy` | (默认返回) |
| `loan_deposit` | (默认返回) |
| `loan_equity` | (默认返回) |
| `loan_assets` | (默认返回) |
| `deposit_equity` | (默认返回) |
| `deposit_assets` | (默认返回) |
| `rol` | (默认返回) |
| `rod` | (默认返回) |

---

### us_balancesheet
**分类**: 美股数据 > 美股资产负债表-获取美股上市公司资产负债表（目前只覆盖主要美股和中概股）

**说明**: /数据接口/美股数据/美股资产负债表-获取美股上市公司资产负债表（目前只覆盖主要美股和中概股）

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告结束始时间（格式：YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, ind_type, name, ind_name, ind_value, report_type 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 指标名(如：新增借款） |
| `period` | string | 否 | 报告期（格式：YYYYMMDD，每个季度最后一天的日期，如20241231) |
| `report_type` | string | 否 | 报告期类型(Q1一季报Q2半年报Q3三季报Q4年报) |
| `start_date` | string | 否 | 报告期开始时间（格式：YYYYMMDD） |
| `ts_code` | string | 是 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `ind_type` | (默认返回) |
| `name` | (默认返回) |
| `ind_name` | (默认返回) |
| `ind_value` | (默认返回) |
| `report_type` | (默认返回) |

---

## 债券

共 12 个工具

### repo_daily
**分类**: 债券 > 债券回购日行情-债券回购日行情

**说明**: /数据接口/债券/债券回购日行情-债券回购日行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, repo_maturity, pre_close, open, high, low, close, weight, weight_r, amount, num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `repo_maturity` | (默认返回) |
| `pre_close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `weight` | (默认返回) |
| `weight_r` | (默认返回) |
| `amount` | (默认返回) |
| `num` | (默认返回) |

---

### eco_cal
**分类**: 债券 > 全球财经事件-获取全球财经日历、包括经济事件数据更新

**说明**: /数据接口/债券/全球财经事件-获取全球财经日历、包括经济事件数据更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `country` | string | 否 | 国家（比如：中国、美国） |
| `currency` | string | 否 | 货币代码 |
| `date` | string | 否 | 日期（YYYYMMDD格式） |
| `end_date` | string | 否 | 结束日期 |
| `event` | string | 否 | 事件 （支持模糊匹配： \*非农\*） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, time, currency, country, event, value, pre_value, fore_value 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `time` | (默认返回) |
| `currency` | (默认返回) |
| `country` | (默认返回) |
| `event` | (默认返回) |
| `value` | (默认返回) |
| `pre_value` | (默认返回) |
| `fore_value` | (默认返回) |

---

### cb_issue
**分类**: 债券 > 可转债发行-获取可转债发行数据

**说明**: /数据接口/债券/可转债发行-获取可转债发行数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 发行公告日 |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, res_ann_date, plan_issue_size, issue_size, issue_price, issue_type, onl_code, onl_name, onl_date, onl_size, onl_pch_vol, onl_pch_num, onl_pch_excess, shd_ration_code, shd_ration_name, shd_ration_date, shd_ra... |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `res_ann_date` | (默认返回) |
| `plan_issue_size` | (默认返回) |
| `issue_size` | (默认返回) |
| `issue_price` | (默认返回) |
| `issue_type` | (默认返回) |
| `onl_code` | (默认返回) |
| `onl_name` | (默认返回) |
| `onl_date` | (默认返回) |
| `onl_size` | (默认返回) |
| `onl_pch_vol` | (默认返回) |
| `onl_pch_num` | (默认返回) |
| `onl_pch_excess` | (默认返回) |
| `shd_ration_code` | (默认返回) |
| `shd_ration_name` | (默认返回) |
| `shd_ration_date` | (默认返回) |
| `shd_ration_record_date` | (默认返回) |
| `shd_ration_pay_date` | (默认返回) |
| `shd_ration_price` | (默认返回) |
| `shd_ration_ratio` | (默认返回) |
| `shd_ration_size` | (默认返回) |
| `offl_size` | (默认返回) |
| `issue_cost` | 发行费用（元） |
| `offl_deposit` | 网下发行定金比例（%） |
| `offl_pch_num` | 网下发行有效申购户数 |
| `offl_pch_vol` | 网下发行有效申购数量（张） |
| `shd_ration_num` | 老股东配售有效申购户数 |
| `shd_ration_vol` | 老股东配售有效申购数量（张） |
| `offl_pch_excess` | 网下发行超额认购倍数 |
| `lead_underwriter` | 主承销商 |
| `onl_winning_rate` | 网上发行中签率（%） |
| `offl_winning_rate` | 网下发行中签率 |
| `shd_ration_excess` | 老股东配售超额认购倍数 |
| `lead_underwriter_vol` | 主承销商包销数量（张） |

---

### cb_basic
**分类**: 债券 > 可转债基础信息-获取可转债基本信息

**说明**: /数据接口/债券/可转债基础信息-获取可转债基本信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `exchange` | string | 否 | 上市交易所 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, bond_full_name, bond_short_name, cb_code, cb_type, stk_code, stk_short_name, maturity, par, issue_price, issue_size, remain_size, value_date, maturity_date, rate_type, coupon_rate, add_rate, pay_per_year, list_date, d... |
| `list_date` | string | 否 | 上市日期 |
| `ts_code` | string | 否 | 转债代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `bond_full_name` | (默认返回) |
| `bond_short_name` | (默认返回) |
| `cb_code` | (默认返回) |
| `cb_type` | (默认返回) |
| `stk_code` | (默认返回) |
| `stk_short_name` | (默认返回) |
| `maturity` | (默认返回) |
| `par` | (默认返回) |
| `issue_price` | (默认返回) |
| `issue_size` | (默认返回) |
| `remain_size` | (默认返回) |
| `value_date` | (默认返回) |
| `maturity_date` | (默认返回) |
| `rate_type` | (默认返回) |
| `coupon_rate` | (默认返回) |
| `add_rate` | (默认返回) |
| `pay_per_year` | (默认返回) |
| `list_date` | (默认返回) |
| `delist_date` | (默认返回) |
| `exchange` | (默认返回) |
| `conv_start_date` | (默认返回) |
| `conv_end_date` | (默认返回) |
| `conv_stop_date` | (默认返回) |
| `first_conv_price` | (默认返回) |
| `conv_price` | (默认返回) |
| `rate_clause` | (默认返回) |
| `guarantor` | 担保人 |
| `put_clause` | 回售条款 |
| `call_clause` | 赎回条款 |
| `conv_clause` | 转股条款 |
| `rating_comp` | 最新评级机构 |
| `issue_rating` | 发行信用等级 |
| `reset_clause` | 特别向下修正条款 |
| `newest_rating` | 最新信用等级 |
| `guarantee_type` | 担保方式 |
| `maturity_put_price` | 到期赎回价格(含税)[更名停用，请使用maturity_call_price] |
| `maturity_call_price` | 到期赎回价格(含税) |

---

### cb_rate
**分类**: 债券 > 可转债票面利率-获取可转债票面利率

**说明**: /数据接口/债券/可转债票面利率-获取可转债票面利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code 额外可选字段:   rate_freq: 付息频率(次/年)   coupon_rate: 票面利率(%)   rate_end_date: 付息结束日期   rate_start_date: 付息开始日期 |
| `ts_code` | string | 是 | 转债代码，支持多值输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `rate_freq` | 付息频率(次/年) |
| `coupon_rate` | 票面利率(%) |
| `rate_end_date` | 付息结束日期 |
| `rate_start_date` | 付息开始日期 |

---

### cb_daily
**分类**: 债券 > 可转债行情-获取可转债行情

**说明**: /数据接口/债券/可转债行情-获取可转债行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, pre_close, open, high, low, close, change, pct_chg, vol, amount 额外可选字段:   cb_value: 转股价值   bond_value: 纯债价值   cb_over_rate: 转股溢价率(%)   bond_over_rate: 纯债溢价率(%) |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `pre_close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `change` | (默认返回) |
| `pct_chg` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `cb_value` | 转股价值 |
| `bond_value` | 纯债价值 |
| `cb_over_rate` | 转股溢价率(%) |
| `bond_over_rate` | 纯债溢价率(%) |

---

### cb_price_chg
**分类**: 债券 > 可转债转股价变动-获取可转债转股价变动

**说明**: /数据接口/债券/可转债转股价变动-获取可转债转股价变动

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, bond_short_name, publish_date, change_date, convert_price_initial, convertprice_bef, convertprice_aft 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | 转债代码，支持多值输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `bond_short_name` | (默认返回) |
| `publish_date` | (默认返回) |
| `change_date` | (默认返回) |
| `convert_price_initial` | (默认返回) |
| `convertprice_bef` | (默认返回) |
| `convertprice_aft` | (默认返回) |

---

### yc_cb
**分类**: 债券 > 国债收益率曲线-获取中债收益率曲线，目前可获取中债国债收益率曲线即期和到期收益率曲线数据

**说明**: /数据接口/债券/国债收益率曲线-获取中债收益率曲线，目前可获取中债国债收益率曲线即期和到期收益率曲线数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `curve_term` | number | 否 | 期限 |
| `curve_type` | string | 否 | 曲线类型：0-到期，1-即期 |
| `end_date` | string | 否 | 查询结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, curve_name, curve_type, curve_term, yield 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 查询起始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 收益率曲线编码：1001.CB-国债收益率曲线 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `curve_name` | (默认返回) |
| `curve_type` | (默认返回) |
| `curve_term` | (默认返回) |
| `yield` | (默认返回) |

---

### bond_blk
**分类**: 债券 > 大宗交易-获取沪深交易所债券大宗交易数据

**说明**: /数据接口/债券/大宗交易-获取沪深交易所债券大宗交易数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, price, vol, amount 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 债券代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `price` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |

---

### bond_blk_detail
**分类**: 债券 > 大宗交易明细-获取沪深交易所债券大宗交易数据

**说明**: /数据接口/债券/大宗交易明细-获取沪深交易所债券大宗交易数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, name, price, vol, amount, buy_dp, sell_dp 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（YYYYMMDD格式，下同） |
| `ts_code` | string | 否 | 债券代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `price` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `buy_dp` | (默认返回) |
| `sell_dp` | (默认返回) |

---

### bc_otcqt
**分类**: 债券 > 柜台流通式债券报价-柜台流通式债券报价

**说明**: /数据接口/债券/柜台流通式债券报价-柜台流通式债券报价

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `bank` | string | 否 | 报价机构 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段:  额外可选字段:   bank: 报价机构   name: 债券简称   qt_time: 报价时间   ts_code: 债券编码   maturity: 期限   bond_type: 债券类型   buy_price: 投资者买入全价   buy_yield: 投资者买入到期收益率（%）   sell_price: 投资者卖出全价   sell_yield: 投资者卖出到期收益率（%）   trade_date: 报价日期   coupon_... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `bank` | 报价机构 |
| `name` | 债券简称 |
| `qt_time` | 报价时间 |
| `ts_code` | 债券编码 |
| `maturity` | 期限 |
| `bond_type` | 债券类型 |
| `buy_price` | 投资者买入全价 |
| `buy_yield` | 投资者买入到期收益率（%） |
| `sell_price` | 投资者卖出全价 |
| `sell_yield` | 投资者卖出到期收益率（%） |
| `trade_date` | 报价日期 |
| `coupon_rate` | 票面利率（%） |
| `remain_maturity` | 剩余期限 |

---

### bc_bestotcqt
**分类**: 债券 > 柜台流通式债券最优报价-柜台流通式债券最优报价

**说明**: /数据接口/债券/柜台流通式债券最优报价-柜台流通式债券最优报价

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段:  额外可选字段:   name: 债券简称   ts_code: 债券编码   bond_type: 债券类型   trade_date: 报价日期   best_buy_bank: 最优报买价方   best_buy_price: 投资者最优买入全价   best_buy_yield: 投资者最优买入价到期收益率（%）   best_sell_bank: 最优卖报价方   best_sell_price: 投资者最优卖出全价   best_sel... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 报价日期(YYYYMMDD格式，下同) |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `name` | 债券简称 |
| `ts_code` | 债券编码 |
| `bond_type` | 债券类型 |
| `trade_date` | 报价日期 |
| `best_buy_bank` | 最优报买价方 |
| `best_buy_price` | 投资者最优买入全价 |
| `best_buy_yield` | 投资者最优买入价到期收益率（%） |
| `best_sell_bank` | 最优卖报价方 |
| `best_sell_price` | 投资者最优卖出全价 |
| `best_sell_yield` | 投资者最优卖出价到期收益率（%） |
| `remain_maturity` | 剩余期限 |

---

## 债券专题

共 5 个工具

### cb_rating
**分类**: 债券专题 > 可转债债券评级-获取可转债评级历史记录

**说明**: /数据接口/债券专题/可转债债券评级-获取可转债评级历史记录

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ann_date, rating_date, rating_com_name, rating_way, rating_type, rating, rating_outlook 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 是 | 转债代码，支持多值输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ann_date` | (默认返回) |
| `rating_date` | (默认返回) |
| `rating_com_name` | (默认返回) |
| `rating_way` | (默认返回) |
| `rating_type` | (默认返回) |
| `rating` | (默认返回) |
| `rating_outlook` | (默认返回) |

---

### top10_cb_holders
**分类**: 债券专题 > 可转债十大持有人-获取可转债前十大持有人

**说明**: /数据接口/债券专题/可转债十大持有人-获取可转债前十大持有人

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, end_date, holder_rank, holder_name, hold_amount, hold_ratio 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `period` | string | 否 | 报告期（YYYYMMDD格式，年中和年报日期，如20240630,20251231） |
| `start_date` | string | 否 | 报告期开始日期 |
| `ts_code` | string | 是 | TS代码，支持多值输入，如110059.SH,110060.SH |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `end_date` | (默认返回) |
| `holder_rank` | (默认返回) |
| `holder_name` | (默认返回) |
| `hold_amount` | (默认返回) |
| `hold_ratio` | (默认返回) |

---

### cb_factor_pro
**分类**: 债券专题 > 可转债技术面因子(专业版）-获取可转债每日技术面因子数据，用于跟踪可转债当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，_qfq表示前复权 _hfq表示后复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

**说明**: /数据接口/债券专题/可转债技术面因子(专业版）-获取可转债每日技术面因子数据，用于跟踪可转债当前走势情况，数据由Tushare社区自产，覆盖全历史；输出参数_bfq表示不复权，_qfq表示前复权 _hfq表示后复权，描述中说明了因子的默认传参，如需要特殊参数或者更多因子可以联系管理员评估

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, open, high, low, close, pre_close, change, pct_change, vol, amount, asi_bfq, asit_bfq, atr_bfq, bbi_bfq, bias1_bfq, bias2_bfq, bias3_bfq, boll_lower_bfq, boll_mid_bfq, boll_upper_bfq, brar_ar_bfq, brar_br_... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 可转债代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `close` | (默认返回) |
| `pre_close` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `asi_bfq` | (默认返回) |
| `asit_bfq` | (默认返回) |
| `atr_bfq` | (默认返回) |
| `bbi_bfq` | (默认返回) |
| `bias1_bfq` | (默认返回) |
| `bias2_bfq` | (默认返回) |
| `bias3_bfq` | (默认返回) |
| `boll_lower_bfq` | (默认返回) |
| `boll_mid_bfq` | (默认返回) |
| `boll_upper_bfq` | (默认返回) |
| `brar_ar_bfq` | (默认返回) |
| `brar_br_bfq` | (默认返回) |
| `cci_bfq` | (默认返回) |
| `cr_bfq` | (默认返回) |
| `dfma_dif_bfq` | (默认返回) |
| `dfma_difma_bfq` | (默认返回) |
| `dmi_adx_bfq` | (默认返回) |
| `dmi_adxr_bfq` | (默认返回) |
| `dmi_mdi_bfq` | (默认返回) |
| `dmi_pdi_bfq` | (默认返回) |
| `downdays` | (默认返回) |
| `updays` | (默认返回) |
| `dpo_bfq` | (默认返回) |
| `madpo_bfq` | (默认返回) |
| `ema_bfq_10` | (默认返回) |
| `ema_bfq_20` | (默认返回) |
| `ema_bfq_250` | (默认返回) |
| `ema_bfq_30` | (默认返回) |
| `ema_bfq_5` | (默认返回) |
| `ema_bfq_60` | (默认返回) |
| `ema_bfq_90` | (默认返回) |
| `emv_bfq` | (默认返回) |
| `maemv_bfq` | (默认返回) |
| `expma_12_bfq` | (默认返回) |
| `expma_50_bfq` | (默认返回) |
| `kdj_bfq` | (默认返回) |
| `kdj_d_bfq` | (默认返回) |
| `kdj_k_bfq` | (默认返回) |
| `ktn_down_bfq` | (默认返回) |
| `ktn_mid_bfq` | (默认返回) |
| `ktn_upper_bfq` | (默认返回) |
| `lowdays` | (默认返回) |
| `topdays` | (默认返回) |
| `ma_bfq_10` | (默认返回) |
| `ma_bfq_20` | (默认返回) |
| `ma_bfq_250` | (默认返回) |
| `ma_bfq_30` | (默认返回) |
| `ma_bfq_5` | (默认返回) |
| `ma_bfq_60` | (默认返回) |
| `ma_bfq_90` | (默认返回) |
| `macd_bfq` | (默认返回) |
| `macd_dea_bfq` | (默认返回) |
| `macd_dif_bfq` | (默认返回) |
| `mass_bfq` | (默认返回) |
| `ma_mass_bfq` | (默认返回) |
| `mfi_bfq` | (默认返回) |
| `mtm_bfq` | (默认返回) |
| `mtmma_bfq` | (默认返回) |
| `obv_bfq` | (默认返回) |
| `psy_bfq` | (默认返回) |
| `psyma_bfq` | (默认返回) |
| `roc_bfq` | (默认返回) |
| `maroc_bfq` | (默认返回) |
| `rsi_bfq_12` | (默认返回) |
| `rsi_bfq_24` | (默认返回) |
| `rsi_bfq_6` | (默认返回) |
| `taq_down_bfq` | (默认返回) |
| `taq_mid_bfq` | (默认返回) |
| `taq_up_bfq` | (默认返回) |
| `trix_bfq` | (默认返回) |
| `trma_bfq` | (默认返回) |
| `vr_bfq` | (默认返回) |
| `wr_bfq` | (默认返回) |
| `wr1_bfq` | (默认返回) |
| `xsii_td1_bfq` | (默认返回) |
| `xsii_td2_bfq` | (默认返回) |
| `xsii_td3_bfq` | (默认返回) |
| `xsii_td4_bfq` | (默认返回) |

---

### cb_call
**分类**: 债券专题 > 可转债赎回信息-获取可转债到期赎回、强制赎回等信息。数据来源于公开披露渠道，供个人和机构研究使用，请不要用于数据商业目的。

**说明**: /数据接口/债券专题/可转债赎回信息-获取可转债到期赎回、强制赎回等信息。数据来源于公开披露渠道，供个人和机构研究使用，请不要用于数据商业目的。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期(YYYYMMDD格式，下同) |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, call_type, is_call, ann_date, call_date, call_price, call_price_tax, call_vol, call_amount, payment_date, call_reg_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | 转债代码，支持多值输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `call_type` | (默认返回) |
| `is_call` | (默认返回) |
| `ann_date` | (默认返回) |
| `call_date` | (默认返回) |
| `call_price` | (默认返回) |
| `call_price_tax` | (默认返回) |
| `call_vol` | (默认返回) |
| `call_amount` | (默认返回) |
| `payment_date` | (默认返回) |
| `call_reg_date` | (默认返回) |

---

### cb_share
**分类**: 债券专题 > 可转债转股结果-获取可转债转股结果

**说明**: /数据接口/债券专题/可转债转股结果-获取可转债转股结果

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 是 | 公告日期（YYYYMMDD格式，下同） |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, bond_short_name, publish_date, end_date, issue_size, convert_price_initial, convert_price, convert_val, convert_vol, convert_ratio, acc_convert_val, acc_convert_vol, acc_convert_ratio, remain_size, total_shares 额外可选字段... |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 是 | 转债代码，支持多值输入 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `bond_short_name` | (默认返回) |
| `publish_date` | (默认返回) |
| `end_date` | (默认返回) |
| `issue_size` | (默认返回) |
| `convert_price_initial` | (默认返回) |
| `convert_price` | (默认返回) |
| `convert_val` | (默认返回) |
| `convert_vol` | (默认返回) |
| `convert_ratio` | (默认返回) |
| `acc_convert_val` | (默认返回) |
| `acc_convert_vol` | (默认返回) |
| `acc_convert_ratio` | (默认返回) |
| `remain_size` | (默认返回) |
| `total_shares` | (默认返回) |

---

## 宏观经济

共 19 个工具

### cn_schedule
**分类**: 宏观经济 > 国内宏观 > 中国经济数据发布日程-获取国家统计局、中国人民银行等经济数据发布日程及对应tushare接口，持续更新中

**说明**: /数据接口/宏观经济/国内宏观/中国经济数据发布日程-获取国家统计局、中国人民银行等经济数据发布日程及对应tushare接口，持续更新中

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, publish_date, title, issuing_org, data_api 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `m` | string | 否 | 月份（YYYYMM） |
| `title` | string | 否 | 发布数据 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `publish_date` | (默认返回) |
| `title` | (默认返回) |
| `issuing_org` | (默认返回) |
| `data_api` | (默认返回) |

---

### cn_cpi
**分类**: 宏观经济 > 国内宏观 > 价格指数 > 居民消费价格指数（CPI）-获取CPI居民消费价格数据，包括全国、城市和农村的数据

**说明**: /数据接口/宏观经济/国内宏观/价格指数/居民消费价格指数（CPI）-获取CPI居民消费价格数据，包括全国、城市和农村的数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_m` | string | 否 | 结束月份 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, nt_val, nt_yoy, nt_mom, nt_accu, town_val, town_yoy, town_mom, town_accu, cnt_val, cnt_yoy, cnt_mom, cnt_accu 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `m` | string | 否 | 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔 |
| `start_m` | string | 否 | 开始月份 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `nt_val` | (默认返回) |
| `nt_yoy` | (默认返回) |
| `nt_mom` | (默认返回) |
| `nt_accu` | (默认返回) |
| `town_val` | (默认返回) |
| `town_yoy` | (默认返回) |
| `town_mom` | (默认返回) |
| `town_accu` | (默认返回) |
| `cnt_val` | (默认返回) |
| `cnt_yoy` | (默认返回) |
| `cnt_mom` | (默认返回) |
| `cnt_accu` | (默认返回) |

---

### cn_ppi
**分类**: 宏观经济 > 国内宏观 > 价格指数 > 工业生产者出厂价格指数（PPI）-获取PPI工业生产者出厂价格指数数据

**说明**: /数据接口/宏观经济/国内宏观/价格指数/工业生产者出厂价格指数（PPI）-获取PPI工业生产者出厂价格指数数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_m` | string | 否 | 结束月份 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, ppi_yoy, ppi_mp_yoy, ppi_mp_qm_yoy, ppi_mp_rm_yoy, ppi_mp_p_yoy, ppi_cg_yoy, ppi_cg_f_yoy, ppi_cg_c_yoy, ppi_cg_adu_yoy, ppi_cg_dcg_yoy, ppi_mom, ppi_mp_mom, ppi_mp_qm_mom, ppi_mp_rm_mom, ppi_mp_p_mom, ppi_cg_mom, ppi_c... |
| `m` | string | 否 | 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔 |
| `start_m` | string | 否 | 开始月份 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `ppi_yoy` | (默认返回) |
| `ppi_mp_yoy` | (默认返回) |
| `ppi_mp_qm_yoy` | (默认返回) |
| `ppi_mp_rm_yoy` | (默认返回) |
| `ppi_mp_p_yoy` | (默认返回) |
| `ppi_cg_yoy` | (默认返回) |
| `ppi_cg_f_yoy` | (默认返回) |
| `ppi_cg_c_yoy` | (默认返回) |
| `ppi_cg_adu_yoy` | (默认返回) |
| `ppi_cg_dcg_yoy` | (默认返回) |
| `ppi_mom` | (默认返回) |
| `ppi_mp_mom` | (默认返回) |
| `ppi_mp_qm_mom` | (默认返回) |
| `ppi_mp_rm_mom` | (默认返回) |
| `ppi_mp_p_mom` | (默认返回) |
| `ppi_cg_mom` | (默认返回) |
| `ppi_cg_f_mom` | (默认返回) |
| `ppi_cg_c_mom` | (默认返回) |
| `ppi_cg_adu_mom` | (默认返回) |
| `ppi_cg_dcg_mom` | (默认返回) |
| `ppi_accu` | (默认返回) |
| `ppi_mp_accu` | (默认返回) |
| `ppi_mp_qm_accu` | (默认返回) |
| `ppi_mp_rm_accu` | (默认返回) |
| `ppi_mp_p_accu` | (默认返回) |
| `ppi_cg_accu` | (默认返回) |
| `ppi_cg_f_accu` | (默认返回) |
| `ppi_cg_c_accu` | (默认返回) |
| `ppi_cg_adu_accu` | (默认返回) |
| `ppi_cg_dcg_accu` | (默认返回) |

---

### hibor
**分类**: 宏观经济 > 国内宏观 > 利率数据 > Hibor利率-Hibor利率

**说明**: /数据接口/宏观经济/国内宏观/利率数据/Hibor利率-Hibor利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期  (日期输入格式：YYYYMMDD，下同) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, on, 1w, 2w, 1m, 2m, 3m, 6m, 12m 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `on` | (默认返回) |

---

### shibor_lpr
**分类**: 宏观经济 > 国内宏观 > 利率数据 > LPR贷款基础利率-LPR贷款基础利率

**说明**: /数据接口/宏观经济/国内宏观/利率数据/LPR贷款基础利率-LPR贷款基础利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期  (日期输入格式：YYYYMMDD，下同) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, 1y, 5y 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |

---

### libor
**分类**: 宏观经济 > 国内宏观 > 利率数据 > Libor利率-Libor拆借利率

**说明**: /数据接口/宏观经济/国内宏观/利率数据/Libor利率-Libor拆借利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `curr_type` | string | 否 | 货币代码  (USD美元  EUR欧元  JPY日元  GBP英镑  CHF瑞郎，默认是USD) |
| `date` | string | 否 | 日期 (日期输入格式：YYYYMMDD，下同) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, curr_type, on, 1w, 1m, 2m, 3m, 6m, 12m 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `curr_type` | (默认返回) |
| `on` | (默认返回) |

---

### shibor
**分类**: 宏观经济 > 国内宏观 > 利率数据 > Shibor利率-shibor利率

**说明**: /数据接口/宏观经济/国内宏观/利率数据/Shibor利率-shibor利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 (日期输入格式：YYYYMMDD，下同) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, on, 1w, 2w, 1m, 3m, 6m, 9m, 1y 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `on` | (默认返回) |

---

### shibor_quote
**分类**: 宏观经济 > 国内宏观 > 利率数据 > Shibor报价数据-Shibor报价数据

**说明**: /数据接口/宏观经济/国内宏观/利率数据/Shibor报价数据-Shibor报价数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `bank` | string | 否 | 银行名称 （中文名称，例如 农业银行） |
| `date` | string | 否 | 日期 (日期输入格式：YYYYMMDD，下同) |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, bank, on_b, on_a, 1w_b, 1w_a, 2w_b, 2w_a, 1m_b, 1m_a, 3m_b, 3m_a, 6m_b, 6m_a, 9m_b, 9m_a, 1y_b, 1y_a 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `bank` | (默认返回) |
| `on_b` | (默认返回) |
| `on_a` | (默认返回) |

---

### gz_index
**分类**: 宏观经济 > 国内宏观 > 利率数据 > 广州民间借贷利率-广州民间借贷利率

**说明**: /数据接口/宏观经济/国内宏观/利率数据/广州民间借贷利率-广州民间借贷利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, d10_rate, m1_rate, m3_rate, m6_rate, m12_rate, long_rate 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `d10_rate` | (默认返回) |
| `m1_rate` | (默认返回) |
| `m3_rate` | (默认返回) |
| `m6_rate` | (默认返回) |
| `m12_rate` | (默认返回) |
| `long_rate` | (默认返回) |

---

### wz_index
**分类**: 宏观经济 > 国内宏观 > 利率数据 > 温州民间借贷利率-温州民间借贷利率，即温州指数

**说明**: /数据接口/宏观经济/国内宏观/利率数据/温州民间借贷利率-温州民间借贷利率，即温州指数

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, comp_rate, center_rate, micro_rate, cm_rate, sdb_rate, om_rate, aa_rate, m1_rate, m3_rate, m6_rate, m12_rate, long_rate 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `comp_rate` | (默认返回) |
| `center_rate` | (默认返回) |
| `micro_rate` | (默认返回) |
| `cm_rate` | (默认返回) |
| `sdb_rate` | (默认返回) |
| `om_rate` | (默认返回) |
| `aa_rate` | (默认返回) |
| `m1_rate` | (默认返回) |
| `m3_rate` | (默认返回) |
| `m6_rate` | (默认返回) |
| `m12_rate` | (默认返回) |
| `long_rate` | (默认返回) |

---

### cn_gdp
**分类**: 宏观经济 > 国内宏观 > 国民经济 > 国内生产总值（GDP）-获取国民经济之GDP数据

**说明**: /数据接口/宏观经济/国内宏观/国民经济/国内生产总值（GDP）-获取国民经济之GDP数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_q` | string | 否 | 结束季度 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: quarter, gdp, gdp_yoy, pi, pi_yoy, si, si_yoy, ti, ti_yoy 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `q` | string | 否 | 季度（2019Q1表示，2019年第一季度） |
| `start_q` | string | 否 | 开始季度 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `quarter` | (默认返回) |
| `gdp` | (默认返回) |
| `gdp_yoy` | (默认返回) |
| `pi` | (默认返回) |
| `pi_yoy` | (默认返回) |
| `si` | (默认返回) |
| `si_yoy` | (默认返回) |
| `ti` | (默认返回) |
| `ti_yoy` | (默认返回) |

---

### cn_pmi
**分类**: 宏观经济 > 国内宏观 > 景气度 > 采购经理指数（PMI）-采购经理人指数

**说明**: /数据接口/宏观经济/国内宏观/景气度/采购经理指数（PMI）-采购经理人指数

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_m` | string | 否 | 结束月度（e.g. fields='month,pmi010000,pmi010400'） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段:  额外可选字段:   month: 月份YYYYMM   pmi010000: 制造业PMI   pmi010100: 制造业PMI:企业规模/大型企业   pmi010200: 制造业PMI:企业规模/中型企业   pmi010300: 制造业PMI:企业规模/小型企业   pmi010400: 制造业PMI:构成指数/生产指数   pmi010401: 制造业PMI:构成指数/生产指数:企业规模/大型企业   pmi010402: 制造业PMI... |
| `m` | string | 否 | 月度（202401表示，2024年1月） |
| `start_m` | string | 否 | 开始月度 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | 月份YYYYMM |
| `pmi010000` | 制造业PMI |
| `pmi010100` | 制造业PMI:企业规模/大型企业 |
| `pmi010200` | 制造业PMI:企业规模/中型企业 |
| `pmi010300` | 制造业PMI:企业规模/小型企业 |
| `pmi010400` | 制造业PMI:构成指数/生产指数 |
| `pmi010401` | 制造业PMI:构成指数/生产指数:企业规模/大型企业 |
| `pmi010402` | 制造业PMI:构成指数/生产指数:企业规模/中型企业 |
| `pmi010403` | 制造业PMI:构成指数/生产指数:企业规模/小型企业 |
| `pmi010500` | 制造业PMI:构成指数/新订单指数 |
| `pmi010501` | 制造业PMI:构成指数/新订单指数:企业规模/大型企业 |
| `pmi010502` | 制造业PMI:构成指数/新订单指数:企业规模/中型企业 |
| `pmi010503` | 制造业PMI:构成指数/新订单指数:企业规模/小型企业 |
| `pmi010600` | 制造业PMI:构成指数/供应商配送时间指数 |
| `pmi010601` | 制造业PMI:构成指数/供应商配送时间指数:企业规模/大型企业 |
| `pmi010602` | 制造业PMI:构成指数/供应商配送时间指数:企业规模/中型企业 |
| `pmi010603` | 制造业PMI:构成指数/供应商配送时间指数:企业规模/小型企业 |
| `pmi010700` | 制造业PMI:构成指数/原材料库存指数 |
| `pmi010701` | 制造业PMI:构成指数/原材料库存指数:企业规模/大型企业 |
| `pmi010702` | 制造业PMI:构成指数/原材料库存指数:企业规模/中型企业 |
| `pmi010703` | 制造业PMI:构成指数/原材料库存指数:企业规模/小型企业 |
| `pmi010800` | 制造业PMI:构成指数/从业人员指数 |
| `pmi010801` | 制造业PMI:构成指数/从业人员指数:企业规模/大型企业 |
| `pmi010802` | 制造业PMI:构成指数/从业人员指数:企业规模/中型企业 |
| `pmi010803` | 制造业PMI:构成指数/从业人员指数:企业规模/小型企业 |
| `pmi010900` | 制造业PMI:其他/新出口订单 |
| `pmi011000` | 制造业PMI:其他/进口 |
| `pmi011100` | 制造业PMI:其他/采购量 |
| `pmi011200` | 制造业PMI:其他/主要原材料购进价格 |
| `pmi011300` | 制造业PMI:其他/出厂价格 |
| `pmi011400` | 制造业PMI:其他/产成品库存 |
| `pmi011500` | 制造业PMI:其他/在手订单 |
| `pmi011600` | 制造业PMI:其他/生产经营活动预期 |
| `pmi011700` | 制造业PMI:分行业/装备制造业 |
| `pmi011800` | 制造业PMI:分行业/高技术制造业 |
| `pmi011900` | 制造业PMI:分行业/基础原材料制造业 |
| `pmi012000` | 制造业PMI:分行业/消费品制造业 |
| `pmi020100` | 非制造业PMI:商务活动 |
| `pmi020101` | 非制造业PMI:商务活动:分行业/建筑业 |
| `pmi020102` | 非制造业PMI:商务活动:分行业/服务业业 |
| `pmi020200` | 非制造业PMI:新订单指数 |
| `pmi020201` | 非制造业PMI:新订单指数:分行业/建筑业 |
| `pmi020202` | 非制造业PMI:新订单指数:分行业/服务业 |
| `pmi020300` | 非制造业PMI:投入品价格指数 |
| `pmi020301` | 非制造业PMI:投入品价格指数:分行业/建筑业 |
| `pmi020302` | 非制造业PMI:投入品价格指数:分行业/服务业 |
| `pmi020400` | 非制造业PMI:销售价格指数 |
| `pmi020401` | 非制造业PMI:销售价格指数:分行业/建筑业 |
| `pmi020402` | 非制造业PMI:销售价格指数:分行业/服务业 |
| `pmi020500` | 非制造业PMI:从业人员指数 |
| `pmi020501` | 非制造业PMI:从业人员指数:分行业/建筑业 |
| `pmi020502` | 非制造业PMI:从业人员指数:分行业/服务业 |
| `pmi020600` | 非制造业PMI:业务活动预期指数 |
| `pmi020601` | 非制造业PMI:业务活动预期指数:分行业/建筑业 |
| `pmi020602` | 非制造业PMI:业务活动预期指数:分行业/服务业 |
| `pmi020700` | 非制造业PMI:新出口订单 |
| `pmi020800` | 非制造业PMI:在手订单 |
| `pmi020900` | 非制造业PMI:存货 |
| `pmi021000` | 非制造业PMI:供应商配送时间 |
| `pmi030000` | 中国综合PMI:产出指数 |

---

### sf_month
**分类**: 宏观经济 > 国内宏观 > 金融 > 社会融资 > 社融增量（月度）-获取月度社会融资数据

**说明**: /数据接口/宏观经济/国内宏观/金融/社会融资/社融增量（月度）-获取月度社会融资数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_m` | string | 否 | 结束月份 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, inc_month, inc_cumval, stk_endval 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `m` | string | 否 | 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔 |
| `start_m` | string | 否 | 开始月份 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `inc_month` | (默认返回) |
| `inc_cumval` | (默认返回) |
| `stk_endval` | (默认返回) |

---

### cn_m
**分类**: 宏观经济 > 国内宏观 > 金融 > 货币供应量 > 货币供应量（月）-获取货币供应量之月度数据

**说明**: /数据接口/宏观经济/国内宏观/金融/货币供应量/货币供应量（月）-获取货币供应量之月度数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_m` | string | 否 | 结束月度 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: month, m0, m0_yoy, m0_mom, m1, m1_yoy, m1_mom, m2, m2_yoy, m2_mom 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `m` | string | 否 | 月度（202001表示，2020年1月） |
| `start_m` | string | 否 | 开始月度 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `month` | (默认返回) |
| `m0` | (默认返回) |
| `m0_yoy` | (默认返回) |
| `m0_mom` | (默认返回) |
| `m1` | (默认返回) |
| `m1_yoy` | (默认返回) |
| `m1_mom` | (默认返回) |
| `m2` | (默认返回) |
| `m2_yoy` | (默认返回) |
| `m2_mom` | (默认返回) |

---

### us_trycr
**分类**: 宏观经济 > 国际宏观 > 美国利率 > 国债实际收益率曲线利率-国债实际收益率曲线利率

**说明**: /数据接口/宏观经济/国际宏观/美国利率/国债实际收益率曲线利率-国债实际收益率曲线利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 （YYYYMMDD格式，下同） |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, y5, y7, y10, y20, y30 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `y5` | (默认返回) |
| `y7` | (默认返回) |
| `y10` | (默认返回) |
| `y20` | (默认返回) |
| `y30` | (默认返回) |

---

### us_tycr
**分类**: 宏观经济 > 国际宏观 > 美国利率 > 国债收益率曲线利率-获取美国每日国债收益率曲线利率

**说明**: /数据接口/宏观经济/国际宏观/美国利率/国债收益率曲线利率-获取美国每日国债收益率曲线利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 （YYYYMMDD格式，下同） |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, m1, m2, m3, m4, m6, y1, y2, y3, y5, y7, y10, y20, y30 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `m1` | (默认返回) |
| `m2` | (默认返回) |
| `m3` | (默认返回) |
| `m4` | (默认返回) |
| `m6` | (默认返回) |
| `y1` | (默认返回) |
| `y2` | (默认返回) |
| `y3` | (默认返回) |
| `y5` | (默认返回) |
| `y7` | (默认返回) |
| `y10` | (默认返回) |
| `y20` | (默认返回) |
| `y30` | (默认返回) |

---

### us_tltr
**分类**: 宏观经济 > 国际宏观 > 美国利率 > 国债长期利率-国债长期利率

**说明**: /数据接口/宏观经济/国际宏观/美国利率/国债长期利率-国债长期利率

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, ltc, cmt, e_factor 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `ltc` | (默认返回) |
| `cmt` | (默认返回) |
| `e_factor` | (默认返回) |

---

### us_trltr
**分类**: 宏观经济 > 国际宏观 > 美国利率 > 国债长期利率平均值-国债实际长期利率平均值

**说明**: /数据接口/宏观经济/国际宏观/美国利率/国债长期利率平均值-国债实际长期利率平均值

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, ltr_avg 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `ltr_avg` | (默认返回) |

---

### us_tbr
**分类**: 宏观经济 > 国际宏观 > 美国利率 > 短期国债利率-获取美国短期国债利率数据

**说明**: /数据接口/宏观经济/国际宏观/美国利率/短期国债利率-获取美国短期国债利率数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 日期 |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, w4_bd, w4_ce, w8_bd, w8_ce, w13_bd, w13_ce, w17_bd, w17_ce, w26_bd, w26_ce, w52_bd, w52_ce 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期(YYYYMMDD格式) |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `w4_bd` | (默认返回) |
| `w4_ce` | (默认返回) |
| `w8_bd` | (默认返回) |
| `w8_ce` | (默认返回) |
| `w13_bd` | (默认返回) |
| `w13_ce` | (默认返回) |
| `w17_bd` | (默认返回) |
| `w17_ce` | (默认返回) |
| `w26_bd` | (默认返回) |
| `w26_ce` | (默认返回) |
| `w52_bd` | (默认返回) |
| `w52_ce` | (默认返回) |

---

## 行业经济

共 8 个工具

### film_record
**分类**: 行业经济 > TMT行业 > 全国电影剧本备案数据-获取全国电影剧本备案的公示数据

**说明**: /数据接口/行业经济/TMT行业/全国电影剧本备案数据-获取全国电影剧本备案的公示数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公布日期 （至少输入一个参数，格式：YYYYMMDD，日期不连续，定期公布） |
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: rec_no, film_name, rec_org, script_writer, rec_result, rec_area, classified, date_range, ann_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `rec_no` | (默认返回) |
| `film_name` | (默认返回) |
| `rec_org` | (默认返回) |
| `script_writer` | (默认返回) |
| `rec_result` | (默认返回) |
| `rec_area` | (默认返回) |
| `classified` | (默认返回) |
| `date_range` | (默认返回) |
| `ann_date` | (默认返回) |

---

### teleplay_record
**分类**: 行业经济 > TMT行业 > 全国电视剧备案公示数据-获取2009年以来全国拍摄制作电视剧备案公示数据

**说明**: /数据接口/行业经济/TMT行业/全国电视剧备案公示数据-获取2009年以来全国拍摄制作电视剧备案公示数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 备案结束月份（YYYYMM） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: name, classify, types, org, report_date, license_key, episodes, shooting_date, prod_cycle, content, pro_opi, dept_opi, remarks 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 电视剧名称 |
| `org` | string | 否 | 备案机构 |
| `report_date` | string | 否 | 备案月份（YYYYMM） |
| `start_date` | string | 否 | 备案开始月份（YYYYMM） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `name` | (默认返回) |
| `classify` | (默认返回) |
| `types` | (默认返回) |
| `org` | (默认返回) |
| `report_date` | (默认返回) |
| `license_key` | (默认返回) |
| `episodes` | (默认返回) |
| `shooting_date` | (默认返回) |
| `prod_cycle` | (默认返回) |
| `content` | (默认返回) |
| `pro_opi` | (默认返回) |
| `dept_opi` | (默认返回) |
| `remarks` | (默认返回) |

---

### tmt_twincome
**分类**: 行业经济 > TMT行业 > 台湾电子产业月营收-获取台湾TMT电子产业领域各类产品月度营收数据。

**说明**: /数据接口/行业经济/TMT行业/台湾电子产业月营收-获取台湾TMT电子产业领域各类产品月度营收数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 报告期 |
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, item, op_income 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `item` | string | 是 | 产品代码 |
| `start_date` | string | 否 | 报告期开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `item` | (默认返回) |
| `op_income` | (默认返回) |

---

### tmt_twincomedetail
**分类**: 行业经济 > TMT行业 > 台湾电子产业月营收明细-获取台湾TMT行业上市公司各类产品月度营收情况。

**说明**: /数据接口/行业经济/TMT行业/台湾电子产业月营收明细-获取台湾TMT行业上市公司各类产品月度营收情况。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 否 | 报告期 |
| `end_date` | string | 否 | 报告期结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, item, symbol, op_income, consop_income 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `item` | string | 否 | 产品代码 |
| `source` | string | 否 | None |
| `start_date` | string | 否 | 报告期开始日期 |
| `symbol` | string | 否 | 公司代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `item` | (默认返回) |
| `symbol` | (默认返回) |
| `op_income` | (默认返回) |
| `consop_income` | (默认返回) |

---

### bo_cinema
**分类**: 行业经济 > TMT行业 > 影院日度票房-获取每日各影院的票房数据

**说明**: /数据接口/行业经济/TMT行业/影院日度票房-获取每日各影院的票房数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 是 | 日期(格式:YYYYMMDD) |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, c_name, aud_count, att_ratio, day_amount, day_showcount, avg_price, p_pc, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `c_name` | (默认返回) |
| `aud_count` | (默认返回) |
| `att_ratio` | (默认返回) |
| `day_amount` | (默认返回) |
| `day_showcount` | (默认返回) |
| `avg_price` | (默认返回) |
| `p_pc` | (默认返回) |
| `rank` | (默认返回) |

---

### bo_weekly
**分类**: 行业经济 > TMT行业 > 电影周度票房-获取周度票房数据

**说明**: /数据接口/行业经济/TMT行业/电影周度票房-获取周度票房数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 是 | 日期（每周一日期，格式YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, name, avg_price, week_amount, total, list_day, p_pc, wom_index, up_ratio, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `name` | (默认返回) |
| `avg_price` | (默认返回) |
| `week_amount` | (默认返回) |
| `total` | (默认返回) |
| `list_day` | (默认返回) |
| `p_pc` | (默认返回) |
| `wom_index` | (默认返回) |
| `up_ratio` | (默认返回) |
| `rank` | (默认返回) |

---

### bo_daily
**分类**: 行业经济 > TMT行业 > 电影日度票房-获取电影日度票房

**说明**: /数据接口/行业经济/TMT行业/电影日度票房-获取电影日度票房

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 是 | 日期 （格式YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, name, avg_price, day_amount, total, list_day, p_pc, wom_index, up_ratio, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `name` | (默认返回) |
| `avg_price` | (默认返回) |
| `day_amount` | (默认返回) |
| `total` | (默认返回) |
| `list_day` | (默认返回) |
| `p_pc` | (默认返回) |
| `wom_index` | (默认返回) |
| `up_ratio` | (默认返回) |
| `rank` | (默认返回) |

---

### bo_monthly
**分类**: 行业经济 > TMT行业 > 电影月度票房-获取电影月度票房数据

**说明**: /数据接口/行业经济/TMT行业/电影月度票房-获取电影月度票房数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 是 | 日期（每月1号，格式YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, name, list_date, avg_price, month_amount, list_day, p_pc, wom_index, m_ratio, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `name` | (默认返回) |
| `list_date` | (默认返回) |
| `avg_price` | (默认返回) |
| `month_amount` | (默认返回) |
| `list_day` | (默认返回) |
| `p_pc` | (默认返回) |
| `wom_index` | (默认返回) |
| `m_ratio` | (默认返回) |
| `rank` | (默认返回) |

---

## 外汇

共 1 个工具

### fx_obasic
**分类**: 外汇 > 外汇基础信息（海外）-获取海外外汇基础信息，目前只有FXCM交易商的数据

**说明**: /数据接口/外汇/外汇基础信息（海外）-获取海外外汇基础信息，目前只有FXCM交易商的数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `classify` | string | 否 | 分类 |
| `exchange` | string | 否 | 交易商 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, classify, exchange, min_unit, max_unit, pip, pip_cost, traget_spread, min_stop_distance, trading_hours, break_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `classify` | (默认返回) |
| `exchange` | (默认返回) |
| `min_unit` | (默认返回) |
| `max_unit` | (默认返回) |
| `pip` | (默认返回) |
| `pip_cost` | (默认返回) |
| `traget_spread` | (默认返回) |
| `min_stop_distance` | (默认返回) |
| `trading_hours` | (默认返回) |
| `break_time` | (默认返回) |

---

## 外汇数据

共 1 个工具

### fx_daily
**分类**: 外汇数据 > 外汇日线行情-获取外汇日线行情

**说明**: /数据接口/外汇数据/外汇日线行情-获取外汇日线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期（GMT） |
| `exchange` | string | 否 | 交易商，目前只有FXCM |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, bid_open, bid_close, bid_high, bid_low, ask_open, ask_close, ask_high, ask_low, tick_qty 额外可选字段:   exchange: 交易商 |
| `start_date` | string | 否 | 开始日期（GMT） |
| `trade_date` | string | 否 | 交易日期（GMT，日期是格林尼治时间，比北京时间晚一天） |
| `ts_code` | string | 否 | TS代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `bid_open` | (默认返回) |
| `bid_close` | (默认返回) |
| `bid_high` | (默认返回) |
| `bid_low` | (默认返回) |
| `ask_open` | (默认返回) |
| `ask_close` | (默认返回) |
| `ask_high` | (默认返回) |
| `ask_low` | (默认返回) |
| `tick_qty` | (默认返回) |
| `exchange` | 交易商 |

---

## 另类数据

共 4 个工具

### anns_d
**分类**: 另类数据 > 上市公司公告-获取全量公告数据，提供pdf下载URL

**说明**: /数据接口/另类数据/上市公司公告-获取全量公告数据，提供pdf下载URL

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期（yyyymmdd格式，下同） |
| `end_date` | string | 否 | 公告结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ann_date, ts_code, name, title, url 额外可选字段:   rec_time: 发布时间 |
| `start_date` | string | 否 | 公告开始日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ann_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `title` | (默认返回) |
| `url` | (默认返回) |
| `rec_time` | 发布时间 |

---

### ncov_global
**分类**: 另类数据 > 全球新冠疫情数据-获取全球新冠疫情数据，包括国家和地区

**说明**: /数据接口/另类数据/全球新冠疫情数据-获取全球新冠疫情数据，包括国家和地区

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `country` | string | 否 | 国家名称 |
| `end_date` | string | 否 | 结束日期（YYYYMMDD） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: publish_date, country, country_enname, province, province_short, province_enname, confirmed_num, confirmed_num_now, suspected_num, cured_num, dead_num, update_time 额外可选字段:   area_id: 地区代码 |
| `province` | string | 否 | 省份简称（北京、上海） |
| `publish_date` | string | 否 | 公布日期 |
| `start_date` | string | 否 | 开始日期（YYYYMMDD） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `publish_date` | (默认返回) |
| `country` | (默认返回) |
| `country_enname` | (默认返回) |
| `province` | (默认返回) |
| `province_short` | (默认返回) |
| `province_enname` | (默认返回) |
| `confirmed_num` | (默认返回) |
| `confirmed_num_now` | (默认返回) |
| `suspected_num` | (默认返回) |
| `cured_num` | (默认返回) |
| `dead_num` | (默认返回) |
| `update_time` | (默认返回) |
| `area_id` | 地区代码 |

---

### ncov_num
**分类**: 另类数据 > 新冠状肺炎感染人数-获取新冠状肺炎疫情感染人数统计数据

**说明**: /数据接口/另类数据/新冠状肺炎感染人数-获取新冠状肺炎疫情感染人数统计数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `ann_date` | string | 否 | 公告日期 |
| `area_name` | string | 否 | 地区名称 |
| `end_date` | string | 否 | 查询结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ann_date, area_name, parent_name, level, confirmed_num, suspected_num, confirmed_num_now, suspected_num_now, cured_num, dead_num 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `level` | string | 否 | 级别：2-中国内地，3-省级，4-地区市级别 |
| `start_date` | string | 否 | 查询开始日期 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ann_date` | (默认返回) |
| `area_name` | (默认返回) |
| `parent_name` | (默认返回) |
| `level` | (默认返回) |
| `confirmed_num` | (默认返回) |
| `suspected_num` | (默认返回) |
| `confirmed_num_now` | (默认返回) |
| `suspected_num_now` | (默认返回) |
| `cured_num` | (默认返回) |
| `dead_num` | (默认返回) |

---

### cctv_news
**分类**: 另类数据 > 新闻联播文字稿-获取新闻联播文字稿数据，数据开始于2017年。

**说明**: /数据接口/另类数据/新闻联播文字稿-获取新闻联播文字稿数据，数据开始于2017年。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `date` | string | 是 | 日期（输入格式：YYYYMMDD 比如：20181211） |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: date, title, content 额外可选字段:   （所有字段均为默认返回，无需指定） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `date` | (默认返回) |
| `title` | (默认返回) |
| `content` | (默认返回) |

---

## 大模型语料专题数据

共 6 个工具

### irm_qa_sh
**分类**: 大模型语料专题数据 > 上证e互动问答-获取上交所e互动董秘问答文本数据。上证e互动是由上海证券交易所建立、上海证券市场所有参与主体无偿使用的沟通平台,旨在引导和促进上市公司、投资者等各市场参与主体之间的信息沟通,构建集中、便捷的互动渠道。本接口数据记录了以上沟通问答的文本数据。

**说明**: /数据接口/大模型语料专题数据/上证e互动问答-获取上交所e互动董秘问答文本数据。上证e互动是由上海证券交易所建立、上海证券市场所有参与主体无偿使用的沟通平台,旨在引导和促进上市公司、投资者等各市场参与主体之间的信息沟通,构建集中、便捷的互动渠道。本接口数据记录了以上沟通问答的文本数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, q, a, pub_time 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `pub_date` | string | 否 | 发布结束日期(格式：2025-06-03 18:43:23) |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `q` | (默认返回) |
| `a` | (默认返回) |
| `pub_time` | (默认返回) |

---

### research_report
**分类**: 大模型语料专题数据 > 券商研究报告-获取券商研究报告-个股、行业等，历史数据从20170101开始提供，增量每天两次更新

**说明**: /数据接口/大模型语料专题数据/券商研究报告-获取券商研究报告-个股、行业等，历史数据从20170101开始提供，增量每天两次更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 研报结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, abstr, title, report_type, author, name, ts_code, inst_csname, ind_name, url 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ind_name` | string | 否 | 行业名称 |
| `inst_csname` | string | 否 | 券商名称 |
| `report_type` | string | 否 | 研报类别：个股研报/行业研报 |
| `start_date` | string | 否 | 研报开始日期 |
| `trade_date` | string | 否 | 研报日期（格式：YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `abstr` | (默认返回) |
| `title` | (默认返回) |
| `report_type` | (默认返回) |
| `author` | (默认返回) |
| `name` | (默认返回) |
| `ts_code` | (默认返回) |
| `inst_csname` | (默认返回) |
| `ind_name` | (默认返回) |
| `url` | (默认返回) |

---

### npr
**分类**: 大模型语料专题数据 > 国家政策库-获取国家行政机关公开披露的各类法规、条例政策、批复、通知等文本数据。

**说明**: /数据接口/大模型语料专题数据/国家政策库-获取国家行政机关公开披露的各类法规、条例政策、批复、通知等文本数据。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 发布结束时间 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: pubtime, title, pcode, puborg, ptype 额外可选字段:   url: 政策文件url   content_html: 正文内容 |
| `org` | string | 否 | 发布机构 |
| `ptype` | string | 否 | 类型 |
| `start_date` | string | 否 | 发布开始时间 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `pubtime` | (默认返回) |
| `title` | (默认返回) |
| `pcode` | (默认返回) |
| `puborg` | (默认返回) |
| `ptype` | (默认返回) |
| `url` | 政策文件url |
| `content_html` | 正文内容 |

---

### news
**分类**: 大模型语料专题数据 > 新闻快讯（短讯）-获取主流新闻网站的快讯新闻数据,提供超过6年以上历史新闻。

**说明**: /数据接口/大模型语料专题数据/新闻快讯（短讯）-获取主流新闻网站的快讯新闻数据,提供超过6年以上历史新闻。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 是 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: datetime, content, title 额外可选字段:   channels: 分类 |
| `src` | string | 是 | 新闻来源 见下表 |
| `start_date` | string | 是 | 开始日期(格式：2018-11-20 09:00:00） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `datetime` | (默认返回) |
| `content` | (默认返回) |
| `title` | (默认返回) |
| `channels` | 分类 |

---

### major_news
**分类**: 大模型语料专题数据 > 新闻通讯（长篇）-获取长篇通讯信息，覆盖主要新闻资讯网站，提供超过8年历史新闻。

**说明**: /数据接口/大模型语料专题数据/新闻通讯（长篇）-获取长篇通讯信息，覆盖主要新闻资讯网站，提供超过8年历史新闻。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 新闻发布结束时间，e.g. 2018-11-22 00:00:00 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: title, pub_time, src 额外可选字段:   content: 内容 (默认不显示，需要在fields里指定) |
| `src` | string | 否 | 新闻来源（新华网、凤凰财经、同花顺、新浪财经、华尔街见闻、中证网、财新网、第一财经、财联社） |
| `start_date` | string | 否 | 新闻发布开始时间，e.g. 2018-11-21 00:00:00 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `title` | (默认返回) |
| `pub_time` | (默认返回) |
| `src` | (默认返回) |
| `content` | 内容 (默认不显示，需要在fields里指定) |

---

### irm_qa_sz
**分类**: 大模型语料专题数据 > 深证易互动问答-互动易是由深交所官方推出,供投资者与上市公司直接沟通的平台,一站式公司资讯汇集,提供第一手的互动问答、投资者关系信息、公司声音等内容。

**说明**: /数据接口/大模型语料专题数据/深证易互动问答-互动易是由深交所官方推出,供投资者与上市公司直接沟通的平台,一站式公司资讯汇集,提供第一手的互动问答、投资者关系信息、公司声音等内容。

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, name, trade_date, q, a, pub_time, industry 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `pub_date` | string | 否 | 发布结束日期(格式：2025-06-03 18:43:23) |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期（格式YYYYMMDD，下同） |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `name` | (默认返回) |
| `trade_date` | (默认返回) |
| `q` | (默认返回) |
| `a` | (默认返回) |
| `pub_time` | (默认返回) |
| `industry` | (默认返回) |

---

## 现货

共 1 个工具

### sge_basic
**分类**: 现货 > 上海黄金基础信息-获取上海黄金交易所现货合约基础信息

**说明**: /数据接口/现货/上海黄金基础信息-获取上海黄金交易所现货合约基础信息

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, ts_name, trade_type, t_unit, p_unit, min_change, price_limit, min_vol, max_vol, trade_mode, margin_rate, liq_rate, trade_time, list_date 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `ts_code` | string | 否 | 合约代码 （支持多个，逗号分隔，不输入为获取全部） |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `ts_name` | (默认返回) |
| `trade_type` | (默认返回) |
| `t_unit` | (默认返回) |
| `p_unit` | (默认返回) |
| `min_change` | (默认返回) |
| `price_limit` | (默认返回) |
| `min_vol` | (默认返回) |
| `max_vol` | (默认返回) |
| `trade_mode` | (默认返回) |
| `margin_rate` | (默认返回) |
| `liq_rate` | (默认返回) |
| `trade_time` | (默认返回) |
| `list_date` | (默认返回) |

---

## 现货数据

共 1 个工具

### sge_daily
**分类**: 现货数据 > 上海黄金现货日行情-获取上海黄金交易所现货合约日线行情

**说明**: /数据接口/现货数据/上海黄金现货日行情-获取上海黄金交易所现货合约日线行情

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: ts_code, trade_date, close, open, high, low, price_avg, change, pct_change, vol, amount, oi, settle_vol, settle_dire 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 合约代码，可通过[基础信息](https://tushare.pro/document/2?doc_id=284)获得 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `ts_code` | (默认返回) |
| `trade_date` | (默认返回) |
| `close` | (默认返回) |
| `open` | (默认返回) |
| `high` | (默认返回) |
| `low` | (默认返回) |
| `price_avg` | (默认返回) |
| `change` | (默认返回) |
| `pct_change` | (默认返回) |
| `vol` | (默认返回) |
| `amount` | (默认返回) |
| `oi` | (默认返回) |
| `settle_vol` | (默认返回) |
| `settle_dire` | (默认返回) |

---

## 财富管理

共 1 个工具

### fund_sales_vol
**分类**: 财富管理 > 基金销售行业数据 > 销售机构公募基金销售保有规模-获取销售机构公募基金销售保有规模数据，本数据从2021年Q1开始公布，季度更新

**说明**: /数据接口/财富管理/基金销售行业数据/销售机构公募基金销售保有规模-获取销售机构公募基金销售保有规模数据，本数据从2021年Q1开始公布，季度更新

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: year, quarter, inst_name, fund_scale, scale, rank 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `name` | string | 否 | 机构名称 |
| `quarter` | string | 否 | 季度 |
| `year` | string | 否 | 年度 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `year` | (默认返回) |
| `quarter` | (默认返回) |
| `inst_name` | (默认返回) |
| `fund_scale` | (默认返回) |
| `scale` | (默认返回) |
| `rank` | (默认返回) |

---

## 小佩数据

共 2 个工具

### stock_vx
**分类**: 小佩数据 > 估值因子-小沛估值因子

**说明**: /数据接口/小佩数据/估值因子-小沛估值因子

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, level1, level2, vx_life_v_l4, vx_3excellent_v_l4, vx_past_5q_avg_l4, vx_grow_worse_v_l4, vx_life_v_l8, vx_3excellent_v_l8, vx_past_5q_avg_l8, vx_grow_worse_v_l8, vxx, vs, vz11, vz24, vz_lms 额外可选字段:   （所有字段... |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `level1` | (默认返回) |
| `level2` | (默认返回) |
| `vx_life_v_l4` | (默认返回) |
| `vx_3excellent_v_l4` | (默认返回) |
| `vx_past_5q_avg_l4` | (默认返回) |
| `vx_grow_worse_v_l4` | (默认返回) |
| `vx_life_v_l8` | (默认返回) |
| `vx_3excellent_v_l8` | (默认返回) |
| `vx_past_5q_avg_l8` | (默认返回) |
| `vx_grow_worse_v_l8` | (默认返回) |
| `vxx` | (默认返回) |
| `vs` | (默认返回) |
| `vz11` | (默认返回) |
| `vz24` | (默认返回) |
| `vz_lms` | (默认返回) |

---

### stock_mx
**分类**: 小佩数据 > 动能因子-获取小佩数据动量因子数据，可以获取股票动能评级数据，包括最新及过去历史数据

**说明**: /数据接口/小佩数据/动能因子-获取小佩数据动量因子数据，可以获取股票动能评级数据，包括最新及过去历史数据

### 输入参数

| 参数名 | 类型 | 是否必填 | 说明 |
|--------|------|----------|------|
| `end_date` | string | 否 | 结束日期 |
| `fields` | array | 否 | 指定返回字段，不传则返回默认字段。 默认字段: trade_date, ts_code, mx_grade, com_stock, evd_v, zt_sum_z, wma250_z 额外可选字段:   （所有字段均为默认返回，无需指定） |
| `start_date` | string | 否 | 开始日期 |
| `trade_date` | string | 否 | 交易日期 |
| `ts_code` | string | 否 | 股票代码 |

### 输出字段

| 字段名 | 说明 |
|--------|------|
| `trade_date` | (默认返回) |
| `ts_code` | (默认返回) |
| `mx_grade` | (默认返回) |
| `com_stock` | (默认返回) |
| `evd_v` | (默认返回) |
| `zt_sum_z` | (默认返回) |
| `wma250_z` | (默认返回) |

---
