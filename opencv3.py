import cv2
import numpy as np

img = cv2.imread('Amathur.png', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150,150), (98, 220, 199), 15)
#the parameters to draw the line are (where i want the line, the starting point, the ending point, and then the color of the line)
#we can add an optional line width (15 here)

cv2.rectangle(img, (10,10), (150, 200), (199,163,195), 8)
#parameters are the same as the line

cv2.circle(img, (100,100), 50, (0,0,0), 5)
#parametrs are(where, the centre, the radius, color)
#a positive line width will make the circle line wider
#a negative line width will make the circle filled with the same color
cv2.circle(img, (100,100), 35, (0,0,0), -1)

#random polygons
pts = np.array([[10,10],[20,20],[65,98],[90,90],[15,87],[99,99]], np.int32)
#adding the points in a numpy array, converting the data to 32 bit data
## recommended by documentation od opencv if the code fails: pts= pts.reshape((-1,1,2))
#optional reshaping of the polygon
cv2.polylines(img, [pts], True, (90,90,90), 5 )
#a true here will join the first point to the last point, hence closing the polygon

#writing
font = cv2.FONT_HERSHEY_SIMPLEX
#we need to to define a font and choose from an inbuilt font
cv2.putText(img, 'HAHAHAHAHaa', (0, 30), font, 1, (200,245,11), 5, cv2.LINE_AA)
#LINE_AA gives an anti alias line which is good for curves
#(where, the content, the starting point, the font, the size, the color, the width of the letters
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()