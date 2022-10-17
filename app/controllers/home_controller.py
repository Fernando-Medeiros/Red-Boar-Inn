from flask import Blueprint, render_template, request, url_for, redirect

from app.backend.home.auth_login import check_current_user
from app.backend.home.home_page import HomePage
from app.backend.home.updates_page import UpdatePage


home = Blueprint("home", __name__)


@home.route('/')
def index():

    home = HomePage()

    number_of_accounts = home.qnt_users()
    number_of_online_users = home.online_players()
    add_html_rank = home.render_by_level()

    return render_template('/home/views/home.html',
                           title='Red Boar Inn',
                           number_of_accounts=number_of_accounts,
                           number_of_online_users=number_of_online_users,
                           add_html_rank=add_html_rank)


@home.route('/updates')
def updates():

    updates = UpdatePage()

    add_html_updates = updates.render_updates()

    return render_template('/home/views/updates.html',
                           title='Updates',
                           add_html_updates=add_html_updates)


@home.route('/about')
def about():
    return render_template('/home/views/about.html',
                           title='About')


@home.before_request
def _check():
    
    if check_current_user() and request.endpoint in ["home.index", "home.about", 'home.updates']:
        return redirect(url_for('profile.home'))
