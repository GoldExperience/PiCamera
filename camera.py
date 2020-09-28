#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor = 0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        """get frame"""
        success,frame = self.video.read()
        ret,jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()

    def get_frame_face_detector(self):
        success,frame = sel.video.read()
        frame = cv2.resize(frame,None,fx=ds_factor,fy = df_factor,interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            break

        ret,jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()
