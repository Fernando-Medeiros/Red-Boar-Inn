from flask import Flask
from dynaconf import FlaskDynaconf
from .extensions.blueprints import register_routes
from .extensions.models import register_models

def create_app():

    app = Flask(__name__, template_folder='views')

    FlaskDynaconf(app, extensions_list=True, load_dotenv=True)

    register_routes(app)
    
    register_models()
    
    return app