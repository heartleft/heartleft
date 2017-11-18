from flask import Blueprint
import views

m_hello_world = Blueprint('HelloWorld', __name__)
m_hello_world.add_url_rule('/', 'index', views.index, methods=['GET', 'POST'])
m_hello_world.add_url_rule('/login', 'login', views.login, methods=['GET', 'POST'])
