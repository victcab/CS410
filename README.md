# Photo Paint Filter
Paint filter programming project made for CS410-ComputationalPhotography

## Creators
Alexandra Llamas, Victor Cabunoc

## Project Description
The purpose of this project is to "paint-ify" any image inputed into the program. An image goes in, runs through the algorithem, and comes out looking like a painting. The filter in this project is meant to mimic a [pointillism painting technique](https://en.wikipedia.org/wiki/Pointillism).

The algorithem used to create this paint filter was originally designed and built for this project. The creation of the alogorithem was inspired by research from an [NYU academic article](https://www.mrl.nyu.edu/publications/painterly98/hertzmann-siggraph98.pdf).

More details of the project can be found in our presentation slides [here](https://docs.google.com/presentation/d/e/2PACX-1vRfP7LQ6wCQURrrOj1DBEXZB11P9NosAy_BzbMuIBd9FL1vWTB3wTARsHWJvEKuLFB8CdTkKrlm6iIx/pub?start=false&loop=false&delayms=3000&slide=id.g5af439a97a_3_18).

## Running the Code
Before running, make sure you properly add the image you want to "paint-ify" to the project directory. Update line 5 of main.py to referance that image.

```
sourceImg = cv2.imread('yourImage.imgExt')
```
If this is not done, the program will automatically run with the testing.jpg image provided in the directory.

## License
This program is licensed under the "MIT License". Please see the file LICENSE in the source distribution of this software for license terms.
