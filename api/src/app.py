import logging.config
from logging import getLogger
import os
from conf.flask_conf import get_flask_env_conf

from flask import Flask

from .api.convert import convert


url_prefix = '/pdf2html'


def create_app(logging_conf_path='../conf/logging.conf'):
    """アプリインスタンス作成

    Parameters
    ----------
    logging_conf_path : str, optional, default '../conf/logging.conf'
        ログ設定ファイルパス

    Returns
    -------
    flask.app.Flask
        アプリインスタンス
    """
    app = Flask(__name__)

    app.config.from_object(get_flask_env_conf())
    if os.getenv(key='FLASK_CONFIG', default='production') == "development":
        print("Development")

    logging.config.fileConfig(logging_conf_path)
    app.logger = getLogger(__name__)

    app.register_blueprint(convert, url_prefix=url_prefix)

    return app
