import os
import cv2
import numpy as np

img = cv2.imread("/home/dailinhan/C20F656-data/data-fix-equal/need-check-old-data-0428/fusion-data/day/tz-0/image/unv_1611187300361662000.jpg")
print("img.shape = ", img.shape)
hight = int(img.shape[0])
width = int(img.shape[1])
yolo = [0.6927083333333334, 0.059722222222222225, 0.01875, 0.10648148148148148]
# yolo = [xcenter, ycenter, w, h]
voc = [1313, 8, 1349, 123]
# voc = [xmin, ymin, xmax, ymax]

bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
# cv2.imshow("imgshow", img)
# x = voc[2] - voc[0]
# y = voc[3] - voc[1]
# face = np.random.randint(0,256, (y,x,3))
# img[8:123, 1313:1349] = face
# face = img[8:123, 1313:1349]
# cv2.imshow("a", img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# 0.6927083333333334 0.059722222222222225 0.01875 0.10648148148148148
#<bndbox>
				# <xmin>1313</xmin>
				# <ymin>8</ymin>
				# <xmax>1349</xmax>
				# <ymax>123</ymax>
xmin = (yolo[0]-yolo[2]/2.)*width
xmax = (yolo[0]+yolo[2]/2.)*width
ymin = (yolo[1]-yolo[3]/2.)*hight
ymax = (yolo[1]+yolo[3]/2.)*hight
# box = [xmin, ymin, xmax, ymax]
box = [int(xmin), int(ymin), int(xmax), int(ymax)]
# w = box[2] - box[0]
w1 = box[0]
w2 = box[2]
# h = box[3] - box[1]
h1 = box[1]
h2 = box[3]
a[h1:h2, w1:w2] = 0
bgra = cv2.merge([b, g, r, a])
cv2.imshow("a", bgra)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("0000.png",)
print(box)
