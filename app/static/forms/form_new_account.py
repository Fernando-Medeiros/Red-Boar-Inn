from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import SubmitField, PasswordField, StringField

from app.models.user import User


class FormNewAccount(FlaskForm):
    username = StringField('Enter your username', validators=[DataRequired()])
    email = StringField('Enter your e-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Please enter a password', validators=[DataRequired(), Length(6, 20)])
    auth = PasswordField('Please confirm the password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Next')

    def validate_email(self, email):
        try:
            if User.query.all():
                if User.query.filter_by(email=email.data).first():
                    raise ValidationError('E-mail already registered. Sign up with another _email_ or login to continue.')
        except Exception:
            pass
