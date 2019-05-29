import cv2
import numpy as np



def main():
    print("main function")
    sourceImg = cv2.imread('testing.jpg')
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

    cv2.circle(blankCanvas,(100, 300), 100, (120, 100, 50), -1)
    # for i in range(width):  # for every col:
    #     for j in range(height):  # For every row
    #         blankCanvas[i, j] = (100, 100, 100)  # set the colour accordingly


    cv2.imshow("blankCanvas",blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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