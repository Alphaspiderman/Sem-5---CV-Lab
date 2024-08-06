import cv2
import matplotlib.pyplot as plt

# Reading the image
img_data = cv2.imread("static/SampleImage.jpg")
img = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img_data, cv2.COLOR_RGB2GRAY)

# Setting the grid size
plt.figure(figsize=(20, 20))

# Plotting the original image
plt.subplot(221)
plt.title("Original")
plt.imshow(img)

# Plotting the histogram for the image
img_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title("Histogram 1")
plt.plot(img_hist)

# Plotting the histogram using the ravel function
plt.subplot(223)
plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Histogram 2")

# Applying the Histogram equalization using the cv2.equalizeHist() function
final_image = cv2.equalizeHist(gray)

# Displaying the image
# cv2.imshow("Histogram Equalization", final_image)
plt.subplot(224)
plt.title("Histogram Equalization")
plt.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
