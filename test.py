# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np

img_fake = np.array(
    [
        [[1,2,3],
         [1,2,3],
         [1,2,3]],
        [[2,3,1],
         [2,3,1],
         [2,3,1]],
        [[3,1,2],
         [3,1,2],
         [3,1,2]]
    ]
)

pad = np.pad(img_fake, 1, 'symmetric')
pad = pad[:, :, 1:4]

print(pad.shape)
print(pad[1,1])
print(pad[2,2])
print(np.linalg.norm(pad[1,1] - pad[2,2]))