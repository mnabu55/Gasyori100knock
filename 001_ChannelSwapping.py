import cv2

# Read image
img = cv2.imread("imori.jpg")
img_1 = img.copy()

# imread order b, g, r
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# switch to rgb
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.imshow("bgr", img_1)
cv2.imshow("rgb", img)
cv2.waitKey(0)
cv2.destoryAllWindows()


# cv2.waitKeys(0)
# cv2.destoryAllWindows()

