from heartleft.admin.api.urls import admin_mgr
from heartleft.admin.service.server import BlogServer

server = BlogServer(__name__, template_folder='admin/templates')
server.register_blueprint(admin_mgr)
server.run(host='0.0.0.0', port=80)
