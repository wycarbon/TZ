import cv2
import numpy as np


# def merge_img(png_1, png_2):
#     b, g, r, a = cv2.split(png_1)
#     b1, g1, r1, a1 = cv2.split(png_2)
#     # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
#     # alpha_2 = png_2[y1:y2, x1:x2, 3] / 255.0
#     # alpha_1 = 1 - alpha_2
#     a2 = cv2.bitwise_not(a1)
#     a3 = cv2.bitwise_and(a, a2)
#     a4 = cv2.bitwise_or(a1, a3)
#     a5 = a3 / 255.0
#     b = b * a5
#     g = g * a5
#     r = r * a5
#     a6 = cv2.bitwise_not(a5)
#     b1 = b1 * a6
#     g1 = g1 * a6
#     r1 = r1 * a6
#     n_b = cv2.add(b, b1)
#     n_g = cv2.add(g, g1)
#     n_r = cv2.add(r, r1)
#     new_png = cv2.merge([n_b, n_g, n_r, a4])
#     return new_png
#
# if __name__ == '__main__':
#     # 定义图像路径
#     png_1_path = "/home/wangyuchen/project/clip/1_1619314680880310000.png"  # 读者可自行修改文件路径
#     png_2_path = '/home/wangyuchen/project/TZ/merge/res1.png'  # 读者可自行修改文件路径
#
#     # 读取图像
#     img_1 = cv2.imread(png_1_path, cv2.IMREAD_UNCHANGED)
#     img_2 = cv2.imread(png_2_path, cv2.IMREAD_UNCHANGED)
#
#     # 设置叠加位置坐标
#     # x1 = 0
#     # y1 = 0
#     # x2 = x1 + img_2.shape[1]
#     # y2 = y1 + img_2.shape[0]
#
#     # 开始叠加
#     res_img = merge_img(img_1, img_2)
#
#     # 显示结果图像
#     cv2.imshow('result', res_img)
#
#     # 保存结果图像，读者可自行修改文件路径
#     # cv2.imwrite('/home/wangyuchen/project/TZ/merge/res8.png', res_img)
#
#     # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
#     if cv2.waitKey(0) & 0xFF == 27:
#         cv2.destroyAllWindows()

# png_1_path = "/home/wangyuchen/project/clip/1_1619314680880310000.png"  # 读者可自行修改文件路径
# png_2_path = '/home/wangyuchen/project/TZ/merge/res1.png'  # 读者可自行修改文件路径
# img_1 = cv2.imread(png_1_path, cv2.IMREAD_UNCHANGED)
# img_2 = cv2.imread(png_2_path, cv2.IMREAD_UNCHANGED)
# # print(img_1.shape)
# # b, g, r, a = cv2.split(img_1)
# # b1, g1, r1, a1 = cv2.split(img_2)
# # a3 = cv2.bitwise_and(a, a1)
# a=np.zeros((5,5),dtype=np.uint8)
# a[0:3,0:3] = 255
# a[4,4] = 255
# a1 = a /255.0
# b=np.zeros((5,5),dtype=np.uint8)
# b[2:4,2:4] = 255
# b[0,0] = 255
# print("a= \n", a1)
# # print("b= \n", b)
# c = cv2.bitwise_not(a)
# # c = cv2.bitwise_and(a, b)
# print("c= \n", c)


png_1_path = "/home/wangyuchen/project/clip/1_1619314723002635000.png"  # 读者可自行修改文件路径
png_2_path = "/home/wangyuchen/project/TZ/merge/res2.png"  # 读者可自行修改文件路径
img_1 = cv2.imread(png_1_path, cv2.IMREAD_UNCHANGED)
img_2 = cv2.imread(png_2_path, cv2.IMREAD_UNCHANGED)
b, g, r, a = cv2.split(img_1)
b1, g1, r1, a1 = cv2.split(img_2)
print("b1:\n", b1)
print("a:\n", a)
print("a1:\n", a1)
# print(b1)
#     # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
#     # alpha_2 = png_2[y1:y2, x1:x2, 3] / 255.0
#     # alpha_1 = 1 - alpha_2
a2 = cv2.bitwise_and(a, a1)
a3 = cv2.bitwise_not(a)
a4 = cv2.bitwise_not(a1)
a5 = cv2.bitwise_and(a3, a4)
a6 = cv2.bitwise_not(a5)
a7 = cv2.bitwise_and(a3, a6)
# a8 = cv2.bitwise_not(a7)
a8 = cv2.divide(a7, 255)
a9 = cv2.bitwise_not(a7)
a9 = cv2.divide(a9, 255)
print("a8:\n", a8)
b = cv2.multiply(b, a9)
print("b:\n", b)
g = cv2.multiply(g, a9)
r = cv2.multiply(r, a9)

print("a9:\n", a9)
b1 = cv2.multiply(b1, a8)
print("b1:\n", b1)
g1 = cv2.multiply(g1, a8)
r1 = cv2.multiply(r1, a8)
n_b = cv2.add(b, b1)
print("n_b:\n", n_b)
print("a1:\n", a1)
# print(n_b)
# print(a6)
n_g = cv2.add(g, g1)
n_r = cv2.add(r, r1)

new_png = cv2.merge([n_b, n_g, n_r, a6])
cv2.imshow('result', new_png)
    # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
cv2.imwrite('/home/wangyuchen/project/TZ/merge/res3.png', new_png)
# a2 = cv2.bitwise_not(a1)
# print(a2)
# a3 = cv2.bitwise_and(a, a1)
# a4 = cv2.bitwise_or(a1, a3)
# a5 = cv2.divide(a3, 255)
# b = b * a5
# g = g * a5
# r = r * a5
# a6 = cv2.bitwise_not(a5)
# b1 = b1 * a6
# # print(b1)
# g1 = g1 * a6
# r1 = r1 * a6
# n_b = cv2.add(b, b1)
# n_g = cv2.add(g, g1)
# n_r = cv2.add(r, r1)
# print(n_b)
# new_png = cv2.merge([n_b, n_g, n_r, a6])
# new_png = cv2.merge([b, g, r, a4])
# cv2.imshow('result', new_png)

    # 保存结果图像，读者可自行修改文件路径


    # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
# if cv2.waitKey(0) & 0xFF == 27:
#     cv2.destroyAllWindows()