import sqlite3
from flask import g
from flask import Flask, redirect, url_for, render_template, request

DATABASE = '/path/to/database.db'


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# 销毁函数是一定会被执行的。即使请求前处理器执行失败或根本没有执行， 销毁函数也会被执行。因此，我们必须保证在关闭数据库连接之前数据库连接是存在 的。


# 按需查询，
def get_connection():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db


# 查询语句
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


# 只需要单一结果的用法：
user = query_db('select * from users where username = ?',
                [the_username], one=True)
if user is None:
    print 'No such user'
else:
    print the_username, 'has the id', user['user_id']
