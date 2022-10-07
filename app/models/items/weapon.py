from base import Base
from ...extensions.configuration import db_sql as database


class Sword(Base):
    __tablename__ = 'swords'
   
    type = database.Column(database.String(10), default='sword')


class Stick(Base):
    __tablename__ = 'sticks'

    type = database.Column(database.String(10), default='stick')


class Bow(Base):
    __tablename__ = 'bows'

    type = database.Column(database.String(10), default='bow')


class Shield(Base):
    __tablename__ = 'shields'

    type = database.Column(database.String(10), default='shield')


class Spellbook(Base):
    __tablename__ = 'spellbooks'

    type = database.Column(database.String(10), default='spellbook')
 