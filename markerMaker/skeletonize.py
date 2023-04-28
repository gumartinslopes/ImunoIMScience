import cv2
import numpy as np

img = cv2.imread('masks/1.png', cv2.IMREAD_GRAYSCALE)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
skeleton = cv2.ximgproc.thinning(img, None, cv2.ximgproc.THINNING_ZHANGSUEN)
cv2.imwrite('result_skeleton.png', skeleton)
