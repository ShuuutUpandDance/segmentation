# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np

rootDir = r'uw/uw1'
outDIr = 'uw/uw1_vibe/'

image_file = os.path.join(rootDir, os.listdir(rootDir)[0])
image = cv2.imread(image_file, 0)  # read as gray
print(image.shape)

r = cv2.resize(image,(600, 337))
print(r.shape)
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()