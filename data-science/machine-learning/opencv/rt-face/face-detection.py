import cv2

train_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# select one image to predict the face

# img = cv2.imread('tony-stark.jpg')

webcam = cv2.VideoCapture(-1)

while True:

    # read current frame
    success_frame_read, frame = webcam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cordinates = train_face.detectMultiScale(gray_img)

    for (x, y, h, w) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('webcam', frame)
    key = cv2.waitKey(1)
    # press Q to quit the window
    if key == 81 or key == 113:
        break

webcam.release()

# must convert to grayscale image

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # detect face
#
# face_cordinates = train_face.detectMultiScale(gray_img)
#
# #
# for (x, y, w, h) in face_cordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#
# cv2.imshow('clever image', img)

# key = cv2.waitKey(1)
