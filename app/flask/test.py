from flask import Flask

application = Flask(__name__)

# テスト用
@application.route('/')
def index():
    return '<h1>Hello Flask</h1>'

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')