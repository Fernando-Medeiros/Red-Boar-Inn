from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, SubmitField, BooleanField, PasswordField


class FormLogin(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    keep_on = BooleanField('Remember me')
    submit = SubmitField('Sign in')
