import cv2
import numpy as np
from matplotlib import pyplot as plt
#corner detection

img= cv2.imread('grid.png')
#reading the image
print(img)
#checking for none type, or if the image is being processed

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#converting color for processing
gray= np.float32(gray)
#converting to float 32 data type. It will allocate 32 bit memory, allowing it to represent a dynamic range of numeric values.
print ('grey', gray)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#against gray, we are finding upto a 100 of these(100)
#(0.1) is the image quality
#(10) is the minimum distance between finding the corners
#When we specify the quality level, which is a value between 0-1, which denotes the minimum quality of corner below which everyone is rejected.
#Shifting a small window in any direction results in a large change in appearance, if that particular window happens to be located on a corner.
#If there’s an edge, then there will be no major change along the edge direction. But the corner is detected when the edge pixels change significantly, that when the edge line takes a sharp turn
#it uses calculations in Taylor's expansion


corners= np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (200,0,200), -1)
# radius 3, and color to mark the corners i specified on my own to make a purple

#cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows