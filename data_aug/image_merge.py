import cv2
import numpy as np


def merge_img(png_1, png_2, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_2.shape[0]
    xx1 = 0
    xx2 = png_2.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > png_1.shape[1]:
        xx2 = png_2.shape[1] - (x2 - png_1.shape[1])
        x2 = png_1.shape[1]
    if y2 > png_1.shape[0]:
        yy2 = png_2.shape[0] - (y2 - png_1.shape[0])
        y2 = png_1.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_2 = png_2[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_1 = 1 - alpha_2

    # 开始叠加
    for c in range(0, 3):
        png_1[y1:y2, x1:x2, c] = ((alpha_1 * png_1[y1:y2, x1:x2, c]) + (alpha_2 * png_2[yy1:yy2, xx1:xx2, c]))

    return png_1


if __name__ == '__main__':
    # 定义图像路径
    png_1_path = "/home/wangyuchen/project/clip/1_1619314680880310000.png"  # 读者可自行修改文件路径
    png_2_path = '/home/wangyuchen/project/TZ/merge/res1.png'  # 读者可自行修改文件路径

    # 读取图像
    img_1 = cv2.imread(png_1_path, cv2.IMREAD_UNCHANGED)
    img_2 = cv2.imread(png_2_path, cv2.IMREAD_UNCHANGED)

    # 设置叠加位置坐标
    x1 = 0
    y1 = 0
    x2 = x1 + img_2.shape[1]
    y2 = y1 + img_2.shape[0]

    # 开始叠加
    res_img = merge_img(img_1, img_2, y1, y2, x1, x2)

    # 显示结果图像
    cv2.imshow('result', res_img)

    # 保存结果图像，读者可自行修改文件路径
    cv2.imwrite('/home/wangyuchen/project/TZ/merge/res2.png', res_img)

    # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()