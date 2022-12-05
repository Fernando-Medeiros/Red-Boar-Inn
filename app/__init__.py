from dynaconf import FlaskDynaconf
from flask import Flask

from .extensions.blueprints import register_routes
from .extensions.models import register_models


def create_app():

    app = Flask(
        __name__,
        template_folder='frontend/views',
        static_folder='frontend/static')

    FlaskDynaconf(app, extensions_list=True, load_dotenv=True)

    register_routes(app)
    
    register_models()
    
    return app