from keras.models import model_from_json
from PIL import Image as pil_image
from keras import backend as K
import numpy as np
from pickle import dump
from os import listdir
import os
from keras.models import Model
import keras
from tqdm import tqdm

def load_img_as_np_array(path, target_size):
    """从给定文件[加载]图像,[缩放]图像大小为给定target_size,返回[Keras支持]的浮点数numpy数组.

    # Arguments
        path: 图像文件路径
        target_size: 元组(图像高度, 图像宽度).

    # Returns
        numpy 数组.
    """
    img = pil_image.open(path) # 打开文件
    img = img.resize(target_size,pil_image.NEAREST) # NEARSET 是一种插值方法
    return np.asarray(img, dtype=K.floatx()) #转化为向量


def preprocess_input(x):
    """预处理图像用于网络输入, 将图像由RGB格式转为BGR格式.
       将图像的每一个图像通道减去其均值
       均值BGR三个通道的均值分别为 103.939, 116.779, 123.68

    # Arguments
        x: numpy 数组, 4维.
        data_format: Data format of the image array.

    # Returns
        Preprocessed Numpy array.
    """
    # 'RGB'->'BGR', https://www.scivision.co/numpy-image-bgr-to-rgb/
    x = x[..., ::-1]
    mean = [103.939, 116.779, 123.68]

    x[..., 0] -= mean[0]
    x[..., 1] -= mean[1]
    x[..., 2] -= mean[2]

    return x

def load_vgg16_model():
    """从当前目录下面的 vgg16_exported.json 和 vgg16_exported.h5 两个文件中导入 VGG16 网络并返回创建的网络模型
       vgg16_exported.json 下载链接：链接: https://pan.baidu.com/s/13WQBRb4sr3umP7xbUCxmCg 提取码: ycb5 
       vgg16_exported.h5 下载链接: https://pan.baidu.com/s/1yF8wybHuzGoTzwSkqTPzzQ 提取码: ub75
       注意上传完成的作业时不要上传这两个文件
    # Returns
        创建的网络模型 model
    """
    json_file = open("vgg16_exported.json","r")
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    model.load_weights("vgg16_exported.h5")

    return model

def extract_features(directory):
    """提取给定文件夹中所有图像的特征, 将提取的特征保存在文件features.pkl中,
       提取的特征保存在一个dict中, key为文件名(不带.jpg后缀), value为特征值[np.array]

    Args:
        directory: 包含jpg文件的文件夹

    Returns:
        None
    """
    model = load_vgg16_model()
    # 去除模型最后一层
    model.layers.pop()
    model = Model(inputs=model.inputs, outputs=model.layers[-1].output)
    print("Extracting...")

    features = dict()
    pbar = tqdm(total=len(listdir(directory)), desc="进度", ncols=100)
    for fn in listdir(directory):
        print("\tRead file:", fn)
        fn_path = directory + '/' + fn

        # 返回长、宽、通道的三维张量
        arr = load_img_as_np_array(fn_path, target_size=(224,224))

        # 改变数组的形态，增加一个维度（批处理）—— 4维
        arr = arr.reshape((1, arr.shape[0], arr.shape[1], arr.shape[2]))
        # 预处理图像为VGG模型的输入
        arr = preprocess_input(arr)
        # 计算特征
        feature = model.predict(arr, verbose=0)

        print("\tprocessed...",end='')
        id = os.path.splitext(fn)[0]
        features[id] = feature
        print("Saved. ", id)
        pbar.update(1)

    print("Complete extracting.")
    return features

if __name__ == '__main__':
    # 提取Flicker8k数据集中所有图像的特征，保存在一个文件中, 大约一小时的时间，最后的文件大小为127M
    # Flickr8k数据集的下载链接: https://pan.baidu.com/s/1bQcQAz0pxPix9q9kCoZ1aw 提取码: 6gpd 
    # 下载zip文件，解压缩到当前目录的子文件夹Flicker8k_Dataset， 注意上传完成的作业时不要上传这个数据集文件
    directory = './Flicker8k_Dataset'
    features = extract_features(directory)
    print('提取特征的文件个数：%d' % len(features))
    print(keras.backend.image_data_format())
    #保存特征到文件
    dump(features, open('features.pkl', 'wb'))