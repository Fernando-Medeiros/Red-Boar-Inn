from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


world = Blueprint('world', __name__)


@world.route('/world', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/world/world.html',

                           title='world')
