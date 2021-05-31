""" 讀取 顯示圖像 """
import numpy as np
import cv2

img=cv2.imread(filename,-1)   #(檔案名稱,型態)-1 為讀取原始影像 / 0 為灰階 / 1 為彩色
cv2.imshow("Example",img)   #影像顯示在視窗內,視窗大小會隨影像大小自動調整
cv2.waitKey(0)   #等待(秒)按什麼鍵關閉視窗
cv2.destoryAllWindows()   #關閉所有視窗
