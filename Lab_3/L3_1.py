import cv2
import numpy as np

img = cv2.imread("static/SampleImage.jpg", 0)
#  Find width and height of image
row, column = img.shape
#  Create an zeros array to store the sliced image
img1 = np.zeros((row, column), dtype="uint8")
#  Specify the min and max range
min_range = 80
max_range = 140
# Loop over the input image and if pixel value lies in desired range set it to 255
# otherwise set it to desired value
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = img[i - 1, j - 1]
cv2.imwrite("static/original.jpg", img)
cv2.imwrite("static/slicedimage.jpg", img1)
print("Files Saved")
