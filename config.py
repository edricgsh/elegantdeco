# config.py
import os

class Config(object):

    SECRET_KEY = 'Dtranq12!pal1kar1@!@'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/konstantinoszigogiannis/Documents/myapps/elegantdeco/db/elegantdeco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True #for development. Change to false for production
    #SQLALCHEMY_ECHO = True #for development. Change to false for production
