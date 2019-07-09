import numpy as np
from PIL import Image
import cv2
x = np.load('data/training_data/raw/train-data_01-07-2019_14-09-05.npy')
y = Image.fromarray(x[0][1])


a = y.resize((100,32))
b = np.array(a)

cv2.imshow('test',b)
cv2.waitKey(0)