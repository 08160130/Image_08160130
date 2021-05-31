""" 顯示像素資訊 """
import numpy as np
import cv2

global img   #定義全域變數 img

"""副程式"""
def onMouse(event,x,y,flags,param):
    x,y=y,x   #注意！OpenCV x,y軸定義和一般x,y軸定義相反
    if img.ndim!=3:
        print("(x,y)=(%d,%d)"%(x,y),end=" ")
        print("Gray-Level=%3d"%img[x,y])
    else:
        print("(x,y)=(%d,%d)"%(x,y),end=" ")
        print("(R,G,B)=(%3d,%3d,%3d)"%(img[x,y,2],img[x,y,1],img[x,y,0]))   #R,G,B 也和一般相反

"""主程式"""
filename=input("Please enter filename:")  #輸入影像檔名
img=cv2.imread(filename,-1)   #讀取影像
cv2.namedWindow(filename)   #根據檔名建立視窗
cv2.setMouseCallback(filename,onMouse)   #滑鼠在視窗內就會回呼副程式
cv2.imshow(filename,img)
cv2.waitKey(0)
