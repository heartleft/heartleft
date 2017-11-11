from flask import render_template


def hello_world():
    return "Hello world"


def index():
    return render_template('index.html')
