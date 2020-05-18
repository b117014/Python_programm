import cv2

# colured image
img = cv2.imread('images/beatest.png', 1)

# black and white image
img_1 = cv2.imread('images/beatest.png', 0)
print(img.shape)
