from flask import Blueprint
from heartleft.admin.modules import admin


admin_mgr = Blueprint('admin', __name__)
admin_mgr.add_url_rule('/', view_func=admin.index)
admin_mgr.add_url_rule('/', view_func=admin.hello_world)
admin_mgr.add_url_rule('/', view_func=admin.hello_world)
