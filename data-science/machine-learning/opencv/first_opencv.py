import cv2

# colured image
img = cv2.imread('images/beatest.png', 1)

# black and white image
# img_1 = cv2.imread('images/beatest.png', 0)
# shape method for provide the size of image in row,column and rgb
# print(img.shape)
cv2.imshow("beatest", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
