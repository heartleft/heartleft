from flask import Flask
from heartleft.urls import m_hello_world
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


class HeartLeft(Flask):
    def __init__(self, import_name, static_path=None, static_url_path=None,
                 static_folder='static', template_folder='templates',
                 instance_path=None, instance_relative_config=False):
        super(HeartLeft, self).__init__(import_name, static_path, static_url_path,
                                        static_folder, template_folder,
                                        instance_path, instance_relative_config)
        self._setup()

    def _init_config(self):
        self.config['SECRET_KEY'] = 'hard to guess string'
        self.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@localhost:3306/test?charset=utf8'
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    def _setup(self):
        self._init_config()
        self._init_extend()
        self.register_blueprint(m_hello_world)

    def _init_extend(self):
        self.bootstrap = Bootstrap(self)
        self.db = SQLAlchemy(self)


app = HeartLeft(__name__,static_folder="/usr/local/heartleft")
db = app.db
bootstrap = app.bootstrap
