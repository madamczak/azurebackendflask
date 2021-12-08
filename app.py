from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/msg')
def hello_worldmsg():
    return 'Hello World MSG!'


if __name__ == '__main__':
    app.run()
