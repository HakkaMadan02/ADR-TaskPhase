import cv2
import numpy as np
#we need to have some way to remove noise, be it background or foreground
#different lighting, different thresholds etc determine which filter suits us the best

cap = cv2.VideoCapture(0) ##opening my first webcam
while True:
    _, frame = cap.read()   ##_ is a value returened from a function which we dont need
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) ##for changing saturation.

    lower_blue = np.array([75, 50, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res= cv2.bitwise_and(frame, frame, mask=mask)
    #convulations are a 3 step phase: 1) We take two matrices of the same dimensions.2)We perform element by element multiplication. 3)we sum the elements together
    #depth in image is the number of channels in the colors, like rgb has 3 channels so a depth of 3
    #kernel is basically a small matrix which sits on the main big image and goes left-right, up-down, performing mathematical operations and hence convulsions


    kernel = np.ones((15,15), np.float32)/225
    #for convulations we make a kernel
    #numpy ones basically is a list of 1s
    # 15 by 15 pixels
    #float 32 is a data type for 32 bits
    #division is done by (15x15) which is 225 to make an average for the blur

    smoothed= cv2.filter2D(res, -1, kernel)
    #here we apply that kernel by using filter 2D
    #this is our simple blur
    # we can do a simpler blur by basically averaging the pixels
    #we're applying it to the result
    #this is applied per block of pixels
    #15x15square means a total of 225 pixels
    #2-D convulations: images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. LPF helps in removing noise, blurring images, etc. HPF filters help in finding edges in images.
    #working: keep the kernel above a pixel, add all the pixels below this kernel, take the average, and replace the central pixel with the new average value. This operation is continued for all the pixels in the image.

    blur= cv2.GaussianBlur(res, (15,15), 0)
    #w're applying it to the result
    #this is also of 15 by 15 pixels
    #any sharp edges in images are smoothed while minimizing too much blurring.
    #kernel width and height should have odd values and can be different.
    #if ksize is set as [0,0], the kernel then works on standard deviation (sigma).
    #sigma X is kernel standard deviation along x axis
    #sigma y is kernel standard deviation along y axis
    #the pixels nearest the center of the kernel are given more weight than those far away from the center. This averaging is done on a channel-by-channel basis, and the average channel values become the new value for the filtered pixel.
    #Gaussian blur has the effect of reducing the image's high-frequency components; a Gaussian blur is thus a low pass filter.


    median = cv2.medianBlur(res, 15)
    #median gives the best clarity so far, we applyy it to the result
    #it is the least noisy out of all 3
    # cv2.medianBlur() computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. This is highly effective in removing salt-and-pepper noise.
    #in median filtering the central element is always replaced by some pixel value in the image.

    bilateral= cv2.bilateralFilter(res, 15, 75, 75)
    #it leads to noise removal while preserving edges unlike gaussian filter where edges are also blurred
    #The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences
    #a Gaussian function of intensity differences ensures that only those pixels with intensities similar to that of the central pixel are included to compute the blurred intensity value.

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('averaging', smoothed) #kernel was to create a blur
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()