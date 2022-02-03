from os import environ
import os

class Config:
    SECRET_KEY = os.urandom(8)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
