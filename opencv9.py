import cv2
import numpy as np
#morphological transformations are operations based on image shape.
#They are performed on binary images
#one input is the img, the other is the kernel

cap = cv2.VideoCapture(0) ##opening my first webcam
while True:
    _, frame = cap.read()   ##_ is a value returened from a function which we dont need
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) ##for changing saturation.

    lower_blue = np.array([75, 50, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res= cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    #it erodes away the boundaries of foreground object
    #after the kernel slides, the pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (0). (00-0,01-0, 10-0, 11-1)
    #the thickness or size of the foreground object decreases or simply white region decreases in the image.
    #It is useful for removing small white noises


    dilation = cv2.dilate(mask, kernel, iterations=1)
    #Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. so 0 pixel only in the case of 00
    #it increases the white region in the image or size of foreground object increases.
    # Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it.
    #It is also useful in joining broken parts of an object.




    ## goal of opening is to remove false positives
    ## closing is to remove false negatives
    opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #opening is erosion followed by dilation

    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #closing is dilation followed by erosion
    #used in filling small holes in the foreground

    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    ##tophat is the difference between input image and the opening of an image
    ##blackhat is the difference between closing of the input image and the input image

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()