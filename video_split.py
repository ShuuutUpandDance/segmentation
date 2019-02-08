# -*- coding: utf-8 -*-
import cv2

# 仍需手动停止，不知 bug 在哪
def getFrame(videoPath, svPath):
    cap = cv2.VideoCapture(videoPath)
    numFrame = 0

    flag = cap.isOpened()
    while flag:
        if cap.grab():
            flag, frame = cap.retrieve()
            #cv2.imshow('video', frame)
            numFrame += 1
            newPath = svPath + str(numFrame) + ".jpg"
            cv2.imencode('.jpg', frame)[1].tofile(newPath)


video_path = 'uw/uw4.mp4'
img_path = 'uw/uw4/'
getFrame(video_path, img_path)
