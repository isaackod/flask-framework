
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    QUANDL_KEY = os.environ.get('QUANDL_KEY') or "E5Gd2wZn4vXY4a4sZu4T"
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['isaac.khader@gmail.com','isaacdebug@gmail.com']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')