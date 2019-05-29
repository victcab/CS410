# importing opencv CV2 module
import cv2
import numpy as np

def CreateColorRange(hue, sat, val):
    mask = cv2.inRange(blurImg, (hue-10, sat-10, val-10), (hue+10, sat+10, val+10))
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
green = CreateColorRange(60, 100, 50)
#orange = CreateColorRange(
#yellow = CreateColorRange(
#green = CreateColorRange(
#lightblue = CreateColorRange(
#darkblue = CreateColorRange(
#purple = CreateColorRange(

#blankCanvas = np.zeros((height,width,3), np.uint8)

#cv2.imshow('og', img)
cv2.imshow('blurred image', blurImg)
#cv2.imshow('red', red)
#cv2.imshow('orange', orange)
#cv2.imshow('yellow', yellow)
cv2.imshow('green', green)
#cv2.imshow('lightblue', lightblue)
#cv2.imshow('darkblue', darkblue)
#cv2.imshow('purple', purple)
#cv2.imshow('white', white)

#blankCanvas[:] = (245, 245, 220)
#cv2.imshow("blankCanvas",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite("brown.png", brown)



