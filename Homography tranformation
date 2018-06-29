import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

#画像を読み込み
img = cv2.imread('/Users/jimmy/Desktop/VAAK/image.png')

#画像の横と縦の長さ
rows,cols,ch = img.shape
print(img.shape)

#変換前の座標を入力
pts1 = np.float32([[52,250],[177,245],[0,480],[206,476]])

#変換後の座標を設定
pts2 = np.float32([[0,0],[270,0],[0,480],[270,480]])

#変換行列を生成
M = cv2.getPerspectiveTransform(pts1,pts2)
print(M)

"""
変換行列の逆行列を求める場合
invM = np.linalg.inv(M)
print(invM)
"""

#ホモグラフィ透視変換を行う
dst = cv2.warpPerspective(img,M,(270,480))

#read the file
csvfile = pd.read_csv(filepath_or_buffer="/Users/jimmy/Desktop/VAAK/Camera.csv", encoding="ms932", sep=",")
c = csvfile["pos_x"]
d = csvfile["pos_y"]

#
prev_point = None

#use for loop to calculate all of the data.
for i in range(len(c)):
    a = np.array([c[i], d[i], 1])
    b = np.dot(M, a)
    b = b / b[2]
    cv2.drawMarker(dst, (int(b[0]), int(b[1])), (0, 255, 0), markerType=cv2.MARKER_TILTED_CROSS, markerSize=5)
    if i > 0:
        cv2.line(dst, (int(prev_point[0]), int(prev_point[1])), (int(b[0]), int(b[1])), (255, 0, 0), 1)
    prev_point = b

#変換した画像を保存
cv2.imwrite('/Users/jimmy/Desktop/VAAK/out2.png', dst)

#変換した画像を表示
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
