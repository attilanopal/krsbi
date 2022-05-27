import cv2

class Bola:
    def __init__(self, image, bolaLower=(1, 150, 186), bolaUpper=(30, 255, 255) ):
        self.image = image
        self.bolaLower = bolaLower
        self.bolaUpper = bolaUpper
        self.perintah = ""
        self.simpanperintah= ""
        self.run()
        self.center
        self.mask

    # function to get mask image
    def pre_proc_1(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(hsv, self.bolaLower, self.bolaUpper)
        self.mask = cv2.erode(self.mask, None, iterations=5)
        self.mask = cv2.dilate(self.mask, None, iterations=9)
        cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL, 
 		        cv2.CHAIN_APPROX_SIMPLE)[-2]
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
            self.center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 
            # only proceed if the radius meets a minimum size 
            if radius > 3: 
                # draw the circle and centroid on the frame, 
                # then update the list of tracked points 
                cv2.circle(self.image, (int(x), int(y)), int(radius), 
                    (80, 127, 255), 2)  
                cv2.circle(self.image, self.center, 5, (0, 0, 255), -1)
        else:
            self.center=(-1,-1)
            
    def run(self):
        self.get_countour()


