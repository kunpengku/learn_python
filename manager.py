

from flask_script import Manager

from flask import Flask

app = Flask(__name__)
#from yy import app

manager = Manager(app)

@manager.command
def hellox():
    print 'hello'


@manager.option('-n', dest='name')
@manager.option('-a', dest='age')
def hello2(name, age):
    print 'hello 2', name, age

if __name__ == '__main__':
    manager.run()
