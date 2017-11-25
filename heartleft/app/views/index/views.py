from flask import render_template, flash

from heartleft.app.common.forms import NameForm


def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        flash("good name")
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
