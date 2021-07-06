import os
import random

def write_jpgname_to_txt(image_path,txt_path,txt_all_path):
    #image_path = r"/media/tztek/赖校生/rvsu_dataset/0303objecttraindata/0226-anno-yingyongbiaozhu-0303fae/selectTrafficImg/images_selected"
    #txt_path = r"/media/tztek/赖校生/rvsu_dataset/0303objecttraindata/0226-anno-yingyongbiaozhu-0303fae/selectTrafficImg/0226-anno-yingyongbiaozhu-0303fae.txt"
    list_name = os.listdir(image_path)
    print(list_name)
    txt_file = open(txt_path,"w+")
    txt_all_file = open(txt_all_path, "a+")
    for filename in list_name:
       # print(filename)
        if (".txt" in filename) and (os.path.exists(os.path.join(image_path,filename[0:len(filename)-4]+".jpg"))):
            #print(filename)
            train_name = os.path.join(image_path,filename[0:len(filename)-4]+".jpg")
            # txt_file.write(train_name)
            # txt_file.write("\n")
            txt_all_file.write(train_name)
            txt_all_file.write("\n")


if __name__ == "__main__":

    # path_dir = r"/home/tztek/workspace/rvsu/object_train_data_label/fusiondata-0331/train-data/wuhan-data-fix/day/images"
    # pathlist = os.listdir(path_dir)
    # txt_all_path = path_dir + os.path.sep+"train_wuhanFIX-day-0419.txt"
    # for i in range(len(pathlist)):
    #     image_path = path_dir + os.path.sep + pathlist[i]
    #     txt_path =path_dir + os.path.sep + pathlist[i]+".txt"
    #     write_jpgname_to_txt(image_path,txt_path,txt_all_path)

    path_dir = r"/home/dailinhan/C20F656-data/data-fix-equal/tianjin-data/tinajin-data-fix-0514/84/day/84-1/0425-8/"
    for home, dirs, files in os.walk(path_dir):
        # print("#######dir list#######")
        # txt_all_path = path_dir + os.path.sep + "trainval_all_0624.txt"
        txt_all_path = "/home/wangyuchen/project/TZ/" + "trainval_all_06251.txt"
        for dir in dirs:
            if "image" == dir:
                print(os.path.join(home, dir))
                image_path = os.path.join(home, dir)
                txt_path =os.path.join(home, dir)+image_path.split("/")[-2]+"_train.txt"
                write_jpgname_to_txt(image_path,txt_path,txt_all_path)

    #对图像顺序进行shuffle,并区分训练和测试集
    train_list = []
    # trainval_txt_file = open(path_dir + os.path.sep + "trainval_all_0624.txt","r")
    # train_txt_file = open(path_dir + os.path.sep + "train_all_0624.txt","a+")
    # val_txt_file = open(path_dir + os.path.sep + "val_all_0624.txt", "a+")
    trainval_txt_file = open("/home/wangyuchen/project/TZ/trainval_all_06251.txt","r")
    train_txt_file = open("/home/wangyuchen/project/TZ/train_all_06251.txt","a+")
    val_txt_file = open("/home/wangyuchen/project/TZ/val_all_06251.txt", "a+")


    for line in trainval_txt_file.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        print(line)
        train_list.append(line)
    random.shuffle(train_list)


    ## train val rate
    rate = 0.9
    for i in range(int(len(train_list)*rate)):
        train_txt_file.write(train_list[i])
        train_txt_file.write("\n")

    for i in range(int(len(train_list)*rate),len(train_list)):
        val_txt_file.write(train_list[i])
        val_txt_file.write("\n")


