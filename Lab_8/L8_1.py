import cv2

cap = cv2.VideoCapture("sample.webm")
ret, frame = cap.read()
tracker = cv2.TrackerKCF_create()
bbox = cv2.selectROI("Frame", frame, True, False)
tracker.init(frame, bbox)
# Loop over the frames in the video
while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break
    ret2, bbox = tracker.update(frame)
    if ret2:
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == ord("q"):
        break
# Release resources
cap.release()
cv2.destroyAllWindows()
