from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

world = Blueprint('world', __name__)


@world.route('/world', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/world/world.html',

                           title='world')
