from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, PasswordField


class FormSendToken(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])


class FormValidateToken(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    token = PasswordField('Token', validators=[DataRequired(), Length(30, 255)])


class FormNewPassword(FlaskForm):
    password = PasswordField('Please enter a password', validators=[DataRequired(), Length(8, 20)])
    auth = PasswordField('Please confirm the password', validators=[DataRequired(), EqualTo('password')])
