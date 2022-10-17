import os
import shutil
train_image_path = 'D:/python/yolov5-master/yolov5-master/input/mchar_train/'
val_image_path = 'D:/python/yolov5-master/yolov5-master/input/mchar_val/'
dst_image_path = 'D:/python/yolov5-master/datasets/coco128/images/tianchimages/'
train_image_list = os.listdir(train_image_path)
val_image_list = os.listdir(val_image_path)
for img in train_image_list:
    shutil.copy(train_image_path+img, dst_image_path+img)
for img in val_image_list:
    shutil.copy(val_image_path+img, dst_image_path+'val_'+img)