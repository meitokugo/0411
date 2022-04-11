from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_earth():
    return 'Hello earth'


if __name__ == '__main__':
    app.run()
#app.run(host, port, debug, options)
