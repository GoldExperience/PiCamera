#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
