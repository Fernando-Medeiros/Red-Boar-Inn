from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, BooleanField, PasswordField


class FormLogin(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 20)])
    remember = BooleanField('Remember me')
