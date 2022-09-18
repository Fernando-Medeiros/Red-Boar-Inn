from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


tavern = Blueprint('tavern', __name__)


@tavern.route('/tavern', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/tavern/tavern.html',

                           title='tavern')
