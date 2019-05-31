import cv2
import numpy as np

sourceImg = cv2.imread('testing.jpg')
height, width, channels = sourceImg.shape
val = int(input("Enter your level of blur:"))
blurImg = cv2.blur(sourceImg, (val, val))
#blurImg = 5
hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)
blankCanvas = np.zeros((height, width, 3), np.uint8)
blankCanvas[:] = (0, 0, 0)

def main():

 #   sourceImg = cv2.imread('darkgreen.jpg')
    cv2.namedWindow("sourceImage");
    cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("sourceImage",sourceImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    generateThreshold()
    #paint([30, 12, 8, 4, 2])



def paint(maskImage):

    m = 0
    i = 0



    cv2.namedWindow("maskImage");
    cv2.moveWindow("maskImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("maskImage",maskImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.namedWindow("blankCanvas");
    # cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)
    # cv2.imshow("blankCanvas", blankCanvas)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for i in range(0, height, 7):  # for every col:
        for j in range(0, width, 7):  # For every row
            if np.any(maskImage[i, j] != [0, 0, 0]):
                cv2.circle(maskImage, (j, i), 3, (0, 0, 255), -1)


    cv2.namedWindow("maskImage");
    cv2.moveWindow("maskImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("maskImage",maskImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.namedWindow("sourceImage");
    # cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    # cv2.imshow("sourceImage",sourceImg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imshow("blankCanvas",blankCanvas)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    i = 0

    # while i < len(radii):
    #     print(radii[i])
    #     blurImg = cv2.blur(sourceImg, (radii[i], radii[i]))
    #     cv2.namedWindow("blurred image");
    #     cv2.moveWindow("blurred image", 40, 30)  # Move it to (40,30)
    #     cv2.imshow('blurred image', blurImg)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     i += 1



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

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print "Image is black"
        else:
            paint(masks[i])
        i += 1


    #blankCanvas = np.zeros((height,width,3), np.uint8)
    #blankCanvas[:] = (245, 245, 220)
    #final = black | white | gray | orange1 | orange2| yellow1 | yellow2 | lightgreen | darkgreen | lightcyan | darkcyan | lightblue | darkblue | lightred | darkred | lightpurple | darkpurple | lightpink | darkpink
    # final2 = black | white | gray
    # final3 = lightcyan | darkcyan | lightblue | darkblue
    # final4 = orange1 | orange2| yellow1 | yellow2
    # #cv2.imshow('final', final)
    # cv2.imshow('final2', final2)
    # cv2.imshow('final3', final3)
    # cv2.imshow('final4', final4)

    #cv2.imshow('og', img)
    # cv2.imshow('blurred image', blurImg)
    #
    # ##########################################################################
    # cv2.imshow('', black)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', white)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', orange1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', orange2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', yellow1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', yellow2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('lightgreen', lightgreen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('darkgreen', darkgreen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', lightred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', darkred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', lightblue)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', darkblue)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', lightcyan)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cv2.imshow('', darkcyan)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # # cv2.imshow("blankCanvas.jpg",blankCanvas)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()