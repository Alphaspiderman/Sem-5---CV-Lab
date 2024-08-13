import cv2
import numpy as np

image_file = "static/SampleImage.jpg"
# Load image
img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
# Define kernel matrix
kernel = np.ones((5, 5), np.float32) / 25
# Apply mean filtering
mean_filtered = cv2.filter2D(img, -1, kernel)
# Apply median filtering
median_filtered = cv2.medianBlur(img, 5)
# Sharpen the image using the Laplacian operator
sharpened_image2 = cv2.Laplacian(img, cv2.CV_64F)
# Display filtered images
cv2.imshow("Original Image", img)
cv2.imshow("Mean Filtered Image", mean_filtered)
cv2.imshow("Median Filtered Image", median_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
