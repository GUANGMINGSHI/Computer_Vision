"""
機械学習の前処理時、画像の明るさを揃えたい。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#draw image in new window, tuple of integers, default is none
plt.figure(figsize=(7, 7))

#read many image
for i in range(1, 4):
    img = cv2.imread("/Users/jimmy/Desktop/Python/mri" + str(i) + ".png", 0)

    plt.subplot(4, 3, i)
    #?what's this mean
    plt.imshow(img, clim=[0, 255])
    plt.colorbar()
    #?why one more
    plt.subplot(4, 3, i+3)
    plt.imshow(cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_GRAY2BGR))
    plt.colorbar()

    print(np.mean(img), np.std(img))
    img = (img - np.mean(img)) / np.std(img) * 16 + 64

    plt.subplot(4, 3, i+6)
    plt.imshow(img, clim=[0, 255])
    plt.colorbar()

    plt.subplot(4, 3, i+9)
    plt.imshow(cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_GRAY2BGR))
    plt.colorbar()
    
plt.imshow(img)
plt.show()
