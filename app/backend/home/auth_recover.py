import email.message
import os
import smtplib

from flask import render_template

from ..database import Database


class AuthRecover(Database):

    def send_mail(self, e_mail) -> bool | None:  
        
        _user: dict =  self.db_find_one(find={'email': e_mail})

        if _user:

            token = _user['token_pwd']
            body = render_template('/home/views/auth/template_email_recover.html',token=token)

            msg = email.message.Message()

            msg['Subject'] = "Recover Password - Red Boar Inn"
            msg['From'] = os.getenv("MAIL_USERNAME", 'None')
            msg['To'] = e_mail

            password = os.getenv("MAIL_PASSWORD", 'None') 

            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            try:  
                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

            except:
                self.flash_email_does_not_exist()
               
            else:
                self.flash_email_sent()
                return True

        self.flash_email_does_not_exist()
        

    def validate_token(self, **kwargs) -> bool | None:
        
        _token: str = str(kwargs['token']).strip()
        
        if self.db_find_one(find={'token_pwd': _token}):

            self.flash_valid_token()
            return True
        
        self.flash_invalid_email_or_token()


    def new_pwd(self, **kwargs) -> bool | None:
        try:
            token_pwd: str = self.generate_token()
            password: str = self.generate_password(password=str(kwargs['password']).strip())

            if not password:
                raise Exception()

        except:
            self.flash_invalid_password()

        else:
            self.db_find_one_and_update_many(
                find={'token_pwd': kwargs['token']},
                update=[
                    {'password': password},
                    {'token_pwd': token_pwd}
                ])
            
            self.flash_password_changed_successfully()

            return True