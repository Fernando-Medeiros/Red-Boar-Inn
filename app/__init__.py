from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from mvc_flask import FlaskMVC
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app__ = Flask(__name__)
app__.config['SECRET_KEY'] = '1ca8b0ad13d4197ca746bcb13c2169b2'
app__.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_database.db'

database__ = SQLAlchemy(app__)
mvc__ = FlaskMVC()

bcrypt__ = Bcrypt(app__)
login_manager__ = LoginManager(app__)

login_manager__.login_view = 'login.login'
login_manager__.login_message_category = 'alert-info'


def init_ext_app():
    mvc__.init_app(app__)
    return app__


def create_app():
    return init_ext_app()
