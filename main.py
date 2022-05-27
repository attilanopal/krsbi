import cv2
import serial
import time
from gawang import Gawang
from check_bola import Bola
import threading
import multiprocessing
from queue import Queue
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--no-arduino', action='store_true')
# args = vars(parser.parse_args())

noarduino=True

# if args.get('no-arduino',False):
    # noarduino=False

manager=multiprocessing.Manager() # untuk variable yang akan digunakan pada object multiprocessing
print(noarduino)
if noarduino:
    ser=None
else:
    print(noarduino)
    ser=serial.Serial('/dev/ttyUSB0', 9600) # object serial untuk komunikasi arduino
    #ser = serial.Serial('COM', 9600)

# greenLower = (0, 208, 186)
# greenUpper = (47, 255, 255)

# lupa yang color ini buat apa
colorLower = (0, 208, 186) 
colorUpper = (47, 255, 255) 

#warna magenta
magentaLower = (115, 100, 100) 
magentaUpper = (135, 255, 255) 

#warna cyan
cyanLower = (80, 100, 100) 
cyanUpper = (100, 255, 255) 

# gawangLower = (85, 85, 90)
# gawangUpper = (150, 255, 255)

# colorLower = (-2, 100, 100) 
# colorUpper = (18, 255, 255) 

#membuat variabel list perintah untuk memerintah arduino
perintah1=manager.list()
perintah1.append("ok") #memasukan string dulu supaya tinggal ubah-ubah index 0

cap = cv2.VideoCapture(0) # object kamera
ret,frame = cap.read() # mebaca satu frame kamera
frames=manager.list() # membuat varabel list perintah untuk list
frames.append(frame)# memasukan 1 frame dulu ke frames supaya tinggal ubah-ubah index 0

print(frame.shape)

def bacakamera(frames):
    while True:
        ret,frame = cap.read()
        frames[0]=frame

def perintah(perintah1,ser):
    time.sleep(0.50)
    perintah2=None
    while True:
        if perintah1[0]=="kanan":
            if perintah2!="kanan":
                print("kanan")
                if not noarduino:
                    ser.write(b'R')
                perintah2="kanan"
        if perintah1[0]=="kiri":
            if perintah2!="kiri":
                print("kiri")
                if not noarduino:
                    ser.write(b'L')
                perintah2="kiri"
        if perintah1[0]=="tendang":
            if perintah2!="tendang":
                print("tendang")
                if not noarduino:
                    ser.write(b'T')
                perintah2="tendang"
        if perintah1[0]=="maju":
            if perintah2!="maju":
                print("maju")
                if not noarduino:
                    ser.write(b'F')
                perintah2="maju"
        if perintah1[0]=="cari":
            if perintah2!="cari":
                print("cari")
                if not noarduino:
                    ser.write(b'S')
                perintah2="cari"

proses1=multiprocessing.Process(target=bacakamera,args=(frames,))
proses1.daemon=True
proses1.start()
proses=multiprocessing.Process(target=perintah,args=(perintah1,ser))
proses.daemon=True
proses.start()

num=0

while True:
    # if (not frames.empty()):
    # frame = frames.get()
    frame=frames[0]
    bola = Bola(image = frame, bolaLower=(0, 150, 100), bolaUpper=(35, 255, 255) )
    gawang = Gawang(image = frame, lawanLower = magentaLower , lawanUpper = magentaUpper)
    # print(gawang.gawang, gawang.area_gawang)
    # print(gawang.gawang, gawang.batas_kanan, gawang.batas_kiri)    
    
    perintah1[0]=bola.perintah

    cv2.imshow('frame',frame)
    # cv2.imwrite('./foto2/opencv'+str(num)+'.jpg',frame)
    # num = num+1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if proses.is_alive():
    proses.terminate()
if proses1.is_alive():
    proses1.terminate()
cap.release()
if not noarduino:
    ser.write(b'S')
    ser.close()
cv2.destroyAllWindows()
