""" 顯示影像資訊 """
import numpy as np
import cv2

filename=input("Please enter filename:")
img=cv2.imread(filename,-1)
nr,nc=img.shape[:2]
print("Number of Rows=",nr)
print("Number of Columns=",nc)
if img.ndim!=3:   """ 維度數3是彩色 """
    print("Gray-Lavel Image")
else:   """ 維度數2是灰階 """
    print("Color Image")
