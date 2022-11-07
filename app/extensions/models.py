from setup import database_sql as db, admin

from ..backend.home.auth_admin import MyModelView

from ..models.user import Users
from ..models.items.collectable import Material, Jewel, Key, Book
from ..models.items.consumable import Food, Potion, Scroll
from ..models.items.equipment import Hat, Helmet, Armor, Glove, Boot, Ring, Necklace
from ..models.items.weapon import Sword, Stick, Bow, Shield, Spellbook


def register_models():
    models = [
        Users,
        Material,
        Jewel,
        Key,
        Book,
        Food,
        Potion,
        Scroll,
        Hat,
        Helmet,
        Armor,
        Glove,
        Boot,
        Ring,
        Necklace,
        Sword,
        Stick,
        Bow,
        Shield,
        Spellbook
    ]
    
    for model in models:

        admin.add_view(MyModelView(model, db.session))