from flask import flash


class FlashLogin:
  
    def flash_error_auth_login(self):
        flash('Incorrect email or password!', self.alert_danger)


class FlashNewAccount:
  
    def flash_email_already_exists(self):
        flash(
            'E-mail already registered, Please choose another email or reset your password.',
            self.alert_danger)


    def flash_charname_already_exists(self):
        flash('Character name is already in use.', self.alert_danger)
    

    def flash_error_create_account(self):
        flash('Please provide the correct data', self.alert_danger)
        

class FlashRecover:
   
    def flash_email_sent(self):
        flash('Token sent! Check your mailbox.', self.alert_success)


    def flash_valid_token(self):
        flash('Valid Token! Choose your new password.', self.alert_success)


    def flash_password_changed_successfully(self):
        flash('Password changed successfully!', self.alert_success)


    def flash_email_does_not_exist(self):
        flash('Incorrect email!', self.alert_danger)


    def flash_invalid_email_or_token(self):
        flash('Incorrect email or token!', self.alert_danger) 


    def flash_invalid_password(self):
        flash('Invalid Password!', self.alert_danger)



class FlashMessages(
    FlashLogin,
    FlashNewAccount,
    FlashRecover):
    
    alert_danger = 'alert-danger'
    alert_success = 'alert-success'