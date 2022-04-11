from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'hello admin'


@app.route('/guest/<name>')
def hello_guest(name):
    return 'Hello %s!' % name


@app.route('/user/<gold>')
def hello_user(gold):
    if gold == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_gust', guest=gold))


if __name__ == '__main__':
    app.run()
