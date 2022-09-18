from werkzeug.security import check_password_hash
from flask_login import login_user, current_user

from app.models.user import User
from app.extensions.configuration import mongo, login_manager

import datetime


@login_manager.user_loader
def load_user(id_user):

    user_exists = mongo.db.USERS.find_one({"id": id_user})
    
    user = User()
    user.return_user.update(user_exists)
    
    return user


def check_current_user():

    if current_user.is_authenticated and current_user.is_active:
        
        return True


def set_offline_status(id_user):

    mongo.db.USERS.find_one_and_update(
        {'id': id_user}, {'$set': {'online': False}})


def set_online_status(id_user):

    mongo.db.USERS.find_one_and_update(
        {'id': id_user}, {'$set': {'online': True}})


def auth_login(**kwargs):

    try:

        email = str(kwargs['email']).strip()

        __find_user = mongo.db.USERS.find_one({'email': email})

        password = check_password_hash(
            __find_user['password'], kwargs['password'])

    except Exception as ErrorLoginUser:

        return

    else:

        if __find_user and password:

            __user = User()

            __user.return_user.update(__find_user)

            set_online_status(__user.return_user['id'])

            login_user(__user, remember=False, duration=datetime.timedelta(hours=1) ,fresh=False)

            return True
