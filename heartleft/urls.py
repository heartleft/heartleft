from flask import Blueprint
import modules


m_hello_world = Blueprint('HelloWorld', __name__)
m_hello_world.add_url_rule('/', 'index', modules.index, methods=['GET', 'POST'])
m_hello_world.add_url_rule('/login', 'login', modules.login, methods=['GET', 'POST'])

