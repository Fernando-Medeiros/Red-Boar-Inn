from flask import Flask
from dynaconf import FlaskDynaconf
from .extensions.blueprints import register_routes


def create_app():

    app = Flask(__name__)

    FlaskDynaconf(app, extensions_list=True, load_dotenv=True)

    register_routes(app)

    return app