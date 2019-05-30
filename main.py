# importing opencv CV2 module
import cv2
import numpy as np
#import matplotlib as mat

def CreateColorRange(hlower, slower, vlower, hupper, supper, vupper):
    mask = cv2.inRange(hsv, (hlower, slower, vlower), (hupper, supper, vupper))
    imask = mask>0
    color = np.zeros_like(blurImg, np.uint8)
    color[imask] = blurImg[imask]
    return color

img = cv2.imread('testing.jpg')
height, width, channels = img.shape
val = int(input("Enter your level of blur:"))
blurImg = cv2.blur(img, (val, val))
hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)

#######################################5#############
black = CreateColorRange(0,0,0,180,0,0)
white = CreateColorRange(0,0,127.5,180,25,255)
gray = CreateColorRange(0,0,0,180,25,127.5)

orange1 = CreateColorRange(10, 25, 127.5, 22, 255, 255)
orange2 = CreateColorRange(10, 25, 0, 22, 255, 127.5)

yellow1 = CreateColorRange(22, 25, 127.5, 32, 255, 255)
yellow2 = CreateColorRange(22, 25, 0, 32, 255, 127.5)

lightgreen = CreateColorRange(32, 25, 127.5, 82, 255, 255)
darkgreen = CreateColorRange(32, 25, 0, 82, 255, 127.5)

lightcyan = CreateColorRange(82, 25, 127.5, 115, 255, 255)
darkcyan = CreateColorRange(82, 25, 0, 115, 255, 127.5)

lightblue = CreateColorRange(115, 25, 127.5, 125, 255, 255)
darkblue = CreateColorRange(115, 25, 0, 125, 255, 127.5)

lightpurple = CreateColorRange(125, 25, 127.5, 141, 255, 255)
darkpurple = CreateColorRange(125, 25, 0, 141, 255, 127.5)

lightpink = CreateColorRange(141, 25, 127.5, 161, 255, 255)
darkpink = CreateColorRange(141, 25, 0, 161, 255, 127.5)

lightred = CreateColorRange(161, 25, 127.5, 180, 255, 255)
darkred = CreateColorRange(161, 25, 0, 180, 255, 127.5)

blankCanvas = np.zeros((height,width,3), np.uint8)
#blankCanvas[:] = (245, 245, 220)
#final = black | white | gray | orange1 | orange2| yellow1 | yellow2 | lightgreen | darkgreen | lightcyan | darkcyan | lightblue | darkblue | lightred | darkred | lightpurple | darkpurple | lightpink | darkpink
final2 = black | white | gray
final3 = lightcyan | darkcyan | lightblue | darkblue
final4 = orange1 | orange2| yellow1 | yellow2
#cv2.imshow('final', final)
cv2.imshow('final2', final2)
cv2.imshow('final3', final3)
cv2.imshow('final4', final4)

#cv2.imshow('og', img)
cv2.imshow('blurred image', blurImg)

##########################################################################
#cv2.imshow('', black)
#cv2.imshow('', white)
#cv2.imshow('', gray)

#cv2.imshow('', orange1)
#cv2.imshow('', orange2)

#cv2.imshow('', yellow1)
#cv2.imshow('', yellow2)

#cv2.imshow('lightgreen', lightgreen)
#cv2.imshow('darkgreen', darkgreen)

#cv2.imshow('', lightred)
#cv2.imshow('', darkred)

#cv2.imshow('', lightblue)
#cv2.imshow('', darkblue)

#cv2.imshow('', lightcyan)
#cv2.imshow('', darkcyan)

cv2.imshow("blankCanvas.jpg",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()




