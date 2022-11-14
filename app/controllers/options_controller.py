from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

options = Blueprint('options', __name__)


@options.route('/options', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/options/options.html',

                           title='options')
