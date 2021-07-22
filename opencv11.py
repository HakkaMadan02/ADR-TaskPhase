import cv2
import numpy as np
#template matching

img_bgr = cv2.imread('RP stack.jpg')
#we set up our image, to be matched
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#converting colors from bgr to gray because we do the processing in grayscale version
template = cv2.imread('RP stack.jpg',0)
#loading our template, which we will use for matching
w, h = template.shape[::-1]
#here we define the width and height of the shape, followed by a syntax to get the width and height

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#result is the matched template, where we match the gray image with the template
#for htis we use the template matching co-efficient

threshold = 0.8
#here we set a match requirement of 80 percent, we can lower the match percentage to60,70,but then more matches would be found, which might not be identical to the template

loc = np.where( res >= threshold)
#we define the question's location, telling where the result is greater than or equal to the threshold of the template


for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,0,0), 2)
#making a loop where for all the locations matched, we want to draw a rectangle
#draw the rectangle on the image itself, the point, point 0 plus our defined width, point 1 plus our defined height
# we make the rectangle yellow(0.255,255), followed by the line thickness

cv2.imshow('Detected',img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows