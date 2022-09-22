from werkzeug.security import generate_password_hash
from flask_login import login_user
from flask import current_app as app

from ..models.user import User

from random import randint
import datetime


def check_user(**kwargs):
    if not app.db.USERS.find_one({'email': kwargs['email']}):
        return True


def check_char_name(**kwargs):
    if not app.db.USERS.find_one({'character.name': kwargs['charname']}):
        return True



def auth_create(**kwargs):
    try:

        name = str(kwargs['name']).strip()
        email = str(kwargs['email']).strip()
        charname = str(kwargs['charname']).strip()


        __password = generate_password_hash(kwargs['password'])

        __token_pwd = generate_password_hash(
            str(randint(111111111111, 999999999999)))

        __id = generate_password_hash(
            str(randint(111111111111, 999999999999)))

        date = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')


        __new_account = User()

        __new_account.return_user.update(
            id=__id,
            name=name,
            email=email,
            password=__password,
            token_pwd=__token_pwd,
            date=date)

        __new_account.return_user['character']['name'] = charname


    except Exception as ErrorCreateNewUser:
        return

    else:

        try:
            app.db.USERS.insert_one(__new_account.return_user)

        except Exception as ErrorCreateNewUser:
            return False

        else:
            user = User()

            user.return_user.update(__new_account.return_user)

            login_user(user, remember=False, duration=datetime.timedelta(hours=1), fresh=False)
            
            return True
