#app/__init.py__
import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from .site import site as site_blueprint
app.register_blueprint(site_blueprint)
