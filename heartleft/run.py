#!/usr/bin/env python

from flask.ext.bootstrap import Bootstrap
from urls import m_hello_world
from myapp import app

app.register_blueprint(m_hello_world)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)

app.run(host='0.0.0.0', port=80, debug='true')
