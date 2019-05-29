# importing opencv CV2 module
import cv2
import numpy as np

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
black = CreateColorRange(0,0,0,0,0,0)
white = CreateColorRange(0,0,127.5,0,0,255)
gray = CreateColorRange(0,0,0,0,0,127.5)

orange1 = CreateColorRange(10, 75, 127.5, 22, 255, 255)
orange2 = CreateColorRange(10, 75, 0, 22, 255, 127.5)

yellow1 = CreateColorRange(22, 75, 127.5, 32, 255, 255)
yellow2 = CreateColorRange(22, 75, 0, 32, 255, 127.5)

lightgreen = CreateColorRange(40, 75, 127.5, 72, 255, 255)
darkgreen = CreateColorRange(40, 75, 0, 72, 255, 127.5)

lightcyan = CreateColorRange(82, 75, 127.5, 100, 255, 255)
darkcyan = CreateColorRange(82, 75, 0, 100, 255, 127.5)

lightblue = CreateColorRange(115, 75, 127.5, 125, 255, 255)
darkblue = CreateColorRange(115, 75, 0, 125, 255, 127.5)

lightred = CreateColorRange(161, 75, 127.5, 180, 255, 255)
darkred = CreateColorRange(161, 75, 0, 180, 255, 127.5)


#blankCanvas = np.zeros((height,width,3), np.uint8)

#cv2.imshow('og', img)
cv2.imshow('blurred image', blurImg)
#############################################################################
cv2.imshow('black', black)
cv2.imshow('white', white)
cv2.imshow('gray', gray)

cv2.imshow('orange1', orange1)
cv2.imshow('orange2', orange2)

cv2.imshow('yellow1', yellow1)
cv2.imshow('yellow2', yellow2)

cv2.imshow('lightgreen', lightgreen)
cv2.imshow('darkgreen', darkgreen)
cv2.imshow('lightred', lightred)
cv2.imshow('darkred', darkred)

cv2.imshow('lightblue', lightblue)
cv2.imshow('darkblue', darkblue)

cv2.imshow('lightcyan', lightcyan)
cv2.imshow('darkcyan', darkcyan)
#blankCanvas[:] = (245, 245, 220)
#cv2.imshow("blankCanvas",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite("brown.png", brown)



