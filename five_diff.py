# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from tqdm import tqdm


rootDir = r'uw/uw1'
outDIr = 'uw/uw1_diff_5/'
W = 600
H = 337

files_list = os.listdir(rootDir)
for i in tqdm(range(2, len(files_list) - 2)):
    f0_name = str(i + 151 - 2) + '.jpg'
    f1_name = str(i + 151 - 1) + '.jpg'
    f2_name = str(i + 151) + '.jpg'
    f3_name = str(i + 151 + 1) + '.jpg'
    f4_name = str(i + 151 + 2) + '.jpg'

    f0_path = os.path.join(rootDir, f0_name)
    f1_path = os.path.join(rootDir, f1_name)
    f2_path = os.path.join(rootDir, f2_name)
    f3_path = os.path.join(rootDir, f3_name)
    f4_path = os.path.join(rootDir, f4_name)

    f0 = cv2.imread(f0_path, 0)
    f0 = cv2.resize(f0, (W, H)).astype(np.int32)
    f1 = cv2.imread(f1_path, 0)
    f1 = cv2.resize(f1, (W, H)).astype(np.int32)
    f2 = cv2.imread(f2_path, 0)
    f2 = cv2.resize(f2, (W, H)).astype(np.int32)
    f3 = cv2.imread(f3_path, 0)
    f3 = cv2.resize(f3, (W, H)).astype(np.int32)
    f4 = cv2.imread(f4_path, 0)
    f4 = cv2.resize(f4, (W, H)).astype(np.int32)

    diff0 = np.abs(np.subtract(f0, f1)).astype(np.uint8)
    diff0_bin = cv2.threshold(diff0, 3, 1, cv2.THRESH_BINARY)[1]
    diff1 = np.abs(np.subtract(f1, f2)).astype(np.uint8)
    diff1_bin = cv2.threshold(diff1, 3, 1, cv2.THRESH_BINARY)[1]
    diff2 = np.abs(np.subtract(f2, f3)).astype(np.uint8)
    diff2_bin = cv2.threshold(diff2, 3, 1, cv2.THRESH_BINARY)[1]
    diff3 = np.abs(np.subtract(f3, f4)).astype(np.uint8)
    diff3_bin = cv2.threshold(diff3, 3, 1, cv2.THRESH_BINARY)[1]

    diff = np.logical_and(diff0_bin, diff1_bin)
    diff = np.logical_and(diff, diff2_bin)
    diff = np.logical_and(diff, diff3_bin)
    diff = diff.astype(np.uint8)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff_morph = cv2.morphologyEx(diff, cv2.MORPH_CLOSE, kernel)
    diff_morph_visual = cv2.threshold(diff_morph, 0, 255, cv2.THRESH_BINARY)[1]

    filename = str(i) + '.jpg'
    cv2.imwrite(outDIr + filename, diff_morph_visual)





