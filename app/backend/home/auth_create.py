import datetime

from flask_login import login_user

from ...models.user import User
from ..database import Database


class CreateNewAccount(Database):

    def check_user(self, **kwargs) -> bool:

        if self.db_find_one(find={'email': kwargs['email']}):
            return self.flash_email_already_exists()
        
        return True


    def check_char_name(self, **kwargs) -> bool:

        if self.db_find_one(find={'character.name': kwargs['charname']}):
            return self.flash_charname_already_exists()

        return True
        

    def check_gender(self, form: dict) -> str:
        
        try:
            form['woman']
            return 'woman'
        except:
            return 'man'


    def auth_create(self, **kwargs) -> bool:

        try:
            name: str = kwargs['name'].strip()
            email: str = kwargs['email'].strip()
            charname: str = kwargs['charname'].strip()
            gender: str = kwargs['gender'].strip()

            password: str = self.generate_password(kwargs['password'])

            token_pwd: str = self.generate_token()

            _id: str = self.generate_id()

            date: str = self.get_datetime()

            new_account = User()
            new_account.return_user.update(
                _id=_id,
                name=name,
                email=email,
                password=password,
                token_pwd=token_pwd,
                date=date
                )
            new_account.character.update(
                name=charname,
                gender=gender,
                sprite=f'/{gender}/peasant.png'
                )
        except:
            self.flash_error_create_account()

        else:
            try:
                self.db_insert_one(new_account.return_user)

            except:        
                self.flash_error_create_account()
                
            else:
                login_user(
                    new_account,
                    remember=False,
                    duration=datetime.timedelta(minutes=30),
                    fresh=True)                

                return True