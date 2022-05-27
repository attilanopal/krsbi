'''
    class gawang python
    auth : 
        - sufyan saori
'''
import cv2

class Gawang:
    def __init__(self, image, gawangLower=(60, 0, 200), gawangUpper=(255, 100, 255) , lawanLower=(0,0,0) , lawanUpper=(0,0,0) ) :
        self.image = image
        self.gawangLower = gawangLower
        self.gawangUpper = gawangUpper
        self.lawanLower = lawanLower
        self.lawanUpper = lawanUpper
        self.batas_kiri = 0
        self.batas_kanan = 0
        self.gawang = False
        self.run()

    # function to get mask image
    def pre_proc_1(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.gawangLower, self.gawangUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 
 		        cv2.CHAIN_APPROX_SIMPLE)[-2]
        return cnts

    # check tiang                     
    def persegi_panjang_berdiri (self, x, y, w, h):
        check1 = abs((y+h) - y)   > abs((x+w) - x)
        check2 = w/h
        if ( check1):
            if ( check2 < 0.35):
                return True
        return False

    # draw and get outer midle points (x, y)
    def draw_points(self, coord, batas, flag):
        font = cv2.FONT_HERSHEY_SIMPLEX
        x,y,w,h = coord
        center_circle = batas
        text = "ujung"+flag
        cv2.rectangle(self.image, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(self.image,center_circle , 4, (0,0,255), -1)
        cv2.putText(self.image, text, center_circle, font, 0.5,(0,0,255),2,cv2.LINE_AA)

    # functtion to ger countour
    def get_countour(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cnts = self.pre_proc_1()
        if len(cnts)>1:
            # cari 2 blob terbesar
            tiangs = sorted(cnts, key=cv2.contourArea, reverse=True)[:2]
            # cari mana blob kanan dan kiri berdasarkan posisi x-nya
            rec1 = cv2.boundingRect(tiangs[0])
            rec2 = cv2.boundingRect(tiangs[1])
            if(rec1[0] > rec2[1]):
                pos = [rec2, rec1]
            pos = [rec1, rec2]
            # (x, ( y +(h//2)) ) ; 5//2 = 2 ; 5/2 = 2.5
            self.batas_kiri = (pos[0][0], (pos[0][1] + pos[0][3]//2) )
            self.draw_points(pos[0], self.batas_kiri, "kiri")

            # ( (x+w), ( (y +(h//2) )
            self.batas_kanan = ( (pos[1][0] + pos[1][2]),  (pos[1][1]+ (pos[1][3]//2)) )
            self.draw_points(pos[1], self.batas_kanan, "kanan")

            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lawanLower, self.lawanUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=6)
            cnts2 = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 
                    cv2.CHAIN_APPROX_SIMPLE)[-2]

            if(len(cnts2)>0 and pos[0][3] == pos[1][3]):
                self.gawang = True

        else:
            self.batas_kiri = 0
            self.batas_kanan = 0

    
    def run(self):
        self.get_countour()


