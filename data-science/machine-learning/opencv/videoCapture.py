import cv2
import time

video = cv2.VideoCapture(-1)  # 0 for built in camera , 1 for external camera and 2 for third camera

# video.read() method returns two value first is boolean which specify the opencv are able to open web cam
# and second value is numpy array of frame of image
check, frame = video.read()


time.sleep(2)
cv2.imshow("Capturee", frame)
cv2.waitKey(0)

cv2.destroyAllWindow()
video.release()
