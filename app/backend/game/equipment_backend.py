from flask_login import current_user


def equipments() -> dict:

    equips: dict = {}

    for equip in current_user.equipment:
        
        name: str = equip

        try:
            equip: dict = current_user.equipment[name]

            type: str = equip['type']

            sprite: str = f"/static/img/items/{type}/{equip['name']}.png"

            equips.update(
                {name: {
                    "equip": name.upper(),
                    "sprite": sprite,
                    "name": equip['name'].title().replace('_', ' '),
                    "level" : f"lv. {equip['level']}",
                    "status": f"status +  {equip['status']}"
                    }})          
        except:
            equips.update(
                {name: {
                    "equip": name.upper(),
                    "sprite": '',
                    "name": '',
                    "level": '',
                    "status": ''
                    }})

    return equips