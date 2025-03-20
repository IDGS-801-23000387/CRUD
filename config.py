import os
from sqlalchemy import create_engine #type: ignore
import urllib

class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_NAME='FlaskSesion'

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root1234@127.0.0.1/flaskDB'
    SQLALCHEMY_TRACK_MODIFICATIONS=False