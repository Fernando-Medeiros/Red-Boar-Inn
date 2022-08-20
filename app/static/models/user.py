from flask_login import UserMixin
from datetime import datetime

from app import database__, login_manager__


@login_manager__.user_loader
def load_user(id_user):
    database__.create_all()
    return User.query.get(int(id_user))


class User(database__.Model, UserMixin):

    id = database__.Column(database__.Integer, primary_key=True)
    username = database__.Column(database__.String, nullable=False, unique=True)
    email = database__.Column(database__.String, nullable=False, unique=True)
    password = database__.Column(database__.String, nullable=False)
    token_recover_pwd = database__.Column(database__.String, nullable=False)
    picture = database__.Column(database__.String, nullable=False, default="default.jpg")
    date = database__.Column(database__.DateTime, nullable=False, default=datetime.utcnow)
    gold = database__.Column(database__.Integer, nullable=False, default='1')
    character = database__.relationship('Characters', backref='author', lazy=True)
    inventory = database__.relationship('Inventory', backref='author', lazy=True)


class Characters(database__.Model):

    id = database__.Column(database__.Integer, primary_key=True)
    level = database__.Column(database__.Integer, nullable=False, default="1")
    experience = database__.Column(database__.Integer, nullable=False, default="1")
    profession = database__.Column(database__.String, nullable=False, default="Peasant")
    health = database__.Column(database__.Integer, nullable=False, default="15")
    energy = database__.Column(database__.Integer, nullable=False, default="10")

    strength = database__.Column(database__.Integer, nullable=False, default="1")
    vitality = database__.Column(database__.Integer, nullable=False, default="1")
    wisdom = database__.Column(database__.Integer, nullable=False, default="1")
    dexterity = database__.Column(database__.Integer, nullable=False, default="1")
    luck = database__.Column(database__.Integer, nullable=False, default="1")
    date = database__.Column(database__.DateTime, nullable=False, default=datetime.utcnow)
    id_user_ = database__.Column(database__.Integer, database__.ForeignKey('user.id'), nullable=False)


class Inventory(database__.Model):

    id = database__.Column(database__.Integer, primary_key=True)
    name = database__.Column(database__.String, nullable=False)
    description = database__.Column(database__.Text, nullable=False)
    id_user_ = database__.Column(database__.Integer, database__.ForeignKey('user.id'), nullable=False)
