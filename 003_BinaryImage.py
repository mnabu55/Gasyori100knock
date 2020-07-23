import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")
img_origion = img.copy()
img = img.astype(np.float)

# この時点で２次元配列になっている
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

threshold = 128
out[out < threshold] = 0
out[out >= threshold] = 255

# Save result
cv2.imwrite("answer003.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()