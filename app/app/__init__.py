import logging
from logging.config import dictConfig
from flask import Flask

dictConfig({
    'version': 1,
    'formatters': {
        'file': {
            'format': '[%(asctime)s] [%(levelname)s] : %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'filename': '/home/app/app.log'
        }
    },
    'root': {
        'level': 'WARN',
        'handlers': ['file']
    },
})


def create_app(config_mode='production'):
    app = Flask(__name__, instance_relative_config=True)

    if config_mode != 'production':
        # 本番以外のログ設定はtest_config.pyを指定
        config_object = 'test_config.' + config_mode
        app.config.from_object(config_object)
        logging.basicConfig(level=logging.DEBUG)

    from app.views import index, info
    app.register_blueprint(index.bp)
    app.register_blueprint(info.bp)

    return app