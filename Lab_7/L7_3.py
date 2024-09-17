import numpy as np
import cv2

# Read the input image
img = cv2.imread("static/SampleImage.jpg", 0)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Translated Image", dst)
cv2.imwrite("translated.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
