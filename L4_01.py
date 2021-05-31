import numpy as np
import cv2

img1 = cv2.imread( "lena.bmp", 0 )   #讀進一個圖片
nr2, nc2 = img1.shape[:2]   #讀圖片長寬


angle = eval( input( "Please enter angle: " ) )   #請輸入一個角度


rotation_matrix = cv2.getRotationMatrix2D( ( nr2 / 2, nc2 / 2 ), angle, 0.73 )   #((旋轉中心),角度,縮放大小)
img2 = cv2.warpAffine( img1, rotation_matrix, ( nr2, nc2 ) )   #warpAffine仿射轉換函式



cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Rotation", img2 )
cv2.waitKey( 
