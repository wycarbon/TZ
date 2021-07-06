import os
import cv2

def getIMGName(path, suffix):
    input_template_All = []
    input_template_All_Path = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            # print(name)
            if os.path.splitext(name)[1] == suffix:
                input_template_All.append(name)
                input_template_All_Path.append(os.path.join(root, name))

    return input_template_All, input_template_All_Path

path = "/home/dailinhan/C20F656-data/data-fix-equal/wuhan-data/"
img_name,img_path=getIMGName(path,'.jpg')
txt_name,txt_path=getIMGName(path,'.txt')
# print(img_path)
print(txt_path)