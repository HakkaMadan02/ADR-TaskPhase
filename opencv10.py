import cv2
import numpy as runpy
#edge detection

cap = cv2.VideoCapture(0) ##opening my first webcam
while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    #2nd derivative of maximums gives 0, hence we can use 2nd derivative also to detect edges.
    #Since images are 2D, we would need to take the derivative in both dimensions.

    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    #Snowbel is based on the  fact  that in the  edge  area, the  pixel  intensity  shows a  "jump" or a high variation of intensity. Getting the first derivative of the intensity, we observe that an edge is characterized by a maximum

    edges= cv2.Canny(frame, 100, 200) ##increase the number to get only hard edges, to remove noise
    #canny works in 3 stages:
    #1. noise reduction by applyung gaussian filter of 5x5
    #2. we get sobel kernel to find gradiant derivatives along x and y axes. Edge gradient is found by taking a root over the sum of squares of Gx and Gy
    # gradient direction is always perpendicular to edges
    #3. after getting magnitude and direction of the gradient, a scan is done to remove unwanted pixels
    #cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    #cv2.imshow('horizontal', sobelx) ##show a horizontal gradient for laplacian
    #cv2.imshow('vertical', sobely) ## vertical gradient
    cv2.imshow('edge', edges)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()