from flask import Blueprint
from heartleft.app.views.index import views as index_views
from heartleft.app.views.auth import views as auth_views

index_blueprint = Blueprint('index', __name__)
index_blueprint.add_url_rule('/', 'index', index_views.index, methods=['GET', 'POST'])

auth_blueprint = Blueprint('auth', __name__)
auth_blueprint.add_url_rule('/login', 'login', auth_views.login, methods=['GET', 'POST'])
auth_blueprint.add_url_rule('/logout', 'logout', auth_views.login, methods=['GET', 'POST'])
