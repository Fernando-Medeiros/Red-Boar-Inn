from ..database import Database


class UpdatePage(Database):

    def render_updates(self) -> str:
        html = []
        updates: list[dict] = self.db_updates_find()[:14].__reversed__()

        for index, note in enumerate(updates):
            html.append(
                f"""
                <div class="container-updates-main">
                    <div  id="version-update-{index}">

                        <button type="button">
                            <span> <strong> { note['version'] } </strong> { "-" } <small> { note['date'] } </small> </span>  
                            <span>v</span>
                        </button>

                        <div> <p> { '<br>'.join(note['info']) } </p> </div>
                        
                    </div>
                </div>
                """
                )
        add_html = "\n".join(html)

        return add_html