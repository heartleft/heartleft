from flask import Flask
from .config import AppConfig
from .extends import db, bootStrap, loginManger
from .views import auth_blueprint, index_blueprint


class BlogApp(Flask):
    @classmethod
    def factory(cls, **config_items):
        return cls(**config_items)

    def __init__(self, **config_items):
        import_name = config_items.get("import_name") or __name__
        static_path = config_items.get("static_path")
        static_url_path = config_items.get("static_url_path")
        static_folder = config_items.get("static_folder") or "static"
        template_folder = config_items.get("template_folder") or "templates"
        instance_path = config_items.get("instance_path")
        instance_relative_config = config_items.get("instance_relative_config")
        # root_path = config_items.get("root_path")

        super(BlogApp, self).__init__(import_name=import_name, static_path=static_path,
                                      static_url_path=static_url_path,
                                      static_folder=static_folder, template_folder=template_folder,
                                      instance_path=instance_path,
                                      instance_relative_config=instance_relative_config)

        self.config.from_object(AppConfig)
        self.register_urls()
        self.init_extends()

    def register_urls(self):
        self.register_blueprint(auth_blueprint, url_prefix='/auth')
        self.register_blueprint(index_blueprint)

    def init_extends(self):
        db.init_app(self)
        loginManger.init_app(self)
        bootStrap.init_app(self)


app = BlogApp.factory()
