from flask import Blueprint, render_template
from flask_login import login_required

from ..backend.game.inventory import Inventory

inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def home():

    inventory = Inventory()

    qty_items = inventory.__len__()
    add_html_items = inventory.render_items()

    return render_template('/game/inventory/inventory.html',
                           title='Inventory',
                           qty_items=qty_items,
                           add_html_items=add_html_items)