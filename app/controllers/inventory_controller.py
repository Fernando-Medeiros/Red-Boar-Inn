from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import login_required, current_user


inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def home():

    html = []
    qty_items = current_user.inventory.__len__()

    for key in current_user.inventory:
        
        name = key
        item = current_user.inventory[key]
        sprite = url_for('static', filename='img/items/' + item['type'] + '/' + name + '.png')

        html.append(
            f"""
            <div class="row-items">

                <input class="checkbox" type="checkbox" id="{name}">

                <div>
                        <img src="{sprite}" width="35">
                    <span>  x  { item['qty'] }           </span>
                </div>

                <div><span>    { name }                  </span></div>
                <div><span> Lv.{ item['level'] }         </span></div>
                <div><span>    { item['value'] }         </span></div>
                <div><span>    { item['type'].title() }  </span></div>
                <div><span>    { item['status'] }        </span></div>
            </div>
            """)

    add_html = "\n".join(html)

    return render_template('/game/inventory/inventory.html',
                           title='Inventory',
                           qty_items=qty_items,
                           add_html=add_html)