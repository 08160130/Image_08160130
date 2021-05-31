"""西洋棋盤"""
import numpy as np
import math
import cv2

img = np.zeros([512,512,3],dtype = "uint8")

for i in range(0,8):
    for j in range(0,8):
        if(i%2==1):
            rectangleX = i*64
            rectangleY = j*64
            rectangleX2 = rectangleX +64
            rectangleY2 = rectangleY +64
            cv2.rectangle(img,(rectangleX,rectangleY),(rectangleX2,rectangleY2),(255,255,255),-1)
        if(j%2==1):
            rectangleX = i*64
            rectangleY = j*64
            rectangleX2 = rectangleX +64
            rectangleY2 = rectangleY +64
            cv2.rectangle(img,(rectangleX,rectangleY),(rectangleX2,rectangleY2),(255,255,255),-1)
            
for i in range(0,8):
    for j in range(0,8):
        if((i+j)%2==0):
            rectangleX = i*64
            rectangleY = j*64
            rectangleX2 = rectangleX +64
            rectangleY2 = rectangleY +64
            cv2.rectangle(img,(rectangleX,rectangleY),(rectangleX2,rectangleY2),(0,0,0),-1)

cv2.imshow("Chesstable",img)
cv2.waitKey(0)
cv2.imwrite("Chesstable.bmp",img)
cv2.destroyAllWindows()
