
# 1.Start with Image or Video
"""動画を再生する"""
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

# 2.Drawing Function in Opencv

# 3.Mouse as a Paint-Brush

# 4.Track as the Color Palette

