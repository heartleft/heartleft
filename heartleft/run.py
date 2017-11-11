from heartleft.admin.api.urls import admin_mgr, file_mgr
from heartleft.admin.service.server import BlogServer
from flask_script import Manager


def main():
    server = BlogServer(import_name="heartleft",
                        template_folder='admin/templates',
                        static_folder='admin/static')

    server.register_blueprint(admin_mgr)
    server.register_blueprint(file_mgr)
    # TODO(zpzhou): need setup log
    manager = Manager(server)
    manager.run()
