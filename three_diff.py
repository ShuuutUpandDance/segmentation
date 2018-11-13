# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from tqdm import tqdm


rootDir = r'I_SI_01/I_SI_01'
outDIr = 'I_SI_01/output_three_diff/'

files_list = os.listdir(rootDir)
for i in tqdm(range(2, len(files_list) - 1)):  # 文件名标号是从 1 到 len
    current_filename = 'I_SI_01-' + str(i) + '.bmp'
    before_filename = 'I_SI_01-' + str(i - 1) + '.bmp'
    after_filename = 'I_SI_01-' + str(i + 1) + '.bmp'

    current_path = os.path.join(rootDir, current_filename)
    before_path = os.path.join(rootDir, before_filename)
    after_path = os.path.join(rootDir, after_filename)

    current_frame = cv2.imread(current_path, 0).astype(np.int32)
    before_frame = cv2.imread(before_path, 0).astype(np.int32)
    after_frame = cv2.imread(after_path, 0).astype(np.int32)

    diff1 = np.abs(np.subtract(current_frame, before_frame)).astype(np.uint8)
    diff2 = np.abs(np.subtract(current_frame, after_frame)).astype(np.uint8)

    diff1_bin = cv2.threshold(diff1, 3, 1, cv2.THRESH_BINARY)[1]
    diff2_bin = cv2.threshold(diff2, 3, 1, cv2.THRESH_BINARY)[1]

    diff = np.logical_and(diff1_bin, diff2_bin).astype(np.uint8)

    diff_morph = cv2.morphologyEx(diff, cv2.MORPH_CLOSE, (3, 3))
    diff_morph_visual = cv2.threshold(diff_morph, 0, 255, cv2.THRESH_BINARY)[1]

    filename = str(i) + '.jpg'
    cv2.imwrite(outDIr + filename, diff_morph_visual)





