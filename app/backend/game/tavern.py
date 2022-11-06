from flask import url_for
from flask_login import current_user as c_User

from ..database import Database
from ...models.posts import Post


class Tavern(Database):
        
    def get_posts(self) -> list[dict]:
        return self.db_tavern_find()


    def add_post(self, text) -> bool:
        date: str = self.get_datetime()
        
        try:
            _id: str = self.generate_id()
            
            text_field: str = text.strip()
            
            post = Post()
            post.return_post.update(
                _id=_id,
                date=date,
                charname=c_User.character['name'],
                sprite=c_User.character['sprite'],
                info= text_field
            )
            if not text_field:
                raise Exception()

        except Exception as ErroCreatePost:
            return False
        else:
            self.db_tavern_insert_one(post.return_post)
            return True


    def render_posts(self) -> str:
        html = [] 
        posts: list[dict] = self.get_posts().__reversed__()

        for post in posts:
            sprite = url_for('static', filename='img/sprites/' + post['sprite'])

            html.append(
                f"""
                <div class="w-full p-2 flex flex-row-2 border border-gray-400/25
                    rounded bg-gradient-to-b from-[#181818d7] to-black/40">


                    <div class="grid grid-cols gap-2 p-1 items-center w-max">
                        <img src="{sprite}" width="50px">                                             
                    </div>

                    <div class="grid grid-col-2 w-full p-1 items-center border border-gray-400/25
                        bg-gradient-to-b from-[#181818d7] to-black/40 ">

                        <span class="text-1xl flex items-center gap-3">
                            <p class="text-indigo-500">
                                { post['charname'].title() }
                            </p>
                            <small>
                            { post['date'][:10] } - { post['date'][10:] }
                            </small>
                        </span>
                        
                        <span class="h-full min-h-[60px] p-2">
                        { post['info'] }
                        </span>

                    </div>
                </div>
                """
                )
            add_html = "\n".join(html)

        return add_html