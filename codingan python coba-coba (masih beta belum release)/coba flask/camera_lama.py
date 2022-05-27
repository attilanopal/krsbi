import cv2
import multiprocessing
import serial
import time
import numpy as np
import serial
import struct
from queue import Queue
from gawang import Gawang
from check_bola import Bola

ds_factor=0.5

#warna magenta
magentaLower = (115, 100, 100) 
magentaUpper = (135, 255, 255) 

#warna cyan
cyanLower = (80, 100, 100) 
cyanUpper = (100, 255, 255) 

class VideoCamera(object):
    def __init__(self):
        #capturing video
        self.video = cv2.VideoCapture(0)
        self.manager = multiprocessing.Manager()
        # self.ardu = serial.Serial('/dev/ttyUSB0', 9600)
        
        #init camera
        ret, frame = self.video.read()
        self.frames = self.manager.list()
        self.frames.append(frame)
        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        ret, jpeg1 = cv2.imencode('.jpg', frame)

        #variabel yang di multiprocessing
        self.jpeg = self.manager.list()
        self.jpeg.append(jpeg1)
        self.maskbola = self.manager.list()
        self.maskbola.append(jpeg1)
        # self.perintah1=self.manager.list()
        # self.perintah1.append("ok")
        # self.arduino = serial.Serial('/dev/ttyUSB0',9600)
        self.koordinatbola = self.manager.list()
        self.koordinatbola.append((0,0))
        self.jalan = self.manager.list()
        self.jalan.append(True)
        self.bola

    def __del__(self):
        #releasing camera
        self.video.release()

    def commandprocess(self):
        time.sleep(0.50)
        while True:
            if self.jalan[0]:
                print("robot jalan")
                # if (self.koordinatbola[0][0]>400):
                #     if(self.koordinatbola[0][1]>455):
                #         self.arduino.write(b'T')
                #     if(self.koordinatbola[0][1]<455):
                #         self.arduino.write(b'R')
                # elif(self.koordinatbola[0][0]<400 and self.koordinatbola[0][0]>200):
                #     if(self.koordinatbola[0][1]>455):
                #         self.arduino.write(b'T')
                #     if(self.koordinatbola[0][1]<455):
                #         self.arduino.write(b'F')
                # elif(self.koordinatbola[0][0]<200):
                #     if(self.koordinatbola[0][1]>455):
                #         self.arduino.write(b'T')
                #     if(self.koordinatbola[0][1]<455):
                #         self.arduino.write(b'L')
            else:
                print("robot berhenti")
                # self.arduino.write(b'S')

    def processing(self):
        #extracting frames
        while True:
            frame = self.frames[0]
            bola = Bola(image = frame, bolaLower=(0, 150, 100), bolaUpper=(35, 255, 255) )
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
            # print(bola.center)
            self.koordinatbola[0] = bola.center
            ret, jpeg1 = cv2.imencode('.jpg', frame)
            self.jpeg[0] = jpeg1
            ret, jpeg2 = cv2.imencode('.jpg', bola.mask)
            self.maskbola[0] = jpeg2
        
    def run(self):
        #extracting frames
        while True:
            ret, frame = self.video.read()
            self.frames[0] = frame
    
    def get_frame(self):
        return self.jpeg[0].tobytes()

    def get_mask(self):
        return self.maskbola[0].tobytes()