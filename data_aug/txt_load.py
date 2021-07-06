import os
import numpy as np
import cv2

def read_list(filenam):
    pos = []
    with open(filenam, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            p_tmp = [float(i) for i in lines.split(' ')]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            pos.append(p_tmp)  # 添加新读取的数据
            pass
        print(pos)
        L = np.array(pos)
        # print(L[0,3])
    return pos, L.shape

read, s = read_list("/home/dailinhan/C20F656-data/data-fix-equal/xingyun-data-0427fix/day/image/vlc-00450.txt")
img = cv2.imread("/home/dailinhan/C20F656-data/data-fix-equal/xingyun-data-0427fix/day/image/vlc-00450.jpg")
print(read)
hight = img.shape[0]
width = img.shape[1]
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
# print(read[5][0])
for i in range(0, s[0]):
    xmin = (read[i][1]-read[i][3]/2.)*width + 1
    xmax = (read[i][1]+read[i][3]/2.)*width + 1
    ymin = (read[i][2]-read[i][4]/2.)*hight + 1
    ymax = (read[i][2]+read[i][4]/2.)*hight + 1
    box = [int(xmin), int(ymin), int(xmax), int(ymax)]
    w1 = box[0]
    w2 = box[2]
    h1 = box[1]
    h2 = box[3]
    a[h1:h2, w1:w2] = 0
bgra = cv2.merge([b, g, r, a])
print(box)
cv2.imshow("a", bgra)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("/home/wangyuchen/project/444.png",bgra)

# xmin = (read[0][1]-read[0][3]/2.)*width
# xmax = (read[0][1]+read[0][3]/2.)*width
# ymin = (read[0][2]-read[0][4]/2.)*hight
# ymax = (read[0][2]+read[0][4]/2.)*hight
# box = [int(xmin), int(ymin), int(xmax), int(ymax)]
# w1 = box[0]
# w2 = box[2]
# h1 = box[1]
# h2 = box[3]
# a[h1:h2, w1:w2] = 0
# bgra = cv2.merge([b, g, r, a])
# cv2.imshow("a", bgra)
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imwrite("/home/wangyuchen/project/222.png",bgra)