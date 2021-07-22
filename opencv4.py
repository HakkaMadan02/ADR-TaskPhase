import cv2
import numpy as np

img= cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55,55]= [255,255,255] # Here we are modifying the pixel in the next line
px=img[55,55] # pixels can be modified
#refferencing a particular pixel, the location and the color value of the location

##print(px) to fint the color value
roi = img[100:150, 100:150]  #region of the image will show a matrix of all the pixels
#it is the sub image of the image
##print(roi)
#roi can be modified,
#img[100:150, 100:150] = [255, 255, 255] to make it a white square

watch_face= img[25:100, 100:150]
#taking a ROI, copying it with the given cordinates [y:y1, x:x1]
img[0:75, 0:50]= watch_face #roi
# pasting th above roi in a different space of the same cordinate difference

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()