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
        'level': 'DEBUG',
        'handlers': ['file']
    },
})


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_envvar('APP_CONFIG_FILE_PATH')

    from app.views import index, info
    app.register_blueprint(index.bp)
    app.register_blueprint(info.bp)

    return app