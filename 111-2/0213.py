import cv2
import numpy as np
arr = np.zeros((10,10,3))
cv2.imwrite("out.jpg",arr)
img = cv2.imread("out.jpg")
print(img.shape)