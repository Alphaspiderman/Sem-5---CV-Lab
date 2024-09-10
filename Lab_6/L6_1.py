import cv2

# Read the files into grayscale
img1 = cv2.imread("static/img_1.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("static/img_2.png", cv2.IMREAD_GRAYSCALE)
# create SIFT object
sift = cv2.SIFT_create()
# Detect SIFT features in both images
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)
# Create feature matcher
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
# Match descriptors of both images
matches = bf.match(desc1, desc2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)
# Draw first 50 matches
matched_img = cv2.drawMatches(
    img1, kp1, img2, kp2, matches[:50], img2, flags=2
)

# Show and save the image
cv2.imshow("image", matched_img)
cv2.imwrite("output.jpg", matched_img)
# Wait for user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
