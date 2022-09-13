import cv2 as cv
import numpy as n
from box import Box
from image_recognition import Image


'''print(Image.init_dict())
testimg = cv.imread('resources/units/intheory.png')
Image.compare(testimg, testimg)'''

'''img = cv.imread('resources/units/intheory.png')
un1 = img[100:100, 150:150]
img = img[174:235, 21:81]

cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    print("sayonara")'''

Image.cut_aoi(1)
Image.init_unitlist()
