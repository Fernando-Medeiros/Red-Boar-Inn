from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user

from ..forms.form_new_account import FormNewAccount
from ..forms.form_login import FormLogin
from ..forms.form_recover_password import FormSendToken, FormValidateToken, FormNewPassword

from ..backend.home.auth_login import check_current_user, AuthLogin
from ..backend.home.auth_create import CreateNewAccount
from ..backend.home.auth_recover import AuthRecover


auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():

    login = AuthLogin()
    form = FormLogin()

    if form.validate_on_submit():

        if login.auth_login(
            email=form.email.data,
            password=form.password.data,
            remember=form.remember.data):

            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)

            return redirect(url_for('home.index'))

    return render_template('home/views/auth/login.html',
                           title='Login',
                           form=form)



@auth.route('/auth/create', methods=['GET', 'POST'])
def create():

    create = CreateNewAccount()
    form = FormNewAccount()

    if form.validate_on_submit():

        if create.check_user(email=form.email.data):

            if create.check_char_name(charname=form.charname.data):

                if create.auth_create(name=form.username.data,
                                email=form.email.data,
                                password=form.password.data,
                                charname=form.charname.data,
                                gender=create.check_gender(request.form)):

                    return redirect(url_for('home.index'))                   
         
    return render_template('home/views/auth/create.html',
                           title='New account',
                           form=form)



@auth.route('/auth/recover', methods=['GET', 'POST'])
def recover():

    recover = AuthRecover()
    form = FormSendToken()

    if form.validate_on_submit():
        
        if recover.send_mail(form.email.data): 

            return redirect(url_for('auth.auth_token'))
       
    return render_template('home/views/auth/send_email.html',
                           title='Recover',
                           form=form)



@auth.route('/auth/recover/auth_token', methods=['GET', 'POST'])
def auth_token():

    recover = AuthRecover()
    form_auth_token = FormValidateToken()
  
    if form_auth_token.is_submitted():

        if recover.validate_token(token=form_auth_token.token.data):
            
            return redirect(url_for('auth.new_password',
                                    token=form_auth_token.token.data))
            
    return render_template('home/views/auth/auth_token.html',
                           title='Auth',
                           form_auth_token=form_auth_token)



@auth.route('/auth/recover/new_password/<token>', methods=['GET', 'POST'])
def new_password(token):
    
    recover = AuthRecover()
    form_new_pwd = FormNewPassword()

    if form_new_pwd.is_submitted():

        if recover.new_pwd(
            token=token,
            password=form_new_pwd.password.data):
            
            return redirect(url_for('auth.login'))
        
    return render_template('home/views/auth/new_password.html',
                            title='Auth',
                            form_new_pwd=form_new_pwd)



@auth.route('/auth/logout')
@login_required
def logout():

    login = AuthLogin()
    login.offline_status()
    
    logout_user()

    return redirect(url_for('home.index'))



@auth.before_request
def _check():
    if check_current_user() and request.endpoint in ["auth.login", "auth.create", 'auth.recover', 'auth.auth_token', 'auth.new_pwd']:

        return redirect(url_for('profile.home'))
