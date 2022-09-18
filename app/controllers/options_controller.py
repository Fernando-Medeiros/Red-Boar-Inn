from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


options = Blueprint('options', __name__)


@options.route('/options', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/options/options.html',

                           title='options')
