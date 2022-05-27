'''
    class gawang python
    auth : 
        - sufyan saori
        - benhard tamubolon
'''
import cv2

class Bola:
    def __init__(self, image, bolaLower=(1, 150, 186), bolaUpper=(30, 255, 255) ):
        self.image = image
        self.bolaLower = bolaLower
        self.bolaUpper = bolaUpper
        self.lokasi_bola = 0
        self.perintah = ""
        self.simpanperintah= ""
        self.run()

    # function to get mask image
    def pre_proc_1(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.bolaLower, self.bolaUpper)
        mask = cv2.erode(mask, None, iterations=5)
        mask = cv2.dilate(mask, None, iterations=9)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 
 		        cv2.CHAIN_APPROX_SIMPLE)[-2]
        cv2.imshow('mask',mask)
        return cnts

    # check tiang                     
    def persegi_panjang_berdiri (self, x, y, w, h):
        check1 = abs(h)   > abs(w)
        check2 = w/h
        if ( check1):
            if ( check2 < 0.35):
                return True
        return False

    # functtion to ger countour
    def get_countour(self):
        cnts = self.pre_proc_1()
        if len(cnts)>0 : 
            # find the largest contour in the mask, then use 
            # it to compute the minimum enclosing circle and 
            # centroid 
            c = max(cnts, key=cv2.contourArea) 
            ((x, y), radius) = cv2.minEnclosingCircle(c) 
            M = cv2.moments(c) 
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 
            # only proceed if the radius meets a minimum size 
            if radius > 10: 
                # draw the circle and centroid on the frame, 
                # then update the list of tracked points 
                cv2.circle(self.image, (int(x), int(y)), int(radius), 
                    (80, 127, 255), 2)  
                cv2.circle(self.image, center, 5, (0, 0, 255), -1)
            if int(M["m10"] / M["m00"]) > 400:
                self.lokasi_bola = int(M["m10"] / M["m00"])
                if int(M["m01"] / M["m00"]) > 455 :
                    self.perintah = "tendang"    
                if int(M["m01"] / M["m00"]) < 455:
                    self.perintah = "kanan"
            elif int(M["m10"] / M["m00"]) < 400 and int(M["m10"] / M["m00"]) > 200:
                self.lokasi_bola = int(M["m10"] / M["m00"])
                if int(M["m01"] / M["m00"]) > 455 :
                    self.perintah = "tendang"    
                if int(M["m01"] / M["m00"]) < 455:
                    self.perintah = "maju"
                # if i>10:
                #     ser.write(b'f')
            elif int(M["m10"] / M["m00"]) < 200:
                self.lokasi_bola = int(M["m10"] / M["m00"])
                if int(M["m01"] / M["m00"]) > 455 :
                    self.perintah = "tendang"    
                if int(M["m01"] / M["m00"]) < 455:
                    self.perintah = "kiri"
        
        else:
            self.perintah = "cari"

    
    def run(self):
        self.get_countour()


