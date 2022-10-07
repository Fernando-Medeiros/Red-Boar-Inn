from base import Base
from ...extensions.configuration import db_sql as database


class Food(Base):
    __tablename__ = 'foods'

    type = database.Column(database.String(10), default='food')


class Potion(Base):
    __tablename__ = 'potions'

    type = database.Column(database.String(10), default='potion')


class Scroll(Base):
    __tablename__ = 'scrolls'

    type = database.Column(database.String(10), default='scroll')