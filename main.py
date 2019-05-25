# importing opencv CV2 module
import cv2
import numpy as np


sourceImg = cv2.imread('testing.jpg')
height, width, channels = sourceImg.shape;
cv2.imshow("sourceImage",sourceImg)

blurImg = cv2.blur(sourceImg, (5, 5))
cv2.imshow('blurred image', blurImg)

blankCanvas = np.zeros((height,width,3), np.uint8)
blankCanvas[:] = (245, 245, 220)
cv2.imshow("blankCanvas",blankCanvas)

cv2.waitKey(0)
cv2.destroyAllWindows()



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
# # if __name__ == "__main__":
# #     main()