from gawang import Gawang
import cv2

image = cv2.imread('5020.jpg')
check = Gawang(image)
print(check.gawang, check.area_gawang)