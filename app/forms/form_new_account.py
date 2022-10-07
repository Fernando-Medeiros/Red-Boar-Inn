from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import PasswordField, StringField


class FormNewAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    charname = StringField('Charname', validators=[DataRequired()])
    email = StringField('Enter your e-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Enter a password', validators=[DataRequired(), Length(8, 20)])
    auth = PasswordField('Confirm the password', validators=[DataRequired(), EqualTo('password')])
