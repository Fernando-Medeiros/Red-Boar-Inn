from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

craft = Blueprint('craft', __name__)


@craft.route('/craft', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/craft/craft.html',

                           title='Craft')
