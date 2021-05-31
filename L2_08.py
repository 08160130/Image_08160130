"""西洋棋盤"""
import numpy as np
import math
import cv2

T=10
M=512
img_H = np.zeros([512,512],dtype = "uint8")
img_V = np.zeros([512,512],dtype = "uint8")

for x in range(512):
    for y in range(512):
        img_H[x][y] = 128+(int)(math.sin(2*math.pi*x*T/M)*127)
        img_V[y][x] = 128+(int)(math.sin(2*math.pi*x*T/M)*127)
        
cv2.imshow("Exercise 8: Horizontal",img_H)
cv2.imshow("Exercise 8: Vertical",img_V)
cv2.waitKey(0)
cv2.destroyAllWindows()
