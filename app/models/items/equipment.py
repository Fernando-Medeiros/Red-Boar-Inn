from flask_login import UserMixin
from setup import database_sql as db


class Hat(db.Model, UserMixin):
    __tablename__ = 'hats'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='hat')


class Helmet(db.Model, UserMixin):
    __tablename__ = 'helmets'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='helmet')


class Armor(db.Model, UserMixin):
    __tablename__ = 'armors'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='armor')


class Glove(db.Model, UserMixin):
    __tablename__ = 'gloves'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='glove')


class Boot(db.Model, UserMixin):
    __tablename__ = 'boots'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='boot')


class Ring(db.Model, UserMixin):
    __tablename__ = 'rings'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='ring')


class Necklace(db.Model, UserMixin):
    __tablename__ = 'necklaces'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False, default=1)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    type = db.Column(db.String(10), default='necklace')
