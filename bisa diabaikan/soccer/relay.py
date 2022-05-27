import cv2
cap = cv2.VideoCapture(1)
while cap.isOpened():
	ret,frame = cap.read()
	cv2.imshow("webcam", frame)
	if key == ord("q"):
        	break
