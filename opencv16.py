import cv2
import numpy as np

# HAAR CASCADES
#these files have a lot of feature sets, each corresponding to a very specific kind of object

#defining the two cascadess, loading them
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray, 1.3,5) #minSize and maxSize represent the possible size of the object the
    #last two parameters are scalefactor and minNeighbors
    #The scaleFactor parameter determines a trade-off between detection accuracy and speed. The detection window starts out at size minSize, and after testing all windows of that size, the window is scaled up by scaleFactor and re-tested, and so on until the window reaches or exceeds maxSize.
    #minNeighbor works on window sliding, detecting windows one by one. this parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality.
    #there are positive data points where he face is detected
    #negative data points where the face is not detected in a window
    #applied on gray
    #theses window movements are done on 5 rectangular features: edge, line and four rectangle features
    #To obtain features for each of these five rectangular areas, we simply subtract the sum of pixels under the white region from the sum of pixels under the black region
    #Eye regions tend to be darker than cheek regions.
    #The nose region is brighter than the eye region.
    # given these five rectangular regions and their corresponding difference of sums, we can form features that can classify parts of a face.

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w , y+h), (255, 50, 0), 2)
        #drawn on the image, next parameters are the starting points and then the ending points
        #the last two parameters are color, line width, blue color in our case

        #we are going to find eyes only inside the region of the image where the face is in
        roi_gray= gray[y: y+h , x:x+w] # for processing
        roi_color= img[y: y+h , x:x+w] #for later

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    cv2.imshow('image', img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()