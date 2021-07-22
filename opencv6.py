##thresholding is extreme simplification of an image
import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
#12 is our threshold. pixel values above 12 are white, otherwise black


grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(retval, 12, 255, cv2.THRESH_BINARY)
#now applying threshold to the gray image

##making an adaptive threshold
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#max value is 255
#it is not a common threshold. The algorith determines different areas of different lightings
#now we get different thresholds for different areas in the image
#here we are using gaussian weighted sum of the neighboring values

retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Here the threshold value can be chosen arbitrary. The algorithm then finds the optimal threshold value which is returned as the first output.

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('Otsu threshold',threshold2)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()