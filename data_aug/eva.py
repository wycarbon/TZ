import os
import cv2
import numpy as np

# y= open('/home/dailinhan/C20F656-data/data-fix-equal/tianjin-data/tinajin-data-fix-0514/84/day/84-1/0425-8/image/1_1619314679984680000.txt')
# a = y.read()
# 1_1619314679984680000.xml
# print(a)
# def read_list(filenam):
#     pos = []
#     with open(filenam, 'r') as file_to_read:
#         while True:
#             lines = file_to_read.readline()  # 整行读取数据
#             if not lines:
#                 break
#                 pass
#             p_tmp = [float(i) for i in lines.split(' ')]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
#             pos.append(p_tmp)  # 添加新读取的数据
#             pass
#         print(pos)
#         L = np.array(pos)
#         # print(L[0,3])
#     return pos, L.shape

######
read = [[1124,706,1403,980],[935,201,1046,288],[859,318,1024,480],[892,110,976,170],
[225,233,407,360],[805,100,890,155],[957,86,1022,139],[1313,131,1388,192],
[882,62,943,114],[1076,82,1148,152],[1002,139,1099,206],[1160,39,1271,195],
[1166,195,1432,603],[991,30,1032,60],[51,139,312,258],[1016,56,1073,94],
[950,39,999,83],[1216,15,1250,40],[926,59,978,102],[1083,20,1119,50],
[570,94,789,400],[448,177,481,244],[532,70,810,224],[310,179,350,264],
[1116,58,1170,101],[1336,86,1367,133],[1050,30,1097,67],[381,172,418,259]
]

s = np.array(read)
# print(s.shape)
#####

# read, s = read_list("/home/dailinhan/C20F656-data/data-fix-equal/tianjin-data/tinajin-data-fix-0514/84/day/84-1/0425-8/image/1_1619314679984680000.txt")
img = cv2.imread("/home/dailinhan/C20F656-data/data-fix-equal/tianjin-data/tinajin-data-fix-0514/84/day/84-1/0425-8/image/1_1619314679984680000.jpg")
# # print(read)
# # print(s)
hight = img.shape[0]
width = img.shape[1]
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
for i in range(0, s.shape[0]):
#     xmin = (read[i][0]-read[i][2]/2.)*width + 1
#     xmax = (read[i][0]+read[i][2]/2.)*width + 1
#     ymin = (read[i][1]-read[i][3]/2.)*hight + 1
#     ymax = (read[i][1]+read[i][2]/2.)*hight + 1
#     box = [int(xmin), int(ymin), int(xmax), int(ymax)]
    w1 = read[i][0]
    w2 = read[i][2]
    h1 = read[i][1]
    h2 = read[i][3]
    r[h1:h2, w1:w2] = 200
#     # a[h1:h2, w1:w2] = 0
bgra = cv2.merge([b, g, r, a])
# # print(box)
cv2.imshow("a", bgra)
cv2.waitKey()
cv2.destroyAllWindows()
# cv2.imwrite("/home/wangyuchen/project/444.png",bgra)