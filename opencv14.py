import cv2
import numpy as np
from matplotlib import pyplot as plt
#brute force matching will sort the matches based on best matches
#trying to get matches with different angles, rotation, lighting, etc

img1 = cv2.imread('opencv-feature-matching-template.jpg',0)
#loading template image
img2 = cv2.imread('opencv-feature-matching-image.jpg',0)
#loading a tilted image of the same object, kept amongother objects
print(img1, img2)
#checking for none type

orb = cv2.ORB_create()
#orb is the detector we are setting up for feature recognition
# First it uses FAST to find keypoints, then applies a measure to find top N points among them
#It computes the intensity weighted centroid of the patch with located corner at center. The direction of the vector from this corner point to centroid gives the orientation.


kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
#key points and descriptors established to cpmpute the images

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#using brute force for matching using hamming method
#cross checking to establish a true condition
#Hamming distance is the number of elements that are not the same when two rows overlap
#default value is false, by setting to true we make it more strict. A match (1) will only be established if thr two poits are the closest. Otherwise all values remain 0


matches = bf.match(des1,des2)
#setting up matches for the descriptors
matches = sorted(matches, key = lambda x:x.distance)
#sorting the matches of the descriptors using lambda key, based on their distance
#it will prioritize from most likely a match to least likely a match

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
#drawing lines between the matches
#specifying 10 number of matches, a bigger number like 20 might lead to matches outside the object, now the template might match to points on other objects which are not true.
#basically setting up a bigger number will lead to a lot of false positives

plt.imshow(img3)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows