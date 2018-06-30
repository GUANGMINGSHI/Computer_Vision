import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image by channel 3
imgBGR = cv2.imread("/Users/jimmy/Desktop/Python/sample.png", cv2.IMREAD_COLOR)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

cv2.imwrite("/Users/jimmy/Desktop/Python/sample_out.png", imgRGB)

#show the image
plt.imshow(imgRGB)
plt.show()
