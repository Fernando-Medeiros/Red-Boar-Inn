from werkzeug.security import check_password_hash

from flask_login import login_user, current_user
from flask import current_app as app
from flask_pymongo import ObjectId

from ...models.user import User
from ...extensions.configuration import login_manager

import datetime


@login_manager.user_loader
def load_user(id_user) -> object:

    user_exists: dict = app.db.USERS.find_one({"_id": ObjectId(id_user)})
    
    user = User()
    user.return_user.update(user_exists)
   
    return user


def check_current_user() -> bool:

    if current_user.is_authenticated and current_user.is_active:
        
        return True


def set_offline_status(id_user):

    app.db.USERS.find_one_and_update(
        {'_id': ObjectId(id_user)}, {'$set': {'online': False}})


def set_online_status(id_user):

    app.db.USERS.find_one_and_update(
        {'_id': ObjectId(id_user)}, {'$set': {'online': True}})


def auth_login(**kwargs) -> bool:

    try:

        email: str = str(kwargs['email']).strip()

        find_user: dict = app.db.USERS.find_one({'email': email})

        password: bool = check_password_hash(
            find_user['password'], kwargs['password'])

    except Exception as ErrorLoginUser:

        return

    else:

        if find_user and password:

            user = User()

            user.return_user.update(find_user)

            set_online_status(user.return_user['_id'])

            login_user(user, remember=False, duration=datetime.timedelta(hours=1) ,fresh=False)

            return True
