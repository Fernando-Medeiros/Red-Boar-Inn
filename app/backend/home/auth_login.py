import datetime

from flask import current_app as app
from flask_login import current_user, login_user
from flask_pymongo import ObjectId
from werkzeug.security import check_password_hash

from setup import login_manager

from ...models.user import User
from ..database import Database


@login_manager.user_loader
def load_user(id_user) -> object:
    
    user_exists: dict = app.db.USERS.find_one({"_id": ObjectId(id_user)})
    user = User()
    user.return_user.update(user_exists)
    return user


def check_current_user() -> bool:
    if current_user.is_authenticated and current_user.is_active:        
        return True


class AuthLogin(Database):
    
    def offline_status(self):
        
        _id = current_user.return_user['_id']

        self.db_find_one_and_update(
            find={'_id': ObjectId(_id)},
            update={'online': False})
   

    def update_model(self, id_user: str, model: dict):

        model['online'] = True

        self.db_find_one_and_update(
            find={'_id': ObjectId(id_user)},
            update=model)

      
    def auth_login(self, **kwargs) -> bool:
        try:
            email: str = str(kwargs['email']).strip()

            find_user: dict = self.db_find_one(find={'email': email})

            password: bool = check_password_hash(
                find_user['password'], kwargs['password'])

            remember = kwargs['remember']
            
            if password == False:
                raise

        except:
            self.flash_error_auth_login()

        else:
            if find_user and password:

                user = User()
                user.return_user.update(find_user)

                login_user(user, remember=remember, duration=datetime.timedelta(minutes=30) ,fresh=True)

                self.update_model(user.return_user['_id'], user.return_user)
                
                return True