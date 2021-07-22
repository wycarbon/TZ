import cv2
import os
import numpy as np

filename = []
all_path = []
file_and_name = {}
path = "/home/wangyuchen/project/TZ/merge4/"
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        filename.append(name)
        all_path.append(os.path.join(root, name))
# print(all_path)
# for i in range(0:500):
# print(a)

# png_1_path = "/home/wangyuchen/project/clip/1_1619314723002635000.png"  # 读者可自行修改文件路径
# png_2_path = "/home/wangyuchen/project/TZ/merge/res2.png"  # 读者可自行修改文件路径
def img_merge():
    j = 0
    for i in range(0,30):
        img_1 = cv2.imread(all_path[i + j], cv2.IMREAD_UNCHANGED)
        img_2 = cv2.imread(all_path[i + 1 + j], cv2.IMREAD_UNCHANGED)
        j = 2
        b, g, r, a = cv2.split(img_1)
        b1, g1, r1, a1 = cv2.split(img_2)
        a2 = cv2.bitwise_and(a, a1)
        a3 = cv2.bitwise_not(a)
        a4 = cv2.bitwise_not(a1)
        a5 = cv2.bitwise_and(a3, a4)
        a6 = cv2.bitwise_not(a5)
        a7 = cv2.bitwise_and(a3, a6)
        a8 = cv2.divide(a7, 255)
        a9 = cv2.bitwise_not(a7)
        a9 = cv2.divide(a9, 255)
        b = cv2.multiply(b, a9)
        g = cv2.multiply(g, a9)
        r = cv2.multiply(r, a9)
        b1 = cv2.multiply(b1, a8)
        g1 = cv2.multiply(g1, a8)
        r1 = cv2.multiply(r1, a8)
        n_b = cv2.add(b, b1)
        n_g = cv2.add(g, g1)
        n_r = cv2.add(r, r1)

        new_png = cv2.merge([n_b, n_g, n_r, a6])
        # cv2.imshow('result', new_png)
            # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
        # if cv2.waitKey(0) & 0xFF == 27:
        #     cv2.destroyAllWindows()
        cv2.imwrite('/home/wangyuchen/project/TZ/merge5/' + str(i) + '.png', new_png)

if __name__ == '__main__':
    img_merge()
