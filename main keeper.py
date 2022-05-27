import cv2
import numpy as np
import serial
import time
from check_bola_keeper import Bola

ser = serial.Serial('/dev/ttyUSB0', 9600)
#ser = serial.Serial('COM', 9600)

# greenLower = (0, 208, 186)
# greenUpper = (47, 255, 255)

colorLower = (0, 208, 186) 
colorUpper = (47, 255, 255) 

magentaLower = (140, 100, 100) 
magentaUpper = (160, 255, 255) 

cyanLower = (80, 100, 100) 
cyanUpper = (100, 255, 255) 

# gawangLower = (85, 85, 90)
# gawangUpper = (150, 255, 255)

# colorLower = (-2, 100, 100) 
# colorUpper = (18, 255, 255) 

majucheck = False
mundurcheck = False
kiricheck = False
kanancheck = False
spinleftcheck = False
spinrightcheck = False
rotateleftcheck = False
rotaterightcheck = False
tendangcheck = False
do_nothing = False
num = 0
start = 0
dur = 0


cap = cv2.VideoCapture(0)

i=0

def periksa(start, dur2, do_nothing, x, dur):
    if x:
        start = time.time()
        return start, dur, doNothing(start,dur), False 
    else:
        return start, dur2, do_nothing, False 

def doNothing(start, x):
    end = time.time()
    print(end-start)
    if(end-start>=x):
        return False
    else:
        return True

