import cv2
import numpy as np



def main():
    print("main function")
    sourceImg = cv2.imread('darkgreen.jpg')
    paint(sourceImg, [30, 12, 8, 4, 2])


def paint(sourceImg, radii):

    i = 0

    height, width, channels = sourceImg.shape;
    cv2.namedWindow("sourceImage");
    cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("sourceImage",sourceImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    blankCanvas = np.zeros((height,width,3), np.uint8)
    blankCanvas[:] = (0, 0, 0)
    cv2.namedWindow("blankCanvas");
    cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)


    for i in range(0, height, 7):  # for every col:
        for j in range(0, width, 7):  # For every row
            #color = tuple(blankCanvas[300, 300])
            #blankCanvas[j, i] = (255, 255, 255)  # set the colour accordingly

             if np.any(sourceImg[i,j] != [0, 0, 0]):
                 cv2.circle(sourceImg, (j, i), 3, (0, 0, 255), -1)
            #     cv2.circle(blankCanvas, (j, i), 10, (0, 0, 255), -1)


    # cv2.imshow("blankCanvas",blankCanvas)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cv2.imshow("dots",sourceImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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




# def paint(sourceImg, radii):
#
#     i = 0
#
#     height, width, channels = sourceImg.shape;
#     cv2.namedWindow("sourceImage");
#     cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
#     cv2.imshow("sourceImage",sourceImg)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
#     blankCanvas = np.zeros((height,width,3), np.uint8)
#     blankCanvas[:] = (255, 255, 255)
#     cv2.namedWindow("blankCanvas");
#     cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)
#
#     cv2.circle(blankCanvas,(100, 300), 100, (120, 100, 50), -1)
#
#     cv2.imshow("blankCanvas",blankCanvas)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
#     # while i < len(radii):
#     #     print(radii[i])
#     #     blurImg = cv2.blur(sourceImg, (radii[i], radii[i]))
#     #     cv2.namedWindow("blurred image");
#     #     cv2.moveWindow("blurred image", 40, 30)  # Move it to (40,30)
#     #     cv2.imshow('blurred image', blurImg)
#     #     cv2.waitKey(0)
#     #     cv2.destroyAllWindows()
#     #     i += 1

if __name__ == "__main__":
    main()