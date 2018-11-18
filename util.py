# -*- coding: utf-8 -*-
import numpy as np


def generate_random_pos():
    pos = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0),
           (-1, -1), (0, -1), (1, -1)]
    return pos[np.random.randint(0, 8)]


def elements_gt_threshold(matrix, threshold):
    count = 0
    h, w = matrix.shape
    for i in range(h):
        for j in range(w):
            if matrix[i, j] > threshold:
                count += 1
    return count