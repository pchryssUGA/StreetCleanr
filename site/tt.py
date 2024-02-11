import tensorflow as tf
import os
import cv2
import imghdr
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from tensorflow.keras.models import load_model

img = cv2.imread(os.path.join('site','static','images','clean5.jpg'))
resize = tf.image.resize(img, (256, 256))
new_model = load_model(os.path.join('site','models', 'streetsmodel.h5'))
yhatnew = new_model.predict(np.expand_dims(resize/255, 0))

print(yhatnew)