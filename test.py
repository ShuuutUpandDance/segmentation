# -*- coding: utf-8 -*-
from multiprocessing import Pool
from tqdm import tqdm, trange
from time import time
from util import elements_gt_threshold
import numpy as np
import cv2

img = cv2.imread('90_4_down.jpg', 0)
print(img.shape)

x = 222
y = 70

left = x - 35
right = x + 35
up = y - 25
down = y + 25
print(img[up:down, left:right].shape)
count = elements_gt_threshold(img[up:down, left:right], 150)
print('count:', count)
print(count / (70*50))