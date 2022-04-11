# redirect()函数。调用时，它返回一个响应对象，并将用户重定向到具有指定状态代码的另一个目标位置。
from flask import Flask, redirect, url_for, render_template, request
Flask.redirect(location, statuscode, response)
# location参数是应该重定向响应的URL。
# statuscode发送到浏览器标头，默认为302。
# response参数用于实例化响应。

# 登录尝试失败后，再次显示登录界面实例

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and
    request.form['username'] == 'admin':
        return redirect(url_for('success'))
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run()
