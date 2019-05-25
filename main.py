# importing opencv CV2 module
import cv2
import numpy as np


sourceImg = cv2.imread('testing.jpg')
height, width, channels = sourceImg.shape;

img = cv2.imread('testing.jpg')

val = int(input("Enter your level of blur:"))

blurImg = cv2.blur(sourceImg, (val, val))
#gray = cv2.cvtColor(blurImg,cv2.COLOR_BGR2GRAY)
#red = cv2.cvtColor(blurImg,cv2.COLOR_BGR2RGB)
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

####################################################
hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
imask = mask>0
green = np.zeros_like(blurImg, np.uint8)
green[imask] = blurImg[imask]
cv2.imwrite("green.png", green)
####################################################
mask = cv2.inRange(hsv, (120, 25, 25), (270, 255, 255))
imask = mask>0
pink = np.zeros_like(blurImg, np.uint8)
pink[imask] = blurImg[imask]
cv2.imwrite("pink.png", pink)
####################################################
mask = cv2.inRange(hsv, (10, 25, 25), (30, 255, 255))
imask = mask>0
brown = np.zeros_like(blurImg, np.uint8)
brown[imask] = blurImg[imask]
cv2.imwrite("brown.png", brown)
#####################################################

cv2.imshow('og', img)
cv2.imshow('blurred image', blurImg)
cv2.imshow('green', green)
cv2.imshow('pink', pink)
cv2.imshow('brown', brown)

blankCanvas = np.zeros((height,width,3), np.uint8)

#blankCanvas[:] = (245, 245, 220)
#cv2.imshow("blankCanvas",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
