from flask_login import UserMixin
from setup import database_sql as db


class Food(db.Model, UserMixin):
    __tablename__ = 'foods'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='food')


class Potion(db.Model, UserMixin):
    __tablename__ = 'potions'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='potion')


class Scroll(db.Model, UserMixin):
    __tablename__ = 'scrolls'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='scroll')