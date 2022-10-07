from base import Base
from ...extensions.configuration import db_sql as database


class Craft(Base):
    __tablename__ = 'crafts'
    
    type = database.Column(database.String(10), default='craft')


class Jewel(Base):
    __tablename__ = 'jewelry'

    type = database.Column(database.String(10), default='jewel')


class Key(Base):
    __tablename__ = 'keys'

    type = database.Column(database.String(10), default='key')


class Book(Base):
    __tablename__ = 'books'
    
    type = database.Column(database.String(10), default='book')
