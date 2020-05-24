import cv2

# path to xml which contains the face features
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('/images/beatest.png')

# convert gray images

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Beatest", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
