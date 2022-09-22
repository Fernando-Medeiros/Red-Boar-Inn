from flask_pymongo import PyMongo
from flask_login import LoginManager


mongo = PyMongo()
mongo_update = PyMongo()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'alert-info'


def development(app):
    pass


def production(app):
    
    login_manager.init_app(app)

    mongo.init_app(app)
    mongo_update.init_app(app, uri=app.config.get("MONGO_URI_UPDATES", None))

    app.db = mongo.db
    app.db_update = mongo_update.db
 

def init_app(app):
    env = app.config.ENV

    if env == "development" or env == "testing":
        development(app)

    production(app)
    