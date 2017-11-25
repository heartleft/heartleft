
class AppConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:example@localhost:3306/test?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'hard to guess string'
    DEBUG = False
    TESTING = False