while True:
    ret,frame = cap.read()

    bola = Bola(frame)

    # print(bola.lokasi_bola + bola.jarak_bola)
    
    if bola.perintah == "kanan":
        if i>30:
            if do_nothing==False:
                print("kanan")
                ser.write(b'R')
                start, dur, do_nothing, mundurcheck = periksa(start, dur, do_nothing, mundurcheck, 0.31)
                start, dur, do_nothing, majucheck = periksa(start, dur, do_nothing, majucheck, 0.31)
                start, dur, do_nothing, kiricheck = periksa(start, dur, do_nothing, kiricheck, 0.31)
                start, dur, do_nothing, spinleftcheck = periksa(start, dur, do_nothing, spinleftcheck, 0.31)
                start, dur, do_nothing, spinrightcheck = periksa(start, dur, do_nothing, spinrightcheck, 0.31)
                start, dur, do_nothing, rotateleftcheck = periksa(start, dur, do_nothing, rotateleftcheck, 0.31)
                start, dur, do_nothing, rotaterightcheck = periksa(start, dur, do_nothing, rotaterightcheck, 0.31)
                start, dur, do_nothing, tendangcheck = periksa(start, dur, do_nothing, tendangcheck, 0.00)
                kanancheck=True
            else:
                do_nothing=doNothing(start,dur)

    if bola.perintah == "kiri":
        if i>30:
            if do_nothing==False:
                print("kiri")
                ser.write(b'L')
                start, dur, do_nothing, majucheck = periksa(start, dur, do_nothing, majucheck, 0.31)
                start, dur, do_nothing, mundurcheck = periksa(start, dur, do_nothing, mundurcheck, 0.31)
                start, dur, do_nothing, kanancheck = periksa(start, dur, do_nothing, kanancheck, 0.31)
                start, dur, do_nothing, spinleftcheck = periksa(start, dur, do_nothing, spinleftcheck, 0.31)
                start, dur, do_nothing, spinrightcheck = periksa(start, dur, do_nothing, spinrightcheck, 0.31)
                start, dur, do_nothing, rotateleftcheck = periksa(start, dur, do_nothing, rotateleftcheck, 0.31)
                start, dur, do_nothing, rotaterightcheck = periksa(start, dur, do_nothing, rotaterightcheck, 0.31)
                start, dur, do_nothing, tendangcheck = periksa(start, dur, do_nothing, tendangcheck, 0.00)
                kiricheck=True
            else:
                do_nothing=doNothing(start,dur)
    
    if bola.perintah == "tendang":
        if i>30:
            if do_nothing==False:
                print("tendang")
                ser.write(b'T')
                start, dur, do_nothing, mundurcheck = periksa(start, dur, do_nothing, mundurcheck, 2.31)
                start, dur, do_nothing, majucheck = periksa(start, dur, do_nothing, majucheck, 2.31)
                start, dur, do_nothing, kiricheck = periksa(start, dur, do_nothing, kiricheck, 2.31)
                start, dur, do_nothing, kanancheck = periksa(start, dur, do_nothing, kanancheck, 2.31)
                start, dur, do_nothing, spinleftcheck = periksa(start, dur, do_nothing, spinleftcheck, 2.31)
                start, dur, do_nothing, spinrightcheck = periksa(start, dur, do_nothing, spinrightcheck, 2.31)
                start, dur, do_nothing, rotateleftcheck = periksa(start, dur, do_nothing, rotateleftcheck, 2.31)
                start, dur, do_nothing, rotaterightcheck = periksa(start, dur, do_nothing, rotaterightcheck, 2.31)
                start, dur, do_nothing, tendangcheck = periksa(start, dur, do_nothing, tendangcheck, 2.01)
                tendangcheck = True
            else:
                do_nothing=doNothing(start,dur)
    
    if bola.perintah == "maju":
        if i>30:
            if do_nothing==False:
                print("maju")
                ser.write(b'F')
                start, dur, do_nothing, mundurcheck = periksa(start, dur, do_nothing, mundurcheck, 0.31)
                start, dur, do_nothing, kiricheck = periksa(start, dur, do_nothing, kiricheck, 0.31)
                start, dur, do_nothing, kanancheck = periksa(start, dur, do_nothing, kanancheck, 0.31)
                start, dur, do_nothing, spinleftcheck = periksa(start, dur, do_nothing, spinleftcheck, 0.31)
                start, dur, do_nothing, spinrightcheck = periksa(start, dur, do_nothing, spinrightcheck, 0.31)
                start, dur, do_nothing, rotateleftcheck = periksa(start, dur, do_nothing, rotateleftcheck, 0.31)
                start, dur, do_nothing, rotaterightcheck = periksa(start, dur, do_nothing, rotaterightcheck, 0.31)
                start, dur, do_nothing, tendangcheck = periksa(start, dur, do_nothing, tendangcheck, 0.00)
                majucheck=True
            else:
                do_nothing=doNothing(start,dur)

    if bola.perintah == "berhenti":
        if i>30:
            if do_nothing==False:
                print("berhenti")
                ser.write(b'S')
                start, dur, do_nothing, majucheck = periksa(start, dur, do_nothing, majucheck, 0.31)
                start, dur, do_nothing, mundurcheck = periksa(start, dur, do_nothing, mundurcheck, 0.31)
                start, dur, do_nothing, kiricheck = periksa(start, dur, do_nothing, kiricheck, 0.31)
                start, dur, do_nothing, kanancheck = periksa(start, dur, do_nothing, kanancheck, 0.31)
                start, dur, do_nothing, spinleftcheck = periksa(start, dur, do_nothing, spinleftcheck, 0.31)
                start, dur, do_nothing, spinrightcheck = periksa(start, dur, do_nothing, spinrightcheck, 0.31)
                start, dur, do_nothing, rotateleftcheck = periksa(start, dur, do_nothing, rotateleftcheck, 0.31)
                start, dur, do_nothing, rotaterightcheck = periksa(start, dur, do_nothing, rotaterightcheck, 0.31)
                start, dur, do_nothing, tendangcheck = periksa(start, dur, do_nothing, tendangcheck, 0.00)
                # spinleftcheck=True
            else:
                do_nothing=doNothing(start,dur)

    cv2.imshow('frame',frame)
    # cv2.imwrite('opencv'+str(num)+'.jpg',frame)
    # num = num+1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i=i+1

cap.release()
ser.write(b'S')
ser.close()
cv2.destroyAllWindows()