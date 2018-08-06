from flask import Flask,url_for,redirect,render_template
from url2list import ListConverter

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
