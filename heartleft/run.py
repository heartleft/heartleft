from heartleft.server import app
from flask_script import Manager, Server

manager = Manager(app)
manager.add_command("runserver", Server('0.0.0.0', port=80))


# app.run(host='0.0.0.0', port=80, debug='true')

def main():
    manager.run()
