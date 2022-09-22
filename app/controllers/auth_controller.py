from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required, logout_user, logout_user, current_user

from ..forms.form_new_account import FormNewAccount
from ..forms.form_login import FormLogin
from ..forms.form_recover_password import FormSendToken, FormValidateToken, FormNewPassword

from ..backend.auth_login_backend import auth_login, check_current_user, set_offline_status
from ..backend.auth_create_backend import auth_create, check_user, check_char_name
from ..backend.auth_recover_backend import send_mail, new_pwd, validate_token


auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    
    form = FormLogin()

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

    form = FormNewAccount()

    if form.validate_on_submit():

        if check_user(email=form.email.data):

            if check_char_name(charname=form.charname.data):

                if auth_create(name=form.username.data,
                                email=form.email.data,
                                password=form.password.data,
                                charname=form.charname.data):

                    return redirect(url_for('home.index'))

                else:
                    flash('Please provide the correct data', 'alert-danger')
            else:
                flash('Character name is already in use.', 'alert-danger')
        else:
            flash(
                'E-mail already registered, Please choose another email or reset your password.', 'alert-danger')

    return render_template('/home/auth/create.html',
                           title='New account',
                           form=form)


@auth.route('/auth/recover', methods=['GET', 'POST'])
def recover():

    form = FormSendToken()

    if form.validate_on_submit():
        
        if send_mail(form.email.data): 

            flash('Token sent! Check your mailbox.', 'alert-success')

            return redirect(url_for('auth.auth_token'))

        else:
            flash('Incorrect email!', 'alert-danger')
       
    return render_template('/home/auth/send_email.html',
                           title='Recover',
                           form=form)


@auth.route('/auth/recover/auth_token', methods=['GET', 'POST'])
def auth_token():

    form_auth_token = FormValidateToken()
  

    if form_auth_token.is_submitted():

        if validate_token(token=form_auth_token.token.data):
            
            flash('Valid Token! Choose your new password.', 'alert-success')

            return redirect(url_for('auth.new_password'))
            
        else:
            flash('Incorrect email or token!', 'alert-danger')

    return render_template('/home/auth/auth_token.html',
                           title='Auth',
                           form_auth_token=form_auth_token)


@auth.route('/auth/recover/new_password', methods=['GET', 'POST'])
def new_password():
    
    form_new_pwd = FormNewPassword()

    if form_new_pwd.is_submitted():

        if new_pwd(
            email=form_new_pwd.email_auth.data,
            password=form_new_pwd.password.data):
            
            flash('Password changed successfully!', 'alert-success')

            return redirect(url_for('auth.login'))
        
        else:
            flash('Invalid Password!', 'alert-danger')

    return render_template('/home/auth/new_password.html',
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
