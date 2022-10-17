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
            return
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
                <div class="body-posts">

                    <div class="column-img-name-date">
                        <img src="{sprite}" width="50px">
                        <span> { post['charname'].title() } </span>
                        <small> { post['date'][:10] } </small>
                        <small> { post['date'][10:] } </small>
                    </div>

                    <div class="post-info">
                        { post['info'] }
                    </div>
                </div>
                """
                )
            add_html = "\n".join(html)

        return add_html