from flask import current_app as app
from flask_login import current_user
from flask_pymongo import ObjectId


class Profile:
    
    def render_profile(self):
        return