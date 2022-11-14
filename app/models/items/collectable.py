from flask_login import UserMixin

from setup import database_sql as db


class Material(db.Model, UserMixin):
    __tablename__ = 'material'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='material')


class Jewel(db.Model, UserMixin):
    __tablename__ = 'jewelry'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='jewel')


class Key(db.Model, UserMixin):
    __tablename__ = 'keys'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='key')


class Book(db.Model,  UserMixin):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='book')
