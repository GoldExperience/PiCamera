#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './files/'
ALLOWED_EXTENTIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


def allowed_file(filena):
    """check the file type"""
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENTIONS


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
