# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import time
from multiprocessing import Pool

vibe_input = 'uw/uw2_vibe'
diff_input = 'uw/uw2_diff_3'

N = 3


def denoise(img, radius):
    h, w = img.shape
    for j in range(h):
        for k in range(w):
            left = max(k - radius, 0)
            right = min(k + radius, w - 1)
            up = max(j - radius, 0)
            down = min(j + radius, h - 1)

            count = 0
            for _j in range(up, down + 1):
                for _k in range(left, right + 1):
                    if img[_j, _k] > 200:
                        count += 1

            if count < 50:
                img[j, k] = 0
    return img


if __name__ == '__main__':

    for i in range(184, 184 + N):
        pool = Pool(processes=4)
        f0_name = str(i) + '.jpg'
        f1_name = str(i + 1) + '.jpg'
        f2_name = str(i + 2) + '.jpg'

        vibe_f0 = cv2.imread(os.path.join(vibe_input, f0_name), 0)
        vibe_f1 = cv2.imread(os.path.join(vibe_input, f1_name), 0)
        vibe_f2 = cv2.imread(os.path.join(vibe_input, f2_name), 0)

        diff_f0 = cv2.imread(os.path.join(diff_input, f0_name), 0)
        diff_f1 = cv2.imread(os.path.join(diff_input, f1_name), 0)
        diff_f2 = cv2.imread(os.path.join(diff_input, f2_name), 0)

        h, w = vibe_f0.shape
        for j in range(h):
            for k in range(w):
                # 补足慢目标
                if diff_f0[j, k] > 200 and diff_f1[j, k] > 200 and diff_f2[j, k] > 200:
                    vibe_f0[j, k] = 255
                # 消除幽灵
                if (vibe_f0[j, k] > 200 > diff_f0[j, k]) and (vibe_f1[j, k] > 200 > diff_f1[j, k]) \
                        and (vibe_f2[j, k] > 200 > diff_f2[j, k]):
                    vibe_f0[j, k] = 0

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # 闭运算：填充空洞
        vibe_f0 = cv2.morphologyEx(vibe_f0, cv2.MORPH_CLOSE, kernel)  # 《视频序列目标检测与跟踪》22-23页
        # 开运算：去除噪点
        vibe_f0 = cv2.morphologyEx(vibe_f0, cv2.MORPH_OPEN, kernel)

        # 进一步消除孤立白色块，多进程版本
        proc_list = []
        radius = 7
        start = time.time()
        proc_list.append(pool.apply_async(func=denoise, args=(vibe_f0[0: int(h / 2), 0: int(w / 2)], radius)))
        proc_list.append(pool.apply_async(func=denoise, args=(vibe_f0[0: int(h / 2), int(w / 2):], radius)))
        proc_list.append(pool.apply_async(func=denoise, args=(vibe_f0[int(h / 2): h, 0: int(w / 2)], radius)))
        proc_list.append(pool.apply_async(func=denoise, args=(vibe_f0[int(h / 2): h, int(w / 2): w], radius)))

        pool.close()
        pool.join()

        vibe_f0[0: int(h / 2), 0: int(w / 2)] = proc_list[0].get()
        vibe_f0[0: int(h / 2), int(w / 2):] = proc_list[1].get()
        vibe_f0[int(h / 2): h, 0: int(w / 2)] = proc_list[2].get()
        vibe_f0[int(h / 2): h, int(w / 2): w] = proc_list[3].get()
        end = time.time()

        filename = str(i) + '_4.jpg'
        cv2.imwrite(filename, vibe_f0)
        print('duration,', end - start)
    #     cv2.imshow(str(i), vibe_f0)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
