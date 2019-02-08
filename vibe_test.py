# -*- coding: utf-8 -*-
import numpy as np
import os
import cv2
from tqdm import tqdm


def initial_background(img, N):
    I_pad = np.pad(img, 1, 'symmetric')  # 复制相邻的原值作为pad的值

    height = I_pad.shape[0]
    width = I_pad.shape[1]
    samples = np.zeros((N, height, width))

    # 对于每个点，从它的 8 个相邻点中以均匀分布随机采样 N 次，作为对应的背景模型
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for n in range(N):
                x, y = 0, 0
                while x == 0 and y == 0 :
                    x = np.random.randint(-1, 1)
                    y = np.random.randint(-1, 1)
                ri = i + x
                rj = j + y
                samples[n, i, j] = I_pad[ri, rj]

    samples = samples[:, 1: height-1, 1: width-1]
    return samples


def vibe_detection(img, samples, _min, N, R, PHI):
    height = img.shape[0]
    width = img.shape[1]
    segMap = np.zeros((height, width)).astype(np.uint8)

    for i in range(height):
        for j in range(width):
            count, index, dist = 0, 0, 0
            #  计算 t 时刻帧中 v(x) 与 t-1 时刻的 M(x) 的交集的势
            while count < _min and index < N:
                dist = np.linalg.norm(img[i, j] - samples[index, i, j])
                if dist < R:
                    count += 1
                index += 1
            if count >= _min:  # 交集的势超过了阈值，分类为背景，进入背景更新策略
                rand = np.random.randint(0, PHI-1)  # 时间下采样：以 1/PHI 的概率决定是否更新背景模型
                if rand == 0:
                    # rand = np.random.randint(0, N-1)  # 等概率更新背景模型中的某个点
                    # samples[i, j, rand] = I_gray[i, j]

                    # rand = np.random.randint(0, N-1)  # 背景扩张：更新 x 邻域中所有的背景模型
                    # if rand == 0:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            ri = i + x
                            rj = j + y
                            rand = np.random.randint(0, PHI - 1)
                            try:
                                samples[rand, ri, rj] = img[i, j]
                            except:
                                pass
            else:
                segMap[i, j] = 255
    return segMap, samples


rootDir = r'uw/uw4'
outDIr = 'uw/uw4_vibe/'
W = 600
H = 400

image_file = os.path.join(rootDir, os.listdir(rootDir)[0])
image = cv2.imread(image_file, 0)  # read as gray
image = cv2.resize(image, (W, H))

N = 20
R = 20
PHI = 16
_min = 1


bg_models = initial_background(image, N)

files_list = os.listdir(rootDir)
for i in tqdm(range(len(files_list))):
    # input_filename = 'I_SI_01-' + str(i) + '.jpg'
    input_filename = str(i + 154) + '.jpg'
    path = os.path.join(rootDir, input_filename)
    frame = cv2.imread(path)
    frame = cv2.resize(frame, (W, H))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    segMap, bg_models = vibe_detection(gray, bg_models, _min, N, R, PHI)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    segMap_morph = cv2.morphologyEx(segMap, cv2.MORPH_CLOSE, kernel)
    filename = str(i) + '.jpg'
    cv2.imwrite(outDIr + filename, segMap)
