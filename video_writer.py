# -*- coding: utf-8 -*-
import os
import cv2

# img_dir = 'I_BS_01/output/'
img_dir = 'I_BS_01/output_three_diff/'
start = 1
end = 275

img_size = (352, 288)
video_dir = 'I_BS_01/diff.avi'

fps = 30
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video_writer = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for i in range(start, end):
    filename = os.path.join(img_dir, str(i)+'.jpg')
    frame = cv2.imread(filename)
    video_writer.write(frame)

video_writer.release()
