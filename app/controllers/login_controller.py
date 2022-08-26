from flask import render_template, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from random import randint

from app import bcrypt__, database__

from app.models.user import User

from app.static.forms.form_login import FormLogin
from app.static.forms.form_new_account import FormNewAccount
from app.static.forms.form_recover_password import FormSendToken, FormNewPassword, FormValidateToken


class LoginController:

    @staticmethod
    def login():
        form_ = FormLogin()

        if form_.validate_on_submit():

            if validate_login(form_.email.data, form_.password.data, form_.keep_on):

                next_page = request.args.get('next')

                if next_page:
                    return redirect(next_page)

                return redirect('/profile')

            else:
                flash('Incorrect email or password!', 'alert-danger')

        return render_template("home/forms_login_newacc/login.html",
                               form_=form_,
                               title='Login')

    @staticmethod
    def new_account():

        form_ = FormNewAccount()

        if form_.validate_on_submit():

            pwd_crypt = bcrypt__.generate_password_hash(form_.password.data)
            pwd_recover_crypt = bcrypt__.generate_password_hash(str(randint(1, 9999999999)))

            if not User.query.filter_by(email=form_.email.data).first():

                __user = User(
                    username=form_.username.data,
                    email=form_.email.data,
                    password=pwd_crypt,
                    token_recover_pwd=pwd_recover_crypt
                )

                if __user:

                    database__.create_all()
                    database__.session.add(__user)
                    database__.session.commit()

                    login_after_create_new_account(form_.email.data, form_.password.data)

                    return redirect('/profile')

                else:
                    flash('Please provide the correct data' 'alert-danger')
            else:
                flash('E-mail already registered, Please choose another email or reset your password.', 'alert-danger')

        return render_template("home/forms_login_newacc/new_account.html",
                               form_=form_,
                               title='New Account')

    @staticmethod
    def recover_password():

        form_ = FormSendToken()

        if form_.validate_on_submit():

            if send_email_(form_.email.data):

                flash('Check your email', 'alert-success')
                return redirect('/login/recover/validate-token')

            else:
                flash('Email not registered', 'alert-danger')

        return render_template("home/forms_recover_pwd/send_email.html",
                               form_=form_,
                               title='Recover Password/Send Email')

    @staticmethod
    def validate_token():

        form_new_pwd_ = FormNewPassword()
        form_validate_token_ = FormValidateToken()

        if form_validate_token_.validate_on_submit():

            if validate_token(form_validate_token_.email.data,
                              form_validate_token_.token.data):

                flash('Valid Token', 'alert-success')

                return render_template("home/forms_recover_pwd/new_password.html",
                                       title="Recover Password/Change Password",
                                       form_new_pwd_=form_new_pwd_, )

            else:
                flash('Token invalid', 'alert-danger')

        if form_new_pwd_.validate_on_submit():

            if change_new_password(form_new_pwd_.email_auth.data,
                                   form_new_pwd_.password.data,
                                   form_new_pwd_.token_auth.data):
                flash('Password changed successfully', 'alert-success')

                return redirect('/login')

            else:
                flash('Token or Email invalid', 'alert-danger')
                return redirect('/login/recover/validate-token')

        return render_template("home/forms_recover_pwd/validate_token.html",
                               title="Recover Password/Validate Token",
                               form_validate_token_=form_validate_token_)

    @staticmethod
    @login_required
    def logout():
        logout_user()
        return redirect("/")


# Func/Assistant
def __check_user_in_db(_email_: str) -> object | bool:
    try:
        _user_ = User.query.filter_by(email=_email_).first()
    except Exception as User_DoesNotExist:
        pass
    else:
        return _user_
    return False


# Login
def validate_login(_email_: str, password: str, remember_user: bool) -> bool:
    _user_ = __check_user_in_db(_email_)

    if _user_:
        _password = bcrypt__.check_password_hash(_user_.password, password)

        if _password:
            _remember_on = True if remember_user else False
            login_user(_user_, remember=_remember_on)
            return True

    return False


# New Account
def login_after_create_new_account(_email_: str, password: str):
    _user_ = __check_user_in_db(_email_)

    if _user_:
        _password = bcrypt__.check_password_hash(_user_.password, password)

        if _password:
            login_user(_user_, remember=False)


# Recover - Send Email for User if Email in DB
def send_email_(_email_: str) -> bool:
    _user_ = __check_user_in_db(_email_)

    if _user_:
        _token_pwd = _user_.token_recover_pwd
        connect_and_send_email(_email_, _token_pwd)
        return True

    return False


# Recover - Config Email and Message
def connect_and_send_email(_email_: str, _token_pwd: str):
    pass
    # body = """
    # <p>{}</p>
    # """.format(_token_pwd)
    #
    # server = smtplib.SMTP('smtp.gmail.com:587')
    # server.starttls()
    #
    # message = email.message.Message()
    # message['Subject'] = 'Recover Password'
    # message['From'] = 'contatestedeprojetos@gmail.com'
    # message['To'] = f'{_email_}'
    #
    # message.add_header('Content-Type', 'text/html')
    # message.set_payload(body)
    #
    # server.login(message['From'], '123456789')
    #
    # server.sendmail(
    #     message['From'], [message['To']], message.as_string().encode('utf-8'))
    # server.quit()


# Recover - Validate Token/Email
def validate_token(_email_: str, token_data: str) -> bool:
    _user_ = __check_user_in_db(_email_)

    if _user_:
        _token_pwd = _user_.token_recover_pwd

        if str(token_data) == str(_token_pwd):
            return True

    return False


# Recover - Crypt and Update Password
def change_new_password(_email_: str, password: str, token_data: str) -> bool:

    if validate_token(_email_, token_data):

        _password = bcrypt__.generate_password_hash(password)

        User.query.filter_by(email=_email_).first().password = _password

        database__.session.commit()

        return True

    return False
