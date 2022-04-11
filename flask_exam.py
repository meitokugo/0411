# flask处理Cookies
from flask import Flask, make_response, request  # 注意需导入 make_response
from http.cookiejar import Cookie


# Cookie以文本形式存储在客户端的计算机上，目的是记住和跟踪客户相关的数据，从而得到更好的用户体验以及网站统计信息。
# Request对象，包含Cookie的属性，cookie变量对应字典对象，客户端已传输。cookie还保持网站到期事件路径和域名

# 处理步骤  1.设置cookie，
resp = make_response("success")   # 设置响应体
resp.set_cookie("w3cshool", "w3cshool", max_age=3600)

# 获取cookie，返回字典
cookie_1 = request.cookie.get("w3cshool")

# 删除cookie， 这里的删除只是让cookie过期，并不是直接删除cookie.删除cookie，通过delete_cookie()的方式， 里面是cookie的名字
resp = make_response("del success")
resp.delet_cookie("w3cshool")


# 完整实例

app = Flask(__name__)


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool", max_age=3600)
    return resp


@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/delete_cookies")
def delete_cookie():
    resp.delete_cookie("w3cshool")

    return resp


if __name__ == '__main__':
    app.run()
