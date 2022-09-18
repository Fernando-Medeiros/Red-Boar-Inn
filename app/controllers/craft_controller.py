from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


craft = Blueprint('craft', __name__)


@craft.route('/craft', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/craft/craft.html',

                           title='Craft')
