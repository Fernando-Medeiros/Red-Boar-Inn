from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required, logout_user, logout_user, current_user

from app.forms import form_login, form_new_account, form_recover_password

from app.backends.auth_login_backend import auth_login, check_current_user, set_offline_status
from app.backends.auth_create_backend import auth_Create, check_User


auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    
    form = form_login.FormLogin()

    if form.validate_on_submit():

        if auth_login(email=form.email.data,
                      password=form.password.data):

            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)

            return redirect(url_for('home.index'))

        else:
            flash('Incorrect email or password!', 'alert-danger')

    return render_template('/home/auth/login.html',

                           title='Login',
                           form=form)


@auth.route('/auth/create', methods=['GET', 'POST'])
def create():

    form = form_new_account.FormNewAccount()

    if form.validate_on_submit():

        if check_User(email=form.email.data,
                      password=form.password.data):

            if auth_Create(name=form.username.data,
                           email=form.email.data,
                           password=form.password.data):

                return redirect(url_for('home.index'))

            else:
                flash('Please provide the correct data', 'alert-danger')

        else:
            flash(
                'E-mail already registered, Please choose another email or reset your password.', 'alert-danger')

    return render_template('/home/auth/create.html',

                           title='New account',
                           form=form)


@auth.route('/auth/recover', methods=['GET', 'POST'])
def recover():

    form = form_recover_password.FormSendToken()

    return render_template('/home/auth/send_email.html',
                           title='Recover',
                           form=form)


@auth.route('/auth/recover/auth_token', methods=['GET', 'POST'])
def auth_token():

    form_auth_token = form_recover_password.FormValidateToken()

    return render_template('/home/auth/auth_token.html',
                           title='Recover',
                           form_auth_token=form_auth_token)


@auth.route('/auth/recover/auth_token', methods=['GET', 'POST'])
def new_pwd():

    form_new_pwd = form_recover_password.FormNewPassword()

    return render_template('/home/auth/auth_token.html',
                           title='Auth',
                           form_new_pwd=form_new_pwd)


@auth.route('/auth/logout')
@login_required
def logout():

    set_offline_status(current_user.return_user['id'])

    logout_user()

    return redirect(url_for('home.index'))


@auth.before_request
def _check():
    if check_current_user() and request.endpoint in ["auth.login", "auth.create", 'auth.recover', 'auth.auth_token', 'auth.new_pwd']:

        return redirect(url_for('profile.home'))
