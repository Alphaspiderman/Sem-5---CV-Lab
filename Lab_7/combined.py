import cv2
import numpy as np

# Read the input image
img = cv2.imread("static/SampleImage.jpg", 0)
rows, cols = img.shape

# Part A
angle = 45
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

# Part B
img_shrinked = cv2.resize(img, (250, 200), interpolation=cv2.INTER_AREA)
img_enlarged = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# Part C
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

# Part D
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

# Display and Save
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_img)
cv2.imwrite("rotated.jpg", rotated_img)

cv2.imshow("Scaled Image - Shrink", img_shrinked)
cv2.imshow("Scaled Image - Enlarge", img_enlarged)
cv2.imwrite("enlarged.jpg", img_enlarged)
cv2.imwrite("shrinked.jpg", img_shrinked)

cv2.imshow("Translated Image", dst)
cv2.imwrite("translated.jpg", dst)

cv2.imshow("Sheared Image", sheared_img)
cv2.imwrite("sheard.jpg", sheared_img)

# Wait on user
cv2.waitKey(0)
cv2.destroyAllWindows()
