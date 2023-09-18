from flask import Flask

application = Flask(__name__)

# テスト用
@application.route('/')
def index():
    return '<h1>Hello Flask</h1>'