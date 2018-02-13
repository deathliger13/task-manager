from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # for debug in PyCharm
    # app.debug = False
    # app.use_debugger = True
    # app.use_reloader = True
    app.debug = True

    bootstrap.init_app(app)
    db.init_app(app)


    # import blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # api
    # from app.api.v1 import api as api_v1_blueprint
    # app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app