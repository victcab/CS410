# importing opencv CV2 module
import cv2
import numpy as np

def main():
    print("main function")
    sourceImg = cv2.imread('testing.jpg')
    paint(sourceImg, [28, 20, 12, 4])


def paint(sourceImg, radii):

    i = 0

    height, width, channels = sourceImg.shape;
    cv2.namedWindow("sourceImage");
    cv2.moveWindow("sourceImage", 40, 30)  # Move it to (40,30)
    cv2.imshow("sourceImage",sourceImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    blankCanvas = np.zeros((height,width,3), np.uint8)
    blankCanvas[:] = (245, 245, 220)
    cv2.namedWindow("blankCanvas");
    cv2.moveWindow("blankCanvas", 40, 30)  # Move it to (40,30)
    cv2.imshow("blankCanvas",blankCanvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    while i < len(radii):
        print(radii[i])
        blurImg = cv2.blur(sourceImg, (radii[i], radii[i]))
        cv2.namedWindow("blurred image");
        cv2.moveWindow("blurred image", 40, 30)  # Move it to (40,30)
        cv2.imshow('blurred image', blurImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        i += 1



 #   cv2.destroyAllWindows()



# # from PIL import Image
# # from PIL import ImageFilter
# cv2.waitKey()
# cv2.destroyAllWindows()


# def main():
#     # try:
#         # print("trying")
#         # # Relative Path
#         # img = Image.open("testing2.jpg")
#         #
#         #
#         # constantImage = Image.new('RGB', (500, 500), "black")
#         #
#         # blurred_image = img.filter(ImageFilter.GaussianBlur(radius=100))
#         # # pixels = img.load()  # create the pixel map
#         # #
#         # # for i in range(img.size[0]):  # for every col:
#         # #     for j in range(img.size[1]):  # For every row
#         # #         pixels[i, j] = (255, 255, 255)  # set the colour accordingly
#         #         #print(pixels[i,j])
#         #         #print("hi")
#         #
#         # img.show()
#         # constantImage.show()
#         # blurred_image.show()
#
#
#     # except IOError:
#     #     print("ERROR")
#     #     pass
#
# #

if __name__ == "__main__":
    main()