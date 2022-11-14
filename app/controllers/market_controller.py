from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

market = Blueprint('market', __name__)


@market.route('/market', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('/game/market/market.html',

                           title='market')
