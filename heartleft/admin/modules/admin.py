from flask import render_template, make_response
import os
from heartleft.admin.config import ROOT_DIR


def hello_world():
    return "Hello world"


def index():
    return render_template('index.html')


def get_file(file_path):
    # FIXME(zpzhou): here need to implementation as a ftp.
    # if the file which need read is too large, it may cause memory exhausted
    abs_path = os.path.join(ROOT_DIR, file_path)
    print abs_path

    if os.path.exists(abs_path):
        resp = make_response(open(abs_path).read())
        return resp
