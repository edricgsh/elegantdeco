#app/__init.py__
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"
migrate = Migrate(app, db)

from app import models

from .site import site as site_blueprint
app.register_blueprint(site_blueprint)

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')


from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

