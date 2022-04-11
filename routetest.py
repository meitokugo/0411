from flask import Flask
app = Flask(__name__)

# int型作为参数


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'blog Number %d' % postID

# 浮点数作为参数


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


if __name__ == '__main__':
    app.run()
