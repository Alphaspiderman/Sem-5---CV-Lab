import cv2

video_file = "static/SampleVideo.mp4"

cap = cv2.VideoCapture(video_file)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break