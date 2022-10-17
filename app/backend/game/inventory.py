from flask import url_for
from flask_login import current_user as c_User

class Inventory:

    def render_items(self) -> str:

        html = []
      
        for key in c_User.inventory:
            
            name: str = key.replace('_', ' ').title()
            item: dict = c_User.inventory[key]
            sprite = url_for('static', filename='img/items/' + item['type'] + '/' + key + '.png')

            html.append(
                f"""
                <div class="card-item background-global">

                    <img src="{sprite}" width="35">
                    <span>{name}</span>
                    
                    <div class="grid-columns">
                    
                        <div class="color-card-info">
                            <p translate="no"> Qty: </p>
                            <p> Level: </p>
                            <p> Value: </p>
                            <p> Status: </p>
                            <p> Type: </p>
                        </div>
            
                        <div>
                            <p>{item['qty']}</p>
                            <p>{item['level']}</p>
                            <p>{item['value']}</p>
                            <p>{item['status']}</p>
                            <p>{item['type'].title()}</p>
                        </div>
                    </div>

                </div>
                """
                )
        add_html = "\n".join(html)

        return add_html

    def __len__(self):
        return c_User.inventory.__len__()
