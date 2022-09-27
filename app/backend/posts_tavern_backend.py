from flask import current_app as app
from flask_login import current_user as c_User
from flask_pymongo import ObjectId

from ..models.posts import Post

from random import randint
import datetime


def get_posts() -> list | dict:

    return list(app.db.TAVERN.find({}))


def set_posts(text) -> bool:
    
    date = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    
    try:
        _id = ObjectId(str(randint(111111111111111111111111, 999999999999999999999999)))
        
        if not text:
            raise ValueError()

        text_field = text.strip()

        post = Post()

        post.return_post.update(
            _id=_id,
            date=date,
            charname=c_User.character['name'],
            sprite=c_User.character['sprite'],
            info= text_field
        )

    except Exception as ErroCreatePost:
        return False
    
    else:
        app.db.TAVERN.insert_one(post.return_post)

        return True