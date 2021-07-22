import cv2
import numpy as np

cap = cv2.VideoCapture(0) ##opening my first webcam
while True:
    _, frame = cap.read()

    retval, threshold = cv2.threshold(frame, 50, 210, cv2.THRESH_BINARY)
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval2, threshold2 = cv2.threshold(grayscaled, 50, 255, cv2.THRESH_BINARY)

    ##making a guardian threshold
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    cv2.imshow('original', frame)
    cv2.imshow('threshold', threshold)
    cv2.imshow('threshold2', threshold2)
    cv2.imshow('Adaptive threshold', th)








    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()