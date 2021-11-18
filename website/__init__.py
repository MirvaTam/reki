from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__) ## perustaa koko sovelluksen

    app.config['SECRET_KEY'] = 'dingusdangus'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

## Timin juttuja alla
##def create_database(app):
##    if not path.exists('website/' + DB_NAME):
##        db.create_all(app=app)
##        print('Created database')

##from .models import User, Reseptit

#create_database(app)