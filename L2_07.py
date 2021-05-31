"""漸層直方圖"""
import numpy as np
import cv2

row = np.array([(i/2,i/2,i/2) for i in range(512)],dtype = "uint8")

img = np.repeat(np.array([row],dtype = "uint8"),100,axis=0)
cv2.imwrite('color_img.jpg',img)
cv2.imshow("image",img)
cv2.waitKey()
