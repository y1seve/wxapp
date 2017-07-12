from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from webapp import create_app
from webapp.models import db, User, Category, Product

app = create_app('webapp.config.DevConfig')

#initialize Migrate object
migrate = Migrate(app)

#initialize Flask Script
manager = Manager(app)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Category=Category, Product=Product)

if __name__ == '__main__':
    manager.run()
