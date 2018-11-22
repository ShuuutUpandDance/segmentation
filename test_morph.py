# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('uw/uw1_diff_3/130.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

img_m = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img_m = cv2.morphologyEx(img_m, cv2.MORPH_OPEN, kernel)

cv2.imshow('m', img_m)
cv2.waitKey(0)
cv2.destroyAllWindows()