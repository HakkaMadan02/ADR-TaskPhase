import cv2
import numpy as np

cap = cv2.VideoCapture(0) ##opening my first webcam
while True:
    _, frame = cap.read()   ## _ is a value returened from a function which we dont need
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) ##for changing to hue,saturation,and value.
    #its just another color space
    #due to its nature, HSV is better to use for range purposes
    #H-is how much of the color is in existence, while Saturation is the intensity of that color
    #for example if we want blue color to pass while all other colors are converted to black, we need an entire range of blue to pass


    lower_blue= np.array([75,50,50])
    upper_blue= np.array([140,255,255])
    #we are not converting a specific color to hsv, because we want an entire range, not a single color

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #the mask will be everything which is within the range of our defined lower and upper parameters
    res= cv2.bitwise_and(frame, frame, mask=mask)
    #the parameters are(where, applied to the frame, where the mask equals to mask)
    #basically our result is applied in the frame, to the frame and where the mask is true
    #mask will be either 0 or 1. it will be (1) if in the range, hence white. otherwise(0) for out of range, and black
    #we need to restore the blue-ness by running a bitwise operation
    #how it woeks is that the mask will first make everything either black or white. Then that white part will take the value of my blue

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()