import cv2

# path to xml which contains the face features
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('images/photo/sachin-2.jpg', 1)
# print(img.shape)

# convert gray images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# scalefactor dsecrease the size image upto 5% untill the face is found, smaller this vallue greater accuracy

for x, y, w, h in faces:
    # last argument of rectangle method is width size
    # first argument is image object
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


cv2.imshow("Beatest", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
