"""
Opencvの基本：
画像を読み込み、表示、保存、グレースケール化、カラーマップ、リサイズ、動画を再生する。
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image by channel 3
img = cv2.imread("/Users/jimmy/Desktop/Python/sample.png", cv2.IMREAD_COLOR)
# BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#resize the image
img = cv2.resize(img, (100, 200))

cv2.imwrite("/Users/jimmy/Desktop/Python/sample_out.png", img)

#show the image
#画像をグレースケール化、カラーマップ
plt.imshow(img, cmap="gray")
#show image's colorbar
plt.colorbar()
plt.show()


"""
動画を再生する
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("/Users/jimmy/Desktop/Python/Silicon.Valley.S05E04.mp4")

#動画が終わるまで繰り返し
while(cap.isOpened()):
    #フレームの取得
    ret, frame = cap.read()
    #表示
    cv2.imshow("image", frame)
    #qが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


