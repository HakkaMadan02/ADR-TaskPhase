#steps to making HAAR cascade
#1. collection of background images, negatives: these are the images which we are not tracking
#2. collection of positive images: the object which we are tracking
#3. creating a positive vector file by stitching together all positives.
#4. train cascade for positives vs negatives. generally done by ML, but we will do by opencv

#descriptions
#1. for -ves, bg.txt is a file, neg/1.jpg is an image
#2. for +ves, pos.txt, pos/1.jpg 1 0 0 50 50 (parameters are image, number of objects, start point, rectangle cordinates

#negative images should be larger than positive images generally, if creating samples
#100x100 for-, 50x50 for+
#number of + should almost be double