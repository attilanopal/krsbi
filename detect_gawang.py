'''
    detect gawang logic 
        detect warna putih (done)
        detect ujung putih (done)
        kondisi bahwa dia gawang (  )
'''

import cv2


# gawangLower = (85, 85, 90)
# gawangUpper = (150, 255, 255)

gawangLower = (60, 0, 200)
gawangUpper = (255, 100, 255)


font = cv2.FONT_HERSHEY_SIMPLEX

image = cv2.imread('foto/opencv0.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask2 = cv2.inRange(hsv, gawangLower, gawangUpper)
mask2 = cv2.erode(mask2, None, iterations=2)
mask2 = cv2.dilate(mask2, None, iterations=2)
cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, 
 		cv2.CHAIN_APPROX_SIMPLE)[-2]
def persegi_panjang_berdiri (x, y, w, h):
    check1 = abs((y+h) - y)   > abs((x+w) - x)
    check2 = w/h
    if ( check1):
        if ( check2 < 0.35):
            return True
    return False

check_gawang = 0
area_gawang = [0, 0]
# for id, cnt in enumerate(cnts2):
#     x,y,w,h = cv2.boundingRect(cnt)
#     if (persegi_panjang_berdiri(x, y, w, h)):
#         text = 'tiang'+str(id)
#         cv2.putText(image, text,(x,h), font, 1,(255,255,255),2,cv2.LINE_AA)
#         cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.drawContours(image, cnt, 3, (0,0,255), 3)
#         area_gawang[check_gawang] = (x,h)
#         check_gawang += 1

for id, cnt in enumerate(cnts2):
    x,y,w,h = cv2.boundingRect(cnt)
    if (persegi_panjang_berdiri(x, y, w, h)):
        text = 'tiang'+str(id)
        cv2.putText(image, text,(x,h), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.drawContours(image, cnt, 3, (0,0,255), 3)
        area_gawang[check_gawang] = (x,h)
        check_gawang += 1
        if(check_gawang == 2):
            print("ada gawang", area_gawang)
            cv2.imshow('gawang',mask2)
        if(check_gawang==2):
            check_gawang = 0

# if(check_gawang == 2):
#     print("ada gawang", area_gawang)
#     cv2.imshow('gawang',mask2)

cv2.imshow('gawang',mask2)
cv2.imshow('asli',image)
cv2.imshow('hsv',hsv)
cv2.waitKey()
cv2.destroyAllWindows()