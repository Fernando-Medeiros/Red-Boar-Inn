from flask_login import UserMixin


class User(UserMixin):
    
    __user = {
        "_id":'',
        "name": '',
        "email": '',
        "password": '',
        "token_pwd": '',
        "date": '',
        "online": True,

        "character": {
            "name": 'change a new name',
            "gender": "",
            "level": 1,
            "gold": 1,
            "jewel": 1,
            "sprite": 'sprite1.png',
            "vocation": "peasant",
            "job": "farmer"
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

        "skill": {
            "woodcutting": 1,
            "mining": 1,
            "herbalism": 1,
            "farming": 1,
            "hunt": 1
        },

        "craft": {
            "food": 1,
            "tool": 1,
            "armor": 1,
            "robe": 1,
            "accessory": 1,
          
            "shield": 1,
            "axe": 1,
            "bow": 1,
            "sword": 1,
            "stick": 1,
            "dagger": 1
        },

        "inventory": {
            "apple": {
                "qty": 1,
                "level": 1,
                "value": 1,
                "status": 3,
                "type": "food",
                "description": "Just a bland fruit"
            }
        },

        "equipment": {
            "head": "",
            "neckacle": "",
            "body": "",
            "handL": "",
            "handR": "",
            "ringL": "",
            
            "ringR": {
                "name":"bronze_ring",
                "level": 1,
                "value": 3,
                "status": 3,
                "type": "ring",
                "description": "Worth a few coins"},

            "legL": "",
            "legR": ""
        }

    }

    def get_id(self) -> str:

        try:
            return str(self.__user['_id'])
        except AttributeError:
            raise NotImplementedError(
                "No `id` attribute - override `get_id`") from None

    @property
    def return_user(self) -> dict:
        return self.__user

    @property
    def character(self) -> dict:
        return self.__user['character']
    
    @property
    def status(self) -> dict:
        return self.__user['status']
    
    @property
    def skill(self) -> dict:
        return self.__user['skill']
    
    @property
    def craft(self) -> dict:
        return self.__user['craft']

    @property
    def inventory(self) -> dict:
        return self.__user['inventory']
    
    @property
    def equipment(self) -> dict:
        return self.__user['equipment']