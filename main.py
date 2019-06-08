#Library imports
import cv2
import numpy as np
import random

#Reading in image
sourceImg = cv2.imread('testing.jpg')
height, width, channels = sourceImg.shape
blurImg = sourceImg

#User options for blurring
print("1: No smoothing")
print("2: Medium smoothing")
print("3: High smoothing")
level = int(input("Please enter your level of smoothness: "))

if(level == 1):
    blurSelection = 1

elif(level == 2):
    blurSelection = 5

elif(level == 3):
    blurSelection = 10

else:
    blurSelection = 1

print(blurSelection)

hsv = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)
blankCanvas = np.zeros((height, width, 3), np.uint8)
blankCanvas[:] = (0, 0, 0)

def main():

    global blurImg

    cv2.namedWindow("sourceImage");
    cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("sourceImage", sourceImg)
    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    blurImg = cv2.blur(sourceImg, (blurSelection, blurSelection))
    generateThreshold()

    cv2.namedWindow("blankCanvas");
    cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)
    cv2.imshow("blankCanvas", blankCanvas)
    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def paint(maskImage, spacing, dotSize):

    #List created for pixel locations and color
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
                    print("skip")


    random.shuffle(myList)
    a = 0

    if len(myList) != 0:
        while a < len(myList):
            print(myList[a])
            b = myList[a][0]
            c = myList[a][1]
            color = maskImage[b, c]
            #intColor = np.array((int(color[0]), int(color[1]), int(color[2])))
            #print("INTCOLOR: ")
            #print(intColor)
            #intColor = intColor.astype(np.int32, copy=False)
            cv2.circle(blankCanvas, (c, b), dotSize, (int(color[0]),int(color[1]),int(color[2])), -1)
            a += 1



def CreateColorRange(hlower, slower, vlower, hupper, supper, vupper):
    mask = cv2.inRange(hsv, (hlower, slower, vlower), (hupper, supper, vupper))
    imask = mask>0
    color = np.zeros_like(blurImg, np.uint8)
    color[imask] = blurImg[imask]
    return color

def generateThreshold():

    mask = CreateColorRange(0,0,0,180,255,255)

    masks = [mask]

    i = 0

    cv2.namedWindow("blur");
    cv2.moveWindow("blur", 40, 30)  # Move it to (40,30)
    cv2.imshow("blur", blurImg)
    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print("Image is black")
        else:
            print(i)
            paint(masks[i], 20, 19)
        i += 1

    i = 0

    print("zero layer")
    cv2.namedWindow("zero layer");
    cv2.moveWindow("zero layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("zero layer", blankCanvas)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print("Image is black")
        else:
            print(i)
            paint(masks[i], 15, 14)
        i += 1

    i = 0

    print("first layer")
    cv2.namedWindow("first layer");
    cv2.moveWindow("first layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("first layer", blankCanvas)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print("Image is black")
        else:
            print(i)
            paint(masks[i], 10, 9)
        i += 1

    i =  0

    print("second layer")
    cv2.namedWindow("second layer");
    cv2.moveWindow("second layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("second layer", blankCanvas)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print("Image is black")
        else:
            print(i)
            paint(masks[i], 7, 6)
        i += 1

    print("third layer")
    cv2.namedWindow("third layer");
    cv2.moveWindow("third layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("third layer", blankCanvas)
    cv2.waitKey(500)
    cv2.destroyAllWindows()

    i =  0

    while i < len(masks):
        gray = cv2.cvtColor(masks[i], cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) == 0:
            print("Image is black")
        else:
            print(i)
            paint(masks[i], 6, 5)
        i += 1

    print("fourth layer")
    cv2.namedWindow("fourth layer");
    cv2.moveWindow("fourth layer", 40, 30)  # Move it to (40,30)
    cv2.imshow("fourth layer", blankCanvas)
    cv2.waitKey(500)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()