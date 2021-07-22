import cv2
import numpy as np
from matplotlib import pyplot as plt
#fg extraction in the region of the image

img = cv2.imread('Amathur.png')
#specifying the image
print(img)
mask = np.zeros(img.shape[:2],np.uint8)
#np.zero is a shape, float data type which returns a new array of the defined shape and type, filled with zeroes

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#using and defining a same background and foreground model
rect = (30,150,700,600)
#choosing a rectangle on the image for extraction, defining the color range, and the x and y co-ordinates till where the processing has to be done
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
#Grab cut feature grabs out or extracts the foreground from the background within the rectangle parameters
#input parameters include our image, the mask, the rectangle for our main object, the bg and fg model, then the number of iteration to run, and then the mode type

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#Here the mask is changed as o and 2 pixels are converted to background and 1 and 3 pixels to the foreground

img = img*mask2[:,:,np.newaxis]
#we multiply the input image to the changed mask

plt.imshow(img)
plt.colorbar()
plt.show()