# get方法以未加密的形式将数据发送到服务器，
# head和get方法相同，但是没有响应体
# post 将html表单数据发送到服务器，post方法接受的数据不由服务器缓存
# put，用上传的内容替换目标资源的所有表示
# delete用来删除由url给出的目标资源的所有当前表示


from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()
