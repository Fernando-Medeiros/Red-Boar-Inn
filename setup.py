from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

mongo_main = PyMongo()
mongo_update = PyMongo()
database_sql = SQLAlchemy()

admin = Admin()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'alert-info'


def development(app):
    pass


def production(app):
    
    admin.init_app(app)
    mongo_main.init_app(app)
    mongo_update.init_app(app, uri=app.config.get("MONGO_URI_UPDATES", None))
    database_sql.init_app(app)
    login_manager.init_app(app) 

    Migrate(app, database_sql)


def context(app):
    app.db = mongo_main.db
    app.db_update = mongo_update.db
    app.db_sql = database_sql


def init_app(app):

    env = app.config.ENV    

    if env == "development" or env == "testing":
        development(app)

    production(app)
    
    context(app)