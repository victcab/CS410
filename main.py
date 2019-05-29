# importing opencv CV2 module
import cv2
import numpy as np

def CreateColorRange(lowerlimit, upperlimit, color):
    mask = cv2.inRange(blurImg, (lowerlimit, 0, 0), (upperlimit, 204, 204))
    imask = mask>0
    color = np.zeros_like(blurImg, np.uint8)
    color[imask] = blurImg[imask]
    return color

img = cv2.imread('testing.jpg')
height, width, channels = img.shape;
val = int(input("Enter your level of blur:"))
blurImg = cv2.blur(img, (val, val))
#hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)

#gray = cv2.cvtColor(blurImg,cv2.COLOR_BGR2GRAY)
#red = cv2.cvtColor(blurImg,cv2.COLOR_BGR2RGB)
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#######################################5#############
#red = CreateColorRange(102, 255, 'red')

mask = cv2.inRange(blurImg, (0, 255, 0), (250, 255, 250))
imask = mask>0
red = np.zeros_like(blurImg, np.uint8)
red[imask] = blurImg[imask]

#orange = CreateColorRange(10, 20, 'orange')
#yellow = CreateColorRange(20, 30, 'yellow')
#green = CreateColorRange(30, 70, 'green')
#lightblue = CreateColorRange(70, 95, 'lightblue')
#darkblue = CreateColorRange(95, 135, 'darkblue')
#purple = CreateColorRange(135, 175, 'purple')

#mask = cv2.inRange(blurImg, (0, 0, 255), (255, 0, 255))
#imask = mask>0
#white = np.zeros_like(blurImg, np.uint8)
#white[imask] = blurImg[imask]

blankCanvas = np.zeros((height,width,3), np.uint8)
#cv2.imshow('og', img)
cv2.imshow('blurred image', blurImg)
cv2.imshow('red', red)
#cv2.imshow('orange', orange)
#cv2.imshow('yellow', yellow)
#cv2.imshow('green', green)
#cv2.imshow('lightblue', lightblue)
#cv2.imshow('darkblue', darkblue)
#cv2.imshow('purple', purple)
#cv2.imshow('white', white)

#blankCanvas[:] = (245, 245, 220)
#cv2.imshow("blankCanvas",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite("brown.png", brown)



