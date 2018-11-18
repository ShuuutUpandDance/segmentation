# -*- coding: utf-8 -*-
import cv2

from tqdm import tqdm
from util import elements_gt_threshold

img = cv2.imread('90_4_down.jpg', 0)
h, w = img.shape

scale = 150 * 150
ratio_list = [1, 2/1, 1/2]
threshold = 0.05


def check(input, left, right, up, down):
    count = 0
    input_h, input_w = input.shape
    tal = int(input_h * input_w * threshold)
    for i in range(up, down):
        for j in range(left, right):
            if input[i, j] > 150:
                count += 1
                if count >= tal:
                    return (left, right, up, down)


if __name__ == '__main__':
    mid_hw = [(100, 50)]
    objects_count = 0
    h, w = img.shape

    result_list = []
    res_dict = {}
    for i in tqdm(range(h)):
        for j in range(w):
            # pool = Pool(processes=3)
            for hw in mid_hw:
                rect_h, rect_w = hw
                tal = rect_h * rect_w * threshold
                left = max(j - int(rect_w/2), 0)
                right = min(j + int(rect_w/2), w)
                up = max(i - int(rect_h / 2), 0)
                down = min(i + int(rect_h / 2), h)
                result = elements_gt_threshold(img[up:down, left:right], 150)
                # if j == 131 and i == 45:
                #     print(result)
                if result > tal:
                    objects_count += 1
                    res_dict[result / (rect_h * rect_w)] = (left, right, up, down)
                    # result_list.append(res_dict)
    print(objects_count)
    print(res_dict)
            #     result_list.append(pool.apply_async(func=check, args=(img_down, left, right, up, down)))
            # pool.close()
            # pool.join()
            # for result in result_list:
            #     value = result.get()
            #     if value is not None:
            #         print(value)
                    # rect_left, rect_right, rect_up, rect_down = value
                    # cv2.rectangle(img, (rect_up, rect_left), (rect_down, rect_right), (0, 0, 255), 3)
            #         objects_count += 1

    # cv2.imshow('a', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()