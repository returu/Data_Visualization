from flask import Flask,render_template,request
# 从getdata.py中导入上一步编写的两个函数方法
from getdata import get_data,get_name

# 创建Flask对象
app = Flask(__name__)

# 创建Flask路由
# 通过GET或POST请求方式访问 http://127.0.0.1:5000/ 时调用下面定义的stock_query()函数
@app.route('/',methods=['GET','POST'])
def stock_query():
    """
    首先获取输入框中输入的股票代码，
    然后将调用get_data,get_name两个函数方法后得到的数据分别返回给data_return、info_return变量，
    最后上述变量传入index.html中使用
    """
    if request.method=='POST':
        # 使用POST方法时，即在页面输入框中输入股票代码时，
        # 首先获取输入的股票代码，然后通过函数方法返回该股票的具体信息
        stock_code = request.form.get('name')
        data_return = get_data(stock_code)
        info_return = get_name(stock_code)
        return render_template('index.html',data_return=data_return,info_return=info_return)
    else:
        # 默认查询股票代码为“000001.SZ”
        data_return = get_data('000001.SZ')
        info_return = get_name('000001.SZ')
        return render_template('index.html',data_return=data_return,info_return=info_return)

if  __name__  ==  '__main__':
    app.run(debug = True)