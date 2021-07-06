import os
import cv2

img = cv2.imread("/home/wangyuchen/project/111.png", cv2.IMREAD_UNCHANGED)
print("img.shape = ", img.shape)
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
a[100:400, 100:400] = 0
a[10:110, 9:32] = 0
# r[300:500, 200:300] = 100
# b[300:500, 200:300] = 100
# g[300:500, 200:300] = 200
bgra = cv2.merge([b, g, r, a])
cv2.imshow("a", bgra)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("/home/wangyuchen/project/222.png",bgra)


# def addImage(img1_path, img2_path):
#     img1 = cv2.imread(img1_path, cv2.IMREAD_UNCHANGED)
#     img = cv2.imread(img2_path, cv2.IMREAD_UNCHANGED)
#     # h, w, _ = img1.shape
#     # 函数要求两张图必须是同一个size
#     img2 = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
#     #print img1.shape, img2.shape
#     #alpha，beta，gamma可调
#     alpha = 1
#     beta = 1-alpha
#     gamma = 0
#     img_add = cv2.addWeighted(img1, alpha, img2, alpha, gamma)
#     cv2.imwrite("/home/wangyuchen/project/666.png", img_add)
#     # cv2.namedWindow('addImage')
#     cv2.imshow('img_add',img_add)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#
# imgg = addImage("/home/wangyuchen/project/111.png", "/home/wangyuchen/project/222.png")