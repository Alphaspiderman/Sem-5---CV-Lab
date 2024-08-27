import cv2
import numpy as np

# read input image
img = cv2.imread("static/SampleImage.jpg")

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply Gaussian blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# apply Sobel operator to detect edges in x and y directions
sobelx = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_8U, 0, 1, ksize=3)

# combine edges detected in x and y directions
sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("Partial Image", sobel)
sobel = sobel.astype(np.uint8)

# apply non-maximum suppression to thin out edges
canny = cv2.Canny(sobel, 100, 200)

# display original image and edge-detected image
cv2.imshow("Original Image", img)
cv2.imshow("Edge-Detected Image", canny)

# save edge-detected image
cv2.imwrite("output.jpg", canny)

# wait for user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
