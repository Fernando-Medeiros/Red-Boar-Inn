from flask_login import UserMixin
from setup import database_sql as db


class Sword(db.Model, UserMixin):
    __tablename__ = 'swords'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='sword')


class Stick(db.Model, UserMixin):
    __tablename__ = 'sticks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='stick')


class Bow(db.Model, UserMixin):
    __tablename__ = 'bows'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='bow')


class Shield(db.Model, UserMixin):
    __tablename__ = 'shields'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='shield')


class Spellbook(db.Model, UserMixin):
    __tablename__ = 'spellbooks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='spellbook')
 