# -*- coding: utf-8 -*-
from multiprocessing import Pool
from tqdm import tqdm, trange
from time import time
from util import elements_gt_threshold
import numpy as np
import cv2

img = cv2.imread('90_4_down.jpg', 0)
print(img.shape)

x = 220
y = 68

left = x - 16
right = x + 16
up = y - 16
down = y + 16
print(img[up:down, left:right].shape)
count = elements_gt_threshold(img[up:down, left:right], 200)
print('count:', count)
print(count / (32*32))