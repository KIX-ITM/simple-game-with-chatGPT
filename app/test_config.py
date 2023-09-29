# 参考：https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/config.html?highlight=app.debug
class Dev:
    DEBUG = True
    SECRET_KEY = 'develop'


class Test:
    TESTING = True
    SECRET_KEY = 'testing'
