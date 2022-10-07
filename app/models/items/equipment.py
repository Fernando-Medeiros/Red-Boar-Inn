from base import Base
from ...extensions.configuration import db_sql as database


class Hat(Base):
    __tablename__ = 'hats'

    type = database.Column(database.String(10), default='hat')


class Helmet(Base):
    __tablename__ = 'helmets'

    type = database.Column(database.String(10), default='helmet')


class Armor(Base):
    __tablename__ = 'armors'

    type = database.Column(database.String(10), default='armor')


class Glove(Base):
    __tablename__ = 'gloves'

    type = database.Column(database.String(10), default='glove')


class Boot(Base):
    __tablename__ = 'boots'

    type = database.Column(database.String(10), default='boot')


class Ring(Base):
    __tablename__ = 'rings'

    type = database.Column(database.String(10), default='ring')


class Necklace(Base):
    __tablename__ = 'necklaces'
   
    type = database.Column(database.String(10), default='necklace')
