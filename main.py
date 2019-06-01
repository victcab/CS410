import cv2
import numpy as np
import random

sourceImg = cv2.imread('testing.jpg')
height, width, channels = sourceImg.shape
blurImg = sourceImg
blurSelection = 1
hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)
blankCanvas = np.zeros((height, width, 3), np.uint8)
blankCanvas[:] = (0, 0, 0)

def main():

    global blurImg

    cv2.namedWindow("sourceImage");
    cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("sourceImage", sourceImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    blurImg = cv2.blur(sourceImg, (blurSelection, blurSelection))
    generateThreshold()

    cv2.namedWindow("blankCanvas");
    cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)
    cv2.imshow("blankCanvas", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def paint(maskImage, spacing, dotSize):

    myList = []


    for i in range(0, height, spacing):  # for every col:
        for j in range(0, width, spacing):  # For every row
            if np.any(maskImage[i, j] != [0, 0, 0]):
                if (np.any(maskImage[i,j] != blankCanvas[i,j])):
                    myList.append([i,j])
                    # color = maskImage[i, j]
                    # intColor = np.array((int(color[0]), int(color[1]), int(color[2])))
                    # cv2.circle(blankCanvas, (j, i), dotSize, intColor , -1)
                else:
                    print "skip"


    random.shuffle(myList)
    a = 0

    if len(myList) != 0:
        while a < len(myList):
            print myList[a]
            b = myList[a][0]
            c = myList[a][1]
            color = maskImage[b, c]
            intColor = np.array((int(color[0]), int(color[1]), int(color[2])))
            cv2.circle(blankCanvas, (c, b), dotSize, intColor , -1)
            a += 1



def CreateColorRange(hlower, slower, vlower, hupper, supper, vupper):
    mask = cv2.inRange(hsv, (hlower, slower, vlower), (hupper, supper, vupper))
    imask = mask>0
    color = np.zeros_like(blurImg, np.uint8)
    color[imask] = blurImg[imask]
    return color

def generateThreshold():

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

    masks = [black, white, gray, orange1, orange2, yellow1, yellow2, lightgreen, darkgreen, lightcyan, darkcyan, lightblue, darkblue, lightpurple, darkpurple, lightpink, darkpink, lightred, darkred]

    i = 0


    cv2.namedWindow("blur");
    cv2.moveWindow("blur", 40, 30)  # Move it to (40,30)
    cv2.imshow("blur", blurImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            print i
            paint(masks[i], 20, 19)
        i += 1

    i = 0

    print "zero layer"
    cv2.namedWindow("zero layer");
    cv2.moveWindow("zero layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("zero layer", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            print i
            paint(masks[i], 15, 14)
        i += 1

    i = 0

    print "first layer"
    cv2.namedWindow("first layer");
    cv2.moveWindow("first layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("first layer", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            print i
            paint(masks[i], 10, 9)
        i += 1

    i =  0

    print "second layer"
    cv2.namedWindow("second layer");
    cv2.moveWindow("second layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("second layer", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            print i
            paint(masks[i], 7, 6)
        i += 1

    print "third layer"
    cv2.namedWindow("third layer");
    cv2.moveWindow("third layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("third layer", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    i =  0

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            print i
            paint(masks[i], 6, 5)
        i += 1

    print "fourth layer"
    cv2.namedWindow("fourth layer");
    cv2.moveWindow("fourth layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("fourth layer", blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()