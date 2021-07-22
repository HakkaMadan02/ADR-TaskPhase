#IMAGE ARITHEMATICS
import cv2
import numpy as np

img1 = cv2.imread('Amathur.png')
img2 = cv2.imread('mainlogo.png')
#img1=cv2.resize(img1, (126,126,))
#images need to be of the same size to add them


##addition operator
#add = img1+img2
#add1= cv2.add(img1,img2) ## this will add all pixel values together
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#choosing intensities per image to be added

#cv2.imshow('add', add1)
#cv2.imshow('add', add)
#cv2.imshow('add', weighted)

rows, cols, chanels = img2.shape
roi = img1[0:rows,0:cols]
# imposing img 2 on roi left top corner of img 1


img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#converting color
ret, mask = cv2.threshold(img2gray, 220, 225, cv2.THRESH_BINARY_INV) ##numbers represent minimum and maximum threshold value ## if above 220 it is converted to 255 otherwise it will be black
#all values below 220 will become black, all above valuws will be 225 as specified

mask_inv = cv2.bitwise_not(mask) #bitwise is a low level logical operator
#bitwise_or will run the statement if both the values are true or even if one value is true
#xor will run only if 1 value is true, it will give 0 output for both 1 inputs
img1_bg= cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg= cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg,img2_fg)
#adding img1 in the background and image 2 in the foreground
img1[0:rows, 0:cols] = dst

cv2.imshow('mask', mask)
cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)

#cv2.imshow('mask', mask) ##shows a black background on the python logo
cv2.waitKey(0)
cv2.destroyAllWindows()