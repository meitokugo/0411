# Session 数据存储在服务器上，会话是客户端登录到服务器并注销服务器的事件间隔，需要在该会话中保持的数据会存储在服务器的临时目录中。
# 为每个客户端的会话分配会话ID，会话数据存储在cookie的顶部，服务器以加密方式对其签名，同时需要定义一个SECRET_KEY，Session 也是一个字典对象，包含会话·变量和关联值的键值对。

# 设置一个会话
from flask import Flask, session, redirect, url_for, escape, request
from flask import make_response
from flask import render_template
Session['username'] = 'admin'

# 释放一个变量
session.pop('username', None)


# 完整实例


# 运行应用程序并访问主页。（确保设置应用程序的secret_key）
app = Flask(__name__)

app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'

# url'/'只是提示用户登录


@app.route('/')
def index():

    if 'username' in session:

        username = session['username']

        return '登录用户名是:' + username + '<br>' + \

        "<b><a href = '/logout'>点击这里注销</a></b>"

    return "you are not logged in， <br><a href = '/login'></b>" + \

    "点击这里登录</b></a>"


# 当用户浏览到“/login”login()视图函数时，因为它是通过GET方法调用的，所以将打开一个登录表单。
# 表单发送回'/login'，现在会话变量已设置。应用程序重定向到'/'。此时会话变量'username'被找到。
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        session['username'] = request.form['username']

        return redirect(url_for('index'))

    return '''

   <form action = "" method = "post">

      <p><input type="text" name="username"/></p>

      <p><input type="submit" value ="登录"/></p>

   </form>

   '''

# 应用程序还包含一个logout()视图函数，它会弹出'username'会话变量。因此，'/' URL再次显示开始页面。


@app.route('/logout')
def logout():

    # remove the username from the session if it is there

    session.pop('username', None)

    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(debug=True)
