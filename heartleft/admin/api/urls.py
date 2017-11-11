from flask import Blueprint
from heartleft.admin.modules import admin


admin_mgr = Blueprint('admin', __name__)
admin_mgr.add_url_rule('/', view_func=admin.index)
admin_mgr.add_url_rule('/helloworld', view_func=admin.hello_world)


file_mgr = Blueprint('file', __name__)
file_mgr.add_url_rule('/<file_path>', view_func=admin.get_file)
