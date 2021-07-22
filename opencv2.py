import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#syntax to allow the webcam to capture video
#(0) means 1st webcam, (1) would be 2nd webcam. I only have 1 so ill be using (0) throughout


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter('output.avi', fourcc , 20.0, (640,480))
#output of the file
#(640.480) is the size of the video
while True:
    #creating an infinite loop
    ret, frame = cap.read()
    #return will give a true or false, and then we have a frame
    #ret can be replaces by a _

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #converting video color from blue,green,red to gray

    out.write(frame)
    #we use this when we want to write our output

    cv2.imshow('frame', frame)
    #calling opencv to show the defined variable frame, which is our captured video
    cv2.imshow('gray', gray)
    #calling to show a gray video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #we break the loop if we press 'q'

cv2.release()
out.release()
#need to release the camera because the next project won't run if our camera is still engaged in this code
cv2.destroyAllWindows()