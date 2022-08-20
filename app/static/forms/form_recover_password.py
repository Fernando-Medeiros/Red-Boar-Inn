from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, SubmitField, PasswordField


class FormSendToken(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Token Reset')


class FormValidateToken(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    token = StringField('Token', validators=[DataRequired(), Length(50, 80)])
    submit = SubmitField('Confirm Token')


class FormNewPassword(FlaskForm):
    email_auth = StringField('Email address', validators=[DataRequired(), Email()])
    token_auth = StringField('Token', validators=[DataRequired(), Length(50, 80)])
    password = PasswordField('Please enter a password', validators=[DataRequired(), Length(6, 20)])
    auth = PasswordField('Please confirm the password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Confirm')
