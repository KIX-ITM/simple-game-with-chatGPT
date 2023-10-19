import logging
from logging.config import dictConfig
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_envvar('APP_CONFIG_FILE_PATH')
    logging.basicConfig(filename='/home/app/app.log', level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] : %(message)s')

    from app.views import index, info
    app.register_blueprint(index.bp)
    app.register_blueprint(info.bp)
    app.logger.info('This is an info message.')

    return app