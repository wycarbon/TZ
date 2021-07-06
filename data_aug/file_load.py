import os
import cv2
import numpy as np

img_dict = {}
def getIMGName(path, suffix):
    input_template_All = []
    input_template_All_Path = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == suffix:
                input_template_All.append(name)
                input_template_All_Path.append(os.path.join(root, name))
                img_dict[os.path.join(root, name)] = name
    return input_template_All, input_template_All_Path, img_dict

path = "/home/dailinhan/C20F656-data/data-fix-equal/tianjin-data/tinajin-data-fix-0514/84/day/84-1/0425-8/image/"
img_name, img_path, img_dic = getIMGName(path,'.jpg')
# print(img_name)
# print(img_path)

file_match = {}
for i in img_path:
    file_match[i] = i[:-3] + "txt"
iou_match = {}
for key, value in file_match.items():
    whole_iou = []
    pos = []
    with open(value, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            p_tmp = [float(i) for i in lines.split(' ')]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            pos.append(p_tmp)  # 添加新读取的数据
            pass
        iou_match[key] = pos
        # whole_iou.append(pos)
# L = np.array(whole_iou)
# print(len(iou_match))

for key in iou_match:
    # print(np.array(iou_match[key]).shape)
    # print(img_dic[key][:-3] + "png")
    iou_num = np.array(iou_match[key])
    img = cv2.imread(key)
    hight = img.shape[0]
    width = img.shape[1]
    bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    b, g, r, a = cv2.split(bgra)
    for i in range(0, iou_num.shape[0]):
        xmin = (iou_num[i][1] - iou_num[i][3] / 2.) * width + 1
        xmax = (iou_num[i][1] + iou_num[i][3] / 2.) * width + 1
        ymin = (iou_num[i][2] - iou_num[i][4] / 2.) * hight + 1
        ymax = (iou_num[i][2] + iou_num[i][4] / 2.) * hight + 1
        box = [int(xmin), int(ymin), int(xmax), int(ymax)]
        w1 = box[0]
        w2 = box[2]
        h1 = box[1]
        h2 = box[3]
        a[h1:h2, w1:w2] = 0
    bgra = cv2.merge([b, g, r, a])
    # print(box)
    #     cv2.imshow("a", bgra)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()
    cv2.imwrite("/home/wangyuchen/project/clip/" + img_dic[key][:-3] + "png", bgra)
# print(whole_iou)
# print(L.shape)
