from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


mongo = PyMongo()
mongo_update = PyMongo()

db_sql = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'alert-info'


def development(app):
    pass


def production(app):

    login_manager.init_app(app) 

    Migrate(app, db_sql)


def init_app(app):

    env = app.config.ENV


    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "@jinja {{env.DATABASE_URL_SQL}}"
  
  
    mongo.init_app(app)
    mongo_update.init_app(app, uri=app.config.get("MONGO_URI_UPDATES", None))
    db_sql.init_app(app)


    app.db = mongo.db
    app.db_update = mongo_update.db
    app.db_sql = db_sql


    if env == "development" or env == "testing":
        development(app)

    production(app)
    