from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistationForm(FlaskForm):
    username = StringField('Имя пользователя',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirrm_password = PasswordField('Потдвердите пароль',
                                      validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Напомнить пароль')
    submit = SubmitField('Вход')