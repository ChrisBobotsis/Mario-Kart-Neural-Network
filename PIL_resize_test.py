import numpy as np
from PIL import Image
import cv2
x = np.load('data/training_data/1-raw/train-data_01-07-2019_14-09-05_Bowser_Castle_1.npy')
y = Image.fromarray(x[0][1])


a = y.resize((100,32))
b = np.array(a)
#Remove mario 
b[18:32,42:58] = int(255/2)

cv2.imshow('test',b)
cv2.waitKey(0)