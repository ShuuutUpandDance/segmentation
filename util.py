# -*- coding: utf-8 -*-
import numpy as np


def generate_random_pos():
    pos = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0),
           (-1, -1), (0, -1), (1, -1)]
    return pos[np.random.randint(0, 8)]
