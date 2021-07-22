import cv2
import numpy as np

img = cv2.imread('bookpage.jpg', cv2.IMREAD_GRAYSCALE)
#we specified what image i sto be read in " "
#cv2.IMREAD_GRAYSCALE is the syntax for the gray filter. By default it is colored, if not specified, but it removes the alpha chanel
#alpha chanel is the degree of opaqueness
#full color has 3 values, BGR
#grayscale is easier to perform analysis on
#analysis can ve done on full color but it will take a lot more processing
#grayscale is 0, color is 1, unchanged is -1, we can use numbers to avoid long syntax

cv2.imshow('image', img)
#calling opencv to show the image in a pop up window, using a string name and a variable name for the image as defined above

cv2.waitKey(0)
#waits for any key to be pressed, then exists the image window

cv2.destroyAllWindows()
#destroying all windows as the name suggests

cv2.imwrite('bookpageGRAY.png', img)
#saving the image in the directory, same folder as the code.