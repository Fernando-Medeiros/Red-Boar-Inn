from flask import render_template, current_app as app
from werkzeug.security import generate_password_hash

import os
import smtplib
import email.message
from random import randint


def send_mail(e_mail) -> bool:  
    
    __user: dict = app.db.USERS.find_one({'email': e_mail})

    if __user:
    
        body = render_template('/home/auth/template_email_recover.html',token=__user['token_pwd'])

        msg = email.message.Message()

        msg['Subject'] = "Recover Password - Red Boar Inn"
        msg['From'] = os.environ.get("MAIL_USERNAME")
        msg['To'] = e_mail

        password = os.environ.get("MAIL_PASSWORD") 

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        try:  
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        except:
            return
        else:
            return True



def validate_token(**kwargs) -> bool:
    
    __token: str = str(kwargs['token']).strip()
    
    if app.db.USERS.find_one({'token_pwd': __token}):
        return True


def new_pwd(**kwargs) -> bool:

    try:
        token_pwd: str = generate_password_hash(str(randint(1, 999999999999)))

        password: str = generate_password_hash(str(kwargs['password']).strip())

        if not password:
            raise ValueError() 

    except Exception as ErrorUpdatePassword:
        return

    else:
        app.db.USERS.find_one_and_update({'token_pwd': kwargs['token']},
        [
            {'$set': {'password': password}},
            {'$set': {'token_pwd': token_pwd}}
            ])

        return True