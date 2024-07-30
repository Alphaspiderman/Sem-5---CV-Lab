import cv2

img_file = "static/SampleImage.jpg"
img = cv2.imread(img_file)

# Convert input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute negative of the grayscale image
neg = cv2.bitwise_not(gray)

# Display the input image and negative image
# Only resize for large images
cv2.imshow('Input Image', cv2.resize(img, (500, 500)))
cv2.imshow('Negative Image', cv2.resize(neg, (500, 500)))

# Pause
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('output_q1.jpg', neg)

cv2.destroyAllWindows()