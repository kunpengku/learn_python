

from flask_script import Manager
from flask import Flask

app = Flask(__name__)
# configure your app

manager = Manager(app)


@manager.command
def helloxxx():
    print 'make a argg'

@manager.command
def h(name):
    print 'hello', name

if __name__ == "__main__":
    manager.run()
