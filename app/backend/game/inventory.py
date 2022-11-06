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
                <div class="p-2 rounded border border-gray-400/25 items-center">

                    <img src="{sprite}" width="35" class="m-auto">
                    
                    <p class="text-xl text-center py-2">
                    {name}
                    </p>
                    
                    <div class="grid grid-cols-2 gap-5">
                    
                        <div class="color-card-info">
                            <p translate="no"> Qty: </p>
                            <p> Level: </p>
                            <p> Value: </p>
                            <p> Status: </p>
                            <p> Type: </p>
                        </div>
            
                        <div class="text-center">
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
