import numpy as np
import cv2
import sys, os
from PIL import Image

#Use Image.open() to open iamge.Rather than imread of plt.
img_pil = Image.open("/Users/jimmy/Desktop/Python/1.tiff")

#Create a list
FITC = []

try:
    count = 30
    while count<=100:
        #Set the file current position
        img_pil.seek(count)
        
        #Convert list into array
        img = np.asarray(img_pil)
        
        #Information about the memory layout of the array.
        img.flags.writeable = True
        img = cv2.resize(img,(512,512))
        
        #Add array img to list
        FITC.append(img)
        count += 1
        print(count,end=",")
except EOFError:
    pass

FITC = np.array(FITC)
print(FITC.shape)
