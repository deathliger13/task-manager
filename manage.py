import os
from flask_script import Manager, Server


from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)


@manager.command
def hello():
    print('hello')


@manager.command
def create():
    db.create_all()
    db.session.commit()


# manager.add_command("hello", hello())
manager.add_command("run", Server(host="127.0.0.1", port=8888))

if __name__ == "__main__":
    manager.run()