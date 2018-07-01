"""
Pythonで連番画像の読み込み
"""

import cv2
import numpy as np

for i in range(10):
    #1桁の場合(0, 1, 2)
    img = cv2.imread(str(i)+ "/Users/jimmy/Desktop/Python/.png", cv2.IMREAD_GRAYSCALE)
    #ゼロ埋め、3桁の場合（000001）
    img = cv2.imread({0:03d}.png".format(i), cv2.IMREAD_GRAYSCALE")


#連番ではないが、特定のディレクトリ内のファイルをすべて処理
import cv2
import numpy as np
import glob #use glob module

files = glob.glob("image/*") #拡張子を指定: file = glob.glob("image/*.png")
for f in files:
    img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
