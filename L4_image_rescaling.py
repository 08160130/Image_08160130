""" 不同內差法比較 """
import numpy as np
import cv2

img = cv2.imread( "Baboon.bmp", 0 )
nr1, nc1 = img.shape[:2]
nr2, nc2 = nr1 // 4, nc1 // 4

#最近鄰內差法
img1 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_NEAREST )
img1 = cv2.resize( img1, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

#雙線性內差法
img2 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_LINEAR )

#最近鄰內差法
img2 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

#雙立方內差法 , 4-4 補點
img3 = cv2.resize( img, ( nr2, nc2 ), interpolation = cv2.INTER_CUBIC )

#最近鄰內差法
img3 = cv2.resize( img2, ( nr1, nc1 ), interpolation = cv2.INTER_NEAREST )

cv2.imshow( "Original Image", img )
cv2.imshow( "Nearest Neighbor", img1 )
cv2.imshow( "Bilinear", img2 )
cv2.imshow( "Bicubic", img3 )
cv2.waitKey( 0 )
