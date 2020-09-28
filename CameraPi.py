#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL
from camera import VideoCamera

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

# Video Stream
def gen(camera):
    while(True):
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed',method=['GET','POST'])
def video_feed():
    """show video stream"""
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
