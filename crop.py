# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('uw/uw1/241.jpg')
img_down = cv2.resize(img, (300, 168))

pos_mid = (95, 171, 15, 65)
# pos_right = (167, 241, 60, 110)

crop_mid = img_down[pos_mid[2]: pos_mid[3] + 1, pos_mid[0]:pos_mid[1] + 1]
# crop_right = img_down[pos_right[2]: pos_right[3] + 1, pos_right[0]:pos_right[1] + 1]

# cv2.imwrite('90_4_nms.jpg', crop_mid)
cv2.imshow('a', crop_mid)
# cv2.imshow('b', crop_right)
cv2.waitKey(0)
cv2.destroyAllWindows()