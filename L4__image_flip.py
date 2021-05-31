""" 影像翻轉 """
import numpy as np
import cv2

img = cv2.imread( "Baboon.bmp", -1 )

# (原始影像,翻轉,輸出影像)
img1 = cv2.flip( img, 0 )
img2 = cv2.flip( img, 1 )
#翻轉：0 為垂直翻轉 / 正值代表水平翻轉 / 負值代表雙方向

cv2.imshow( "Original Image", img )
cv2.imshow( "Flip Vertically", img1 )
cv2.imshow( "Flip Horizontally", img2 )
cv2.waitKey( 0 )
