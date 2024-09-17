import numpy as np
import cv2

# Read the input image
img = cv2.imread("static/SampleImage.jpg", 0)
rows, cols = img.shape
img_shrinked = cv2.resize(img, (250, 200), interpolation=cv2.INTER_AREA)

img_enlarged = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Original Image", img)
cv2.imshow("Scaled Image - Shrink", img_shrinked)
cv2.imshow("Scaled Image - Enlarge", img_enlarged)
cv2.imwrite("enlarged.jpg", img_enlarged)
cv2.imwrite("shrinked.jpg", img_shrinked)
cv2.waitKey(0)
cv2.destroyAllWindows()
