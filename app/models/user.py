from flask_login import UserMixin
from setup import database_sql as db


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    token_pwd = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    online = db.Column(db.Boolean) 
    admin = db.Column(db.Boolean) 

    def __str__(self) -> str:
        return self.name


class Base:

    def basic_items(self, inventory):
        items = {
            "apple": {
                "qty": 1,
                "level": 1,
                "value": 1,
                "status": 3,
                "type": "food",
                "description": "Just a bland fruit"
            },
            "health_potion": {
                "qty": 1,
                "level": 1,
                "value": 1,
                "status": 4,
                "type": "potion",
                "description": "Just a bland potion"
            },
            "energy_potion": {
                "qty": 1,
                "level": 1,
                "value": 1,
                "status": 4,
                "type": "potion",
                "description": "Just a bland potion"
            }
            }
        inventory.update(items)

    def basic_equipment(self, equipment):
        items = {
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
        equipment.update(items)



class User(UserMixin, Base):
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
        "inventory": {},
        "equipment": {},
        "arena": {
            "victory": 0,
            "defeat": 0
        }
    }

    def __init__(self) -> None:
        super().__init__()
        self.basic_items(self.inventory)
        self.basic_equipment(self.equipment)


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
    
    @property
    def arena(self) -> dict:
        return self.__user['arena']
    