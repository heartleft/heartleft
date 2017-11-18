from flask.ext.wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField("What is your name?",validators=[Required()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("username",validators=[Required()])
    password = PasswordField("password",validators=[Required()])
    submit = SubmitField("Submit")
