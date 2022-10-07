from ...extensions.configuration import db_sql as database



class Base(database.Model):
    __tablename__ = 'base'

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(35), nullable=False, unique=True)
    level = database.Column(database.Integer, nullable=False, default=1)
    value = database.Column(database.Float, nullable=False)
    status = database.Column(database.Integer, nullable=False)
    type = database.Column(database.String(10), default='base')
    description = database.Column(database.String(200), nullable=False)