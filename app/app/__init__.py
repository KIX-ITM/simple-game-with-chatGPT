import logging
from flask import Flask


def create_app(config_mode=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_mode is None:
        # 本番の設定ファイルは環境変数で指定
        app.config.from_envvar('APP_CONFIG_FILE_PATH')
        logging.basicConfig(level=logging.INFO)
    else:
        # それ以外の設定はconfig.pyを指定
        config_object = 'test_config.' + config_mode
        app.config.from_object(config_object)
        logging.basicConfig(level=logging.DEBUG)

    from app.views import index
    app.register_blueprint(index.bp)

    return app