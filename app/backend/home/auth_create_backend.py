from werkzeug.security import generate_password_hash

from flask_login import login_user
from flask import current_app as app
from flask_pymongo import ObjectId

from ...models.user import User

from random import randint
import datetime


def check_user(**kwargs) -> bool:
    if not app.db.USERS.find_one({'email': kwargs['email']}):
        return True


def check_char_name(**kwargs) -> bool:
    if not app.db.USERS.find_one({'character.name': kwargs['charname']}):
        return True


def check_gender(form: dict) -> str:
        
    try:
        form['woman']
        return 'woman'

    except:
        return 'man'


def auth_create(**kwargs) -> bool:

    try:

        name: str = kwargs['name'].strip()
        email: str = kwargs['email'].strip()
        charname: str = kwargs['charname'].strip()
        gender: str = kwargs['gender'].strip()

        _password: str = generate_password_hash(kwargs['password'])

        _token_pwd: str = generate_password_hash(str(randint(1, 999999999999)))

        _id: str = ObjectId(str(randint(1, 999999999999999999999999)))

        date: str = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')


        _new_account = User()

        _new_account.return_user.update(
            _id=_id,
            name=name,
            email=email,
            password=_password,
            token_pwd=_token_pwd,
            date=date
            )

        _new_account.character.update(
            name=charname,
            gender=gender,
            sprite=f'/{gender}/peasant.png'
            )


    except Exception as ErrorCreateNewUser:
        return

    else:

        try:
            app.db.USERS.insert_one(_new_account.return_user)

        except Exception as ErrorCreateNewUser:        
            return False

        else:
          
            login_user(_new_account, remember=False, duration=datetime.timedelta(hours=1), fresh=False)
            
            return True
