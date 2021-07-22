import os
import cv2
import numpy as np

png_1_path = "/home/wangyuchen/project/clip/1_1619314680880310000.png"
png_2_path = '/home/wangyuchen/project/TZ/merge/res2.png'
img_1 = cv2.imread(png_1_path, cv2.IMREAD_UNCHANGED)
img_2 = cv2.imread(png_2_path, cv2.IMREAD_UNCHANGED)
print(img_1.shape)
b, g, r, a = cv2.split(img_1)
b1, g1, r1, a1 = cv2.split(img_2)

a2 = cv2.add(a, a1)
print(a2)