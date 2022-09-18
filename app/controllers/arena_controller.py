from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


arena = Blueprint('arena', __name__)


@arena.route('/arena', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/arena/arena.html',

                           title='arena')
