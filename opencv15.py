import cv2
import numpy as np

# its gonna find the changes from the pre frame and note that as foreground. where there are no changes will become backgrond
#it works well in cases of motion

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
#The output foreground mask as an 8-bit binary image.
#The value between 0 and 1. The background model is learnt. Algorithm uses some automatically chosen learning rate. 0 means that the background model is not updated at all, 1 means that the background model is completely reinitialized from the last frame.

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)



    #applying erosion to remove noise
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(fgmask, kernel, iterations=1)

    # cv2.imshow('original', frame)
    cv2.imshow(' fg', fgmask)
    cv2.imshow('lowNOISE', erosion)






    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()