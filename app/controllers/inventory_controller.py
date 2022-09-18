from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


inventory = Blueprint('inventory', __name__)


@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/inventory/inventory.html',

                           title='Inventory')
