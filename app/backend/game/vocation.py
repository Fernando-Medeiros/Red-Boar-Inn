from flask import url_for
from flask_login import current_user


class Vocation:
    
    def vocations(self) -> dict[str,dict]:

        return {
            'mage': {'man':'mage', 'woman': 'witch'},
            'warrior': {'man':'warrior', 'woman': 'warrior'},
            'thief': {'man':'thief', 'woman': 'thief'},
            'crafts': {'man':'craftsman', 'woman': 'craftswoman'}}


    def model_hmtl(self, name, sprite, description) -> str:
        html =  f"""
                <div id="{name}" class="p-2 flex-cols-2 gap-2 items-center rounded
                                        border border-gray-500/50 md:flex">

                    <div class="grid grid-cols-2 gap-2 w-auto p-2 items-center
                                text-center md:w-[225px]">
    
                        <img src="{sprite}" class="w-[81px]">

                        <div class="grid gap-2 broken-words m-auto">
                            <p>{name.title()}</p>
                        
                            <button value="{name}" class="text-xl">
                                <ion-icon name="add-circle-outline"></ion-icon>
                            </button>
                        </div>

                    </div>

                    <!-- DESCRIPTION -->
                    <div class="p-2 w-auto h-auto items-center border border-gray-500/50
                                md:h-full w-auto">
                        <div>
                            <p>{description}</p>
                        </div>
                    </div>

                </div>
                """
        return html


    def render_vocation(self) -> str:
        html = [] 
        l_vocations = self.vocations()

        for vocation in l_vocations:
            m_name, w_name = l_vocations[vocation].values()
            description = 'The description will be added in the next major update.'
            sprites = {
                'man': url_for('static', filename='img/sprites/man/{}.png'.format(m_name)),
                'woman': url_for('static', filename='img/sprites/woman/{}.png'.format(w_name))
                }

            html.append(self.model_hmtl(m_name, sprites['man'], description))
            html.append(self.model_hmtl(w_name, sprites['woman'], description))

        add_html = "\n".join(html)

        return add_html
