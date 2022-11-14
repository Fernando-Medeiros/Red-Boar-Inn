from setup import admin
from setup import database_sql as db

from ..backend.home.auth_admin import MyModelView
from ..models.items.collectable import Book, Jewel, Key, Material
from ..models.items.consumable import Food, Potion, Scroll
from ..models.items.equipment import (Armor, Boot, Glove, Hat, Helmet,
                                      Necklace, Ring)
from ..models.items.weapon import Bow, Shield, Spellbook, Stick, Sword
from ..models.user import Users


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