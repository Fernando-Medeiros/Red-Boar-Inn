import json
from random import choice

from flask_login import current_user as c_User

from ..database import Database


class Classification(Database):
    def __init__(self):
        self.by_level = []
        self.by_victory = []
        self.__classification()


    def __classification(self):

        users: list[dict] = self.db_find()

        by_level: list[tuple(int, str)] = [
            (char['character']['level'], char['character']['name']) for char in users]

        by_victory: list[tuple(int, str)] = [
            (char['arena']['victory'], char['character']['name']) for char in users]
        
        by_level = sorted(by_level, reverse=True)
        by_victory = sorted(by_victory, reverse=True)

        by_level: list[str] = [name for level, name in by_level]
        by_victory: list[str] = [name for victory, name in by_victory]
        
        self.by_level = by_level
        self.by_victory = by_victory

        for user in users:
            character, arena = user['character'], user['arena']
            character.update(arena)

            for index, name in enumerate(by_level):
                if character['name'] == name:
                    self.by_level[index] = character
                    break

            for index, name in enumerate(by_victory):
                if character['name'] == name:
                    self.by_victory[index] = character                                 
                    break
             

    def render_by_victory(self) -> str:
        html = []
        chars: list = self.by_victory[:5]

        if chars:
            for char in chars:                    
                html.append(
                    f"""
                    <div class="grid grid-cols-5 items-center text-center rounded border
                                border-gray-500/50 p-2">
                        <p class="break-words">{char['name'].title()}</p>
                        <p>{char['vocation'].title()}</p>
                        <p>{char['level']}</p>
                        <p>{char['victory']}</p>
                        <img width="45px" src=static/img/sprites{char['sprite']}
                        class="m-auto">
                    </div>
                    """
                    )
        add_html = "\n".join(html)

        return add_html
    

    def render_by_level(self) -> str:
        html = []
        chars: list[dict] = self.by_level[:5]

        if chars:
            for char in chars:                    
                html.append(
                    f"""
                    <div class="grid grid-cols-5 items-center text-center rounded
                                border border-gray-500/50 p-2">
                        <p class="break-words">{char['name'].title()}</p>
                        <p>{char['vocation'].title()}</p>
                        <p>{char['level']}</p>
                        <p>{char['victory']}</p>
                        <img width="45px" src=static/img/sprites{char['sprite']}
                        class="m-auto">
                    </div>
                    """
                    )
        add_html = "\n".join(html)

        return add_html



class Opponents(Database):
    
    def online(self) -> list[dict]:
        user = self.db_find(online=True)  
        online_characters: list[dict] = []        

        for char in user:
            character, status = char['character'], char['status']
            character.update(status)
            online_characters.append(character)

        return online_characters


    def offline(self) -> list[dict]:
        user = self.db_find() 
        all_characters: list[dict] = []       

        for char in user:
            character, status = char['character'], char['status']
            character.update(status)
            all_characters.append(character)
        
        return all_characters


    def __len__(self) -> (int|int):
        return len(self.online()), len(self.offline())



class BattleLog(Database):

    def add_log(self, status='winner', **kwargs) -> bool:
        date: str = self.get_datetime()
        
        try:
            _id: str = self.generate_id()
            
            winner: str = c_User.character['name']
            loser: str = kwargs['name']
            
            if status == 'defeat':
                winner: str = kwargs['name']
                loser: str = c_User.character['name']

            with open('app/models/log.json', 'r', encoding='utf-8') as jsonfile:
                log = json.load(jsonfile)               
        
            log.update(
                _id=_id,
                winner=winner,
                loser=loser,
                date=date
            )
            if not loser:
                raise Exception()

        except Exception as ErroCreateLog:
            return
        else:
            self.db_arena_insert_one(log)
            return True
   

    def render_logs(self) -> str:
        html = []
        logs: list[dict] = self.db_arena_find()[:4]

        if logs:
            for log in logs:                    
                html.append(
                    f"""
                    <div class="grid grid-cols-3 text-center rounded p-2 py-2 border
                                border-gray-500/50">
                        <p>{log['winner'].title()}</p>
                        <p>{log['loser'].title()}</p>
                        <p>{log['date']}</p>
                    </div>
                    """
                    )
        add_html = "\n".join(html)

        return add_html



class Battle(Opponents, BattleLog):
    opponent = {}

    def shuffle_opponent(self, **kwargs):
                
        if 'opponent' in kwargs['choice']:
            self.opponent = choice(self.online())
        else:
            self.opponent = choice(self.offline())
        

    def render_opponent(self) -> str:
        html = []
        opponent: list[dict] = self.opponent
        
        if opponent:              
            html.append(
                f"""
                <img id="opponent"
                    width="85px"
                    class="m-auto p-2"
                    src=static/img/sprites{opponent['sprite']}>

                <p class="text-1xl p-2">
                    {opponent['name'].title()}
                </p>
                
                <p id="opponent_health" value={opponent['health']}></p>

                <div class="w-full h-5 rounded-full items-center justify-center
                            border border-gray-400/75 ">
                    
                    <div id="opponent_current_health" value={opponent['current_health']}
                            class="relative w-full h-5 rounded-full bg-red-400/50">                                            
                    </div>                 

                </div>             
                """
                )
        add_html = "\n".join(html)
        
        return add_html