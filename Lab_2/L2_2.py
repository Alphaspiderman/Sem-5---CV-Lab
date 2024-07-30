import cv2
import numpy as np

img_file = "static/SampleImage.jpg"
img = cv2.imread(img_file)

# Convert input image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform log transformation
log_img = 20 * np.log(1 + gray_img)
log_img = log_img.astype(np.uint8)

# Display
result = cv2.hconcat([gray_img, log_img])
# Only resize for large images
cv2.imshow("Log transformation", cv2.resize(result, (1500, 500)))
cv2.imwrite("output_q2.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
