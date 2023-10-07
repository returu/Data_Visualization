import tushare as ts

def get_data(stock_code):

    # 初始化pro接口
    # 或者使用自己的token：pro = ts.pro_api('your token')
    pro = ts.pro_api()

    # 通过股票代码获取股票最近的数据
    df = pro.daily(ts_code=stock_code)
    # 获取最近30天的股票数据并正序排列
    data_30 = df[:30].iloc[::-1]

    # 统计近30个交易日的涨跌数据
    data_30['rise'] = data_30['change'] > 0 # 涨
    data_30['fall'] = data_30['change'] < 0 # 跌
    rise_fall_count = data_30[['rise','fall']].sum().values.tolist() # 统计近30交易日的涨跌次数,并转为列表格式

    # 获取近30交易日的价格变化
    price_change = data_30['change'].values.tolist()

    # 获取近30交易日的收盘价
    close_value = data_30['close'].values.tolist()

    # 获取近30交易日的成交量
    volume = data_30['vol'].values.tolist()

    # 获取近30交易日的成交额
    amount = data_30['amount'].values.tolist()

    # 获取时间序列，将其作为x轴数据
    x_index = data_30['trade_date'].values.tolist()

    # 存放echarts需要的数据内容
    data_return = {}
    # 以下为将处理好的数据加入字典
    data_return['x_index'] = x_index 
    data_return['close_value'] = close_value
    data_return['price_change'] = price_change
    data_return['volume'] = volume
    data_return['amount'] = amount
    data_return['rise_fall_count'] = rise_fall_count
    return data_return

def get_name(stock_code):
    pro=ts.pro_api()
    data = pro.stock_basic(fields='ts_code,name')
    company_name = data[data['ts_code'] == stock_code]['name'].tolist()[0]
    info_return = {}
    info_return['company_name'] = company_name
    info_return['company_code'] = stock_code
    return info_return

