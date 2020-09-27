#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL

app = Flask(__name__)

files = UploadSet('files', ALL)
app.config[
    'UPLOADED_FILES_DEST'] = r'/mnt/c/Users/Tom/Google Drive/Project/PiCamera/files'
configure_uploads(app, files)


@app.route('/File', methods=['GET', 'POST'])
def upload():
    filename = 'Choose File'
    if request.method == 'POST' and 'file' in request.files:
        filename = files.save(request.files['file'])
        return render_template('File.html', filename=filename)
    return render_template('File.html', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
