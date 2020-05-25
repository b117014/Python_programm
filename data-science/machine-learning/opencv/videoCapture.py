import cv2
import time

video = cv2.VideoCapture(0)  # 0 for built in camera , 1 for external camera and 2 for third camera

# video.read() method returns two value first is boolean which specify the opencv are able to open web cam
# and second value is numpy array of frame of image
check, frame = video.read()
print(check)
print(frame)

time.sleep(2)
video.release()
