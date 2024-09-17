import numpy as np
import cv2

# Read the input image
img = cv2.imread("static/SampleImage.jpg", 0)
rows, cols = img.shape
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))
cv2.imshow("Sheared Image", sheared_img)
cv2.imwrite("sheard.jpg", sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
