import cv2
import numpy as np
from PIL import Image
# 1. inpute images
img1 = cv2.imread("/Users/jimmy/Desktop/cv/Homework/ps0/input/lbj.jpg")
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-1-a-1.jpg", img1)

img2 = cv2.imread("/Users/jimmy/Desktop/cv/Homework/ps0/input/mj.jpg")
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-1-a-2.jpg", img2)

# 2. Color planes
# swap the red and blue pixels: split() and merge()
img1_blue, img1_green, img1_red = cv2.split(img1)
img1 = cv2.merge((img1_red, img1_green, img1_blue))
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-2-a-1.jpg", img1)
# create a monochrome image
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-2-b-1.jpg", img1_green)
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-2-c-1.jpg", img1_red)

# 3. replacement of pixels.
height, width = img1.shape[:2]
x_offset = (width - 100) / 2;
y_offset = (height - 100) / 2;

img_with_center = img1_green.copy()
# why not image 2?
center = img1_red[int(y_offset):int(y_offset+100), int(x_offset):int(x_offset+100)]
# excellent!
img_with_center[int(y_offset):int(y_offset+100), int(x_offset):int(x_offset+100)] = center
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-3-a-1.jpg", img_with_center)


# 4.Arithmetic and Geometric operations
print("min pixels is:" + str(np.amin(img1_green)))
print("max pixels is:" + str(np.amax(img1_green)))
print("mean pixels is:" + str(np.mean(img1_green)))
print("standard deviation is:" + str(np.std(img1_green)))

calculated = (img1_green - np.mean(img1_green)) / np.std(img1_green) * 10 + np.mean(img1_green)
cv2.imwrite("/Users/jimmy/Desktop/cv/Homework/ps0/output/ps0-4-b-1.jpg", calculated)


テストのため追加
