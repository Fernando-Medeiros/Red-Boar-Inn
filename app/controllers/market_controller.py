from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required


market = Blueprint('market', __name__)


@market.route('/market', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/market/market.html',

                           title='market')
