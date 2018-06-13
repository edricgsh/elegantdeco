#app/__init.py__
import os

# third-party imports
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from instance.config import app_config

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)

    from app import models



    from .site import site as site_blueprint
    app.register_blueprint(site_blueprint)


    return app
