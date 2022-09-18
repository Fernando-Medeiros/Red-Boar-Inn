from flask import Blueprint, render_template, request, url_for, redirect

from app.backends.auth_login_backend import check_current_user
from app.backends.home_info_backend import list_updates, qnt_users, online_players, show_rank


home = Blueprint("home", __name__)


@home.route('/')
def index():

    rank_characters_by_level = show_rank()

    number_of_accounts = qnt_users()

    number_of_online_users = online_players()

    return render_template('/home/home/home.html',

                           title='Red Boar Inn',
                           number_of_accounts=number_of_accounts,
                           number_of_online_users=number_of_online_users,

                           rank_characters_by_level=rank_characters_by_level)


@home.route('/update')
def updates():

    updates_notes = list_updates()

    return render_template('/home/updates/updates.html',

                           title='Updates',
                           updates_notes=updates_notes)


@home.route('/about')
def about():

    return render_template('/home/about/about.html',

                           title='About',)


@home.before_request
def _check():

    if check_current_user() and request.endpoint in ["home.index", "home.about", 'home.updates']:

        return redirect(url_for('profile.home'))
