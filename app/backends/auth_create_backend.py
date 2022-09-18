from werkzeug.security import generate_password_hash
from flask_login import login_user

from app.models.user import User
from app.extensions.configuration import mongo

from random import randint
import datetime


def check_User(**kwargs):

    if not mongo.db.USERS.find_one({'email': kwargs['email']}):

        return True


def auth_Create(**kwargs):

    try:

        name = str(kwargs['name']).strip()
        email = str(kwargs['email']).strip()

        __password = generate_password_hash(kwargs['password'])

        __token_pwd = generate_password_hash(
            str(randint(111111111111, 999999999999)))

        __id = generate_password_hash(
            str(randint(111111111111, 999999999999)))

        __new_account = User()

        __new_account.return_user.update(
            id=__id,
            name=name,
            email=email,
            password=__password,
            token_pwd=__token_pwd)

    except Exception as ErrorCreateNewUser:

        return

    else:

        try:
            mongo.db.USERS.insert_one(__new_account.return_user).inserted_id

        except Exception as ErrorCreateNewUser:
            return False

        else:                
            __user = User()

            __user.return_user.update(__new_account.return_user)

            login_user(__user, remember=False, duration=datetime.timedelta(hours=1) ,fresh=False)

            return True
