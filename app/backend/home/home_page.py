from ..database import Database


class HomePage(Database):

    def __init__(self):
        self.by_level = []
        self._classification()


    def qnt_users(self) -> int:
        return self.db_find().__len__()


    def online_players(self) -> int:
        return self.db_find(online=True).__len__()
    

    def _classification(self):

        users: list[dict] = self.db_find()

        by_level: list[tuple(int, str)] = [(char['character']['level'], char['character']['name']) for char in users]        
        by_level = sorted(by_level, reverse=True)
        by_level: list[str] = [name for level, name in by_level]
        
        self.by_level = by_level
     
        for user in users:
            character, arena = user['character'], user['arena']
            character.update(arena)

            for index, name in enumerate(by_level):
                if character['name'] == name:
                    self.by_level[index] = character
                    break
    

    def render_by_level(self) -> str:
        html = []
        chars: list[dict] = self.by_level[:7]

        if chars:
            for char in chars:                    
                html.append(
                    f"""
                    <div class="grid grid-cols-3 m-auto p-2 text-center items-center border-b border-gray-400/20">                        
                        <span> {char['name'].title()} </span>                                           
                        <span> {char['vocation'].title()} - {char['job'].title()} </span>                                               
                        <span> {char['level']} </span>                       
                    </div>
                    """
                    )
        add_html = "\n".join(html)

        return add_html