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
    picture = database__.Column(database__.String, default='default.jpg')
    gold = database__.Column(database__.String, default='1')
    date = database__.Column(database__.DateTime, nullable=False, default=datetime.utcnow)
    character = database__.relationship('Characters', backref='author', lazy=True)
    inventory = database__.relationship('Inventory', backref='author', lazy=True)

    def create_char(self):
        char = Characters(name=self.username, author=self)
        return char

    def create_inventory(self):
        inventory = Inventory(author=self)
        return inventory

    @staticmethod
    def length():
        return len(User.query.all())


class Characters(database__.Model):
    id = database__.Column(database__.Integer, primary_key=True)
    name = database__.Column(database__.String, nullable=False, unique=True)
    profession = database__.Column(database__.String, default="Peasant")
    level = database__.Column(database__.Integer, default=1)
    experience = database__.Column(database__.Integer, default=1)
    health = database__.Column(database__.Integer, default=30)
    energy = database__.Column(database__.Integer, default=10)
    strength = database__.Column(database__.Integer, default=1)
    vitality = database__.Column(database__.Integer, default=1)
    wisdom = database__.Column(database__.Integer, default=1)
    dexterity = database__.Column(database__.Integer, default=1)
    luck = database__.Column(database__.Integer, default=1)
    pts_status = database__.Column(database__.Integer, default=25)
    date = database__.Column(database__.DateTime, nullable=False, default=datetime.utcnow)
    id_user = database__.Column(database__.Integer, database__.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def length():
        return Characters.query.all()


class Inventory(database__.Model):
    id = database__.Column(database__.Integer, primary_key=True)
    items = database__.Column(database__.String, nullable=False, default='item_0')
    id_user_ = database__.Column(database__.Integer, database__.ForeignKey('user.id'), nullable=False)
