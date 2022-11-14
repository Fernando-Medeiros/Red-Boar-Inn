import json
from datetime import datetime

from flask_login import UserMixin

from setup import database_sql as db

from ..backend.database import CollectionUsers


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _id = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    token_pwd = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    online = db.Column(db.Boolean) 
    admin = db.Column(db.Boolean) 

    def __str__(self) -> str:
        return self.name

    def is_admin(self) -> bool:
        return self.admin

    def migrate_mongo_users(self):

        mongo_users: list[dict] = CollectionUsers().db_find()
        
        for user in mongo_users:
            if not Users.query.filter_by(email=user['email']).first():
                    
                db.session.add(
                    Users(
                    _id=user['_id'].__str__(), 
                    name=user['name'], 
                    email=user['email'], 
                    password=user['password'], 
                    token_pwd=user['token_pwd'], 
                    created_at=datetime.strptime(user['date'], '%d/%m/%Y %H:%M:%S'), 
                    online=user['online'],
                    admin=False
                    ))
                db.session.commit()
                    
                    
class User(UserMixin):
    __user = {}
    
    with open('app/models/user.json', 'r', encoding='utf-8') as jsonfile:
        __user = json.load(jsonfile)        

    def get_id(self) -> str:
        try:
            return str(self.__user['_id'])
        except AttributeError:
            raise NotImplementedError(
                "No `id` attribute - override `get_id`") from None

    @property
    def return_user(self) -> dict:
        return self.__user

    @property
    def character(self) -> dict:
        return self.__user['character']
    
    @property
    def status(self) -> dict:
        return self.__user['status']
    
    @property
    def skill(self) -> dict:
        return self.__user['skill']
    
    @property
    def craft(self) -> dict:
        return self.__user['craft']

    @property
    def inventory(self) -> dict:
        return self.__user['inventory']
    
    @property
    def equipment(self) -> dict:
        return self.__user['equipment']
    
    @property
    def arena(self) -> dict:
        return self.__user['arena']
    
    def __str__(self) -> str:
        return 'User:{} <> Char:{}'.format(
            self.return_user['name'], self.character['name'])