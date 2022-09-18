from flask_login import UserMixin
from datetime import datetime

from werkzeug.security import generate_password_hash
from random import randint


class User(UserMixin):

    date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    __user = {
        "id": '',
        "name": '',
        "email": '',
        "password": '',
        "token_pwd": '',
        "date": date,
        "online": True,

        "character": {
            "name": 'change a new name',
            "level": 1,
            "gold": 1,
            "jewel": 1,
            "sprite": 'sprite1.png',
            "vocation": "Peasant",
            "job": "Farmer"
        },

        "status": {
            "points": 25,
            "experience": 1,
            "next_experience": 25,

            "health": 30,
            "energy": 10,
            "current_health": 30,
            "current_energy": 10,

            "strength": 1,
            "vitality": 1,
            "wisdom": 1,
            "dexterity": 1,
            "creativity": 1
        },

        "skills": {
            "woodcutting": 1,
            "mining": 1,
            "herbalism": 1,
            "farming": 1,
            "hunt": 1
        },

        "craft": {
            "food": 1,
            "tools": 1,
            "heavy_armor": 1,
            "light_armor": 1,
            "accessories": 1,
            "axes_and_hammers": 1,
            "bows_and_crossbows": 1,
            "swords": 1,
            "magic_staffs": 1,
            "light_arms": 1
        },

        "inventory": {
            "apple": {
                "qnt": 1,
                "price": 1,
                "type": "food",
                "sprite": "apple.png"
            }
        }

    }

    def get_id(self) -> str:

        try:
            return str(self.__user['id'])
        except AttributeError:
            raise NotImplementedError(
                "No `id` attribute - override `get_id`") from None

    @property
    def return_user(self) -> dict:
        return self.__user


    @return_user.setter
    def return_user(self, **kwargs):
        self.__user.update(**kwargs)
