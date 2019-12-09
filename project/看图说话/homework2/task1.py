rom keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

def generate_vgg16():
    input_shape = (224, 224, 3) # 输入: 224*244，RGB三位图
    model = Sequential([
    	Conv2D(64, (3, 3), input_shape=input_shape, padding='same', activation='relu'),
    	# 卷积层，64个滤波器（卷积核），尺寸3*3，参数：输入规格，填充，激活函数
    	Conv2D(64, (3, 3), padding='same', activation='relu'),
    	# 非首层无需指定输入规格
    	MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),

    	# Block 2
    	Conv2D(128, (3, 3), padding='same', activation='relu'),
    	Conv2D(128, (3, 3), padding='same', activation='relu'),
    	MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    	
    	# 3
    	Conv2D(256, (3, 3), padding='same', activation='relu'),
    	Conv2D(256, (3, 3), padding='same', activation='relu'),
    	Conv2D(256, (3, 3), padding='same', activation='relu'),
    	MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    	# 4
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    	# 5
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	Conv2D(512, (3, 3), padding='same', activation='relu'),
    	MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    	# 全连接层
    	Flatten(),
    	Dense(4096, activation='relu'),
    	Dense(4096, activation='relu'),
    	Dense(1000, activation='softmax')
    	# 最后要做一个softmax，输出概率归一化
    	])
    return model

if __name__ == '__main__':
	# 主函数，调用
    model = generate_vgg16()
    model.summary()