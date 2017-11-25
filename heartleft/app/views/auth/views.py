from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from heartleft.app.common.forms import LoginForm


def login():
    from heartleft.app.db.model import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid email or password, please confirm!')
    return render_template('login.html', form=form)


def logout():
    return "logout success!"
