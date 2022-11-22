import datetime
from random import randint

from flask import current_app as app
from flask_pymongo import ObjectId
from werkzeug.security import generate_password_hash

from .flash_messages import FlashMessages


class Generate:
    def get_datetime(self) -> str:
        return datetime.datetime.today().strftime('%d/%m/%Y %H:%M')


    def generate_id(self) -> ObjectId:
        return ObjectId(str(randint(1, 999999999999999999999999)))
    

    def generate_password(self, password: str) -> str:
        return generate_password_hash(password)


    def generate_token(self) -> str:
        return generate_password_hash(str(randint(1, 999999999999)))



class CollectionUsers:
    def db_find(self, **kwargs) -> list[dict]:
        """COLLECTION USERS"""
        return list(app.db.USERS.find(kwargs))


    def db_find_one(self, find: dict) -> dict:
        """COLLECTION USERS"""
        return app.db.USERS.find_one(find)
    

    def db_insert_one(self, insert: dict):
        """COLLECTION USERS"""
        app.db.USERS.insert_one(insert)


    def db_find_one_and_update(self, find: dict, update: dict):
        """COLLECTION USERS"""
        app.db.USERS.find_one_and_update(find, {'$set': update})


    def db_find_one_and_update_many(self, find: dict, update: list[dict]):
        """COLLECTION USERS"""
        list_dict = [{'$set': item} for item in update]

        app.db.USERS.find_one_and_update(find, list_dict)



class CollectionUpdates:
    def db_updates_find(self, **kwargs) -> list[dict]:
        """COLLECTION UPDATES"""
        return list(app.db_update.UPDATES.find(kwargs))



class CollectionArena:
    def db_arena_find(self, **kwargs) -> list[dict]:
        """COLLECTION ARENA"""
        return list(app.db.ARENA.find(kwargs))
    

    def db_arena_insert_one(self, insert: dict):
        """COLLECTION ARENA"""
        app.db.ARENA.insert_one(insert)



class CollectionTavern:
    def db_tavern_find(self, **kwargs) -> list[dict]:
        """COLLECTION TAVERN"""
        return list(app.db.TAVERN.find(kwargs))


    def db_tavern_insert_one(self, insert: dict):
        """COLLECTION TAVERN"""
        app.db.TAVERN.insert_one(insert)



class Database(
    Generate,
    CollectionUsers,
    CollectionUpdates,
    CollectionArena,
    CollectionTavern,
    FlashMessages):

    def __init__(self):
        super().__init__()