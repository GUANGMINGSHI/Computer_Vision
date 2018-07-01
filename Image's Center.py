# calculate the image's center
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Calculate is based on gray image
img = cv2.imread("/Users/jimmy/Desktop/Python/sample.jpg", cv2.IMREAD_GRAYSCALE)

# findContours(source image, contour retrieval mode, contour approximation method)
_, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 最大の輪郭構成点数をもつ輪郭を計算する
maxCont = contours[0]
for c in contours:
    if len(maxCont) < len(c):
        maxCont = c

# use "moments function" to calculate center
mu = cv2.moments(maxCont)
x,y = int(mu["m10"]/mu["m00"]), int(mu["m01"]/mu["m00"])

cv2.circle(img, (x, y), 4, 100, 2, 4)
plt.imshow(img)
plt.colorbar()
plt.show()
