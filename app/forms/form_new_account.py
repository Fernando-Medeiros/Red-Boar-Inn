from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import SubmitField, PasswordField, StringField


class FormNewAccount(FlaskForm):
    username = StringField('Enter your username', validators=[DataRequired()])
    email = StringField('Enter your e-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Please enter a password', validators=[DataRequired(), Length(6, 20)])
    auth = PasswordField('Please confirm the password', validators=[DataRequired(), EqualTo('password')])
