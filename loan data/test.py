import numpy as np
import cv2
import time
img = cv2.imread('feature_corr.png')
print(type(img))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
