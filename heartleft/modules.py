from flask import render_template, flash
from forms import NameForm, LoginForm


def index():
    name = None 
    form = NameForm() 
    if form.validate_on_submit(): 
        name = form.name.data 
        flash("good name")
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "login success!"
    return render_template('login.html', form=form)
