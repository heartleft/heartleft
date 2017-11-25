from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

db = SQLAlchemy()

bootStrap = Bootstrap()

loginManger = LoginManager()
loginManger.session_protection = 'strong'
loginManger.login_view = 'auth.login'
