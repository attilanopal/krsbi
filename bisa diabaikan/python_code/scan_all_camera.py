import cv2

index = -1
arr = []
while index<10:
    cap = cv2.VideoCapture(index)
    print(index, cap.read())
    index += 1
print(arr)