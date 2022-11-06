from flask import url_for
from flask_login import current_user as c_User


class Status:
    def __init__(self):
        self.attribute()

    def attribute(self):
        character, status, equipment = c_User.character, c_User.status, c_User.equipment
        level = character['level']

        pct = 0.1

        self.attack = level + status['strength']
        self.magic = level + status['wisdom']
        self.defense = level + status['strength'] + status['vitality']
        self.resistance = level + status['dexterity'] + status['wisdom']
        self.agility = level + status['dexterity'] + status['strength']

        self.block = '{:.2f}'.format((level + self.defense) * pct)
        self.dodge = '{:.2f}'.format((level + self.agility) * pct)
        self.critical = '{:.2f}'.format((level + status['dexterity']) * pct)
        self.creativity = '{:.2f}'.format((level + status['creativity']) * pct)


    def settings(self) -> dict[str, int] :
        status = {
            'attack': self.attack,
            'magic': self.magic,
            'defense': self.defense,
            'resistance': self.resistance,
            'agility': self.agility,
            'creativity': self.creativity,
            'block': self.block,
            'dodge': self.dodge,
            'critical': self.critical,
        }
        return status


    def render_status(self) -> str:
        html = []
        status = self.settings()

        for sts in status:
            html.append(f"""
            <div class="flex justify-between border-b border-gray-500/50 p-2">
                <p>
                    {sts.title()}
                </p>
                <p>
                    {status[sts]}
                </p>
            </div>
            """
            )
        add_html = '\n'.join(html)

        return add_html


class CraftSkills:

    def __init__(self):
        self.settings()
        
    def settings(self):
        self.skills = [
            'woodcutting',
            'mining',
            'farming',
            'herbalism',
            'hunt'
        ]
        self.weapons = [
            'sword',
            'dagger',
            'stick',
            'axe',
            'bow'
        ]
        self.foods_tools_equipments = [
            'food',
            'tool',
            'armor',
            'robe',
            'accessory'
        ]

    def render_craft_skills(self):
        html = []
        width = '40px'
        skills, weapons, others = [], [], []

        for item in self.skills:
            skills.append(f"""
                <div class="w-full h-full p-2 gap-3 grid text-center items-center border border-gray-500/50">
                    
                    <img class="m-auto" src="{ url_for('static', filename='img/icons/' + item + '.png') }" width={width}>
                    Lv.{c_User.skill[item]} - {item.title()}
                </div>
            """)

        for item in self.weapons:
            weapons.append(f"""
                <div class="w-full h-full p-2 gap-3 grid text-center items-center border border-gray-500/50">
                    <img class="m-auto" src="{ url_for('static', filename='img/icons/' + item + '.png') }" width={width}>
                    lv.{c_User.craft[item]} - {item.title()}
                </div>
            """)

        for item in self.foods_tools_equipments:
            others.append(f"""
                <div class="w-full h-full p-2 gap-3 grid text-center items-center border border-gray-500/50">
                    <img class="m-auto" src="{ url_for('static', filename='img/icons/' + item + '.png') }" width={width}>
                    lv.{c_User.craft[item]} - {item.title()}
                </div>
            """)

        html.append('\n'.join(skills + weapons + others))

        add_html = '\n'.join(html)
      
        return add_html