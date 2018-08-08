from flask import Flask,url_for,redirect,render_template
from url2list import ListConverter
from jsonify_resp import JSONResponse

app = Flask(__name__)

#将自定义的响应类赋值给当前的app，从而替换响应类
app.response_class=JSONResponse

#将新建的转换器类型加入内建类型中
app.url_map.converters['list']=ListConverter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return '分隔符: {} {}'.format('+',page_names)

#url_for自定义
@app.route('/list2/name/')
def list2():
    return url_for('list2',id=6,next='/')
    #/list2/name/?id=6&next=%2F

#redirect
@app.route('/search/<keyword>/')
def search(keyword):
    if (keyword=='hello'):
        return redirect(url_for('index'))
    else:
        return 'hello {}'.format(keyword)
#jsonify
@app.route('/json_resp/<id>/')
def json_resp(id):
    return {'id':id}

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/item/<int:id>/')
def item(id):
    if (id==520):
        return redirect(url_for('dailyLife'))
    return ('item {}'.format(id))

@app.route('/secret/')
def secret():
    abort(404)
    print('不会执行到这里！！！')

if __name__ == '__main__':
    app.run(debug=True)
