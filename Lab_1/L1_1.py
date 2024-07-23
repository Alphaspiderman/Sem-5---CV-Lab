import cv2

img_file = "static/SampleImage.jpg"

img = cv2.imread(img_file)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()