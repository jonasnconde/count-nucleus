import numpy as np
import cv2
import os, os.path

# paste your image path below. Load the provided 'image01.tif' as an exemple. 
imgDir = "image path"

# create the variable 'image' using OpenCV. As 'image01.tif' is colored, I used '1' as parameter (0 for grayscale).
image = cv2.imread(imgDir, 1)

# setting the lower and upper thresholds for each RGB channel. Note that OpenCV uses BGR order.
# as I used DAPI for nuclear staining, my upper value in Blue channel is maximum.
# those parameters are close to optimum for my images, it should be modified for different ones.
lower = np.array([10, 0, 8])
upper = np.array([225, 10, 100])

# create a mask so we can see which pixels were selected using the threshold.
mask = cv2.inRange(image, lower, upper)

# find the contours in the mask
_, contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("%d blue shapes were found!" % (len(contours)))
cv2.imshow("Mask", mask)
 
# loop over the contours, and filter based on the area size.
# the 120 value for area size is totally arbitrary! It will left out small dots due to stained dirt in your slide,
# and the nucleus that are not completely showed in the edges of your image.
total_nucleus = 0
for c in contours:
    area = cv2.contourArea(c)
    if int(area) > 120:
        print(area)
        # draw the contour and show it
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        
print("The number of cells in my microscopy figure is: ", total_nucleus)
print("Testing git")
