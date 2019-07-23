# The goal of this script is to reduce the size of each image to something much smaller.
# I also plan to have the option to create sets of n-datapoints to allow for a time series model 

# I could hold all of these processes to the data in one variable, but I'm worried about lack of RAM (only 4GB)


import pandas as pd
import numpy as np
import os
from PIL import Image
import time

NEW_WIDTH = 100
NEW_HEIGHT = 32

N = 5


# Function resizes images to 100*32 (width*height)
def resize(img):
    img = Image.fromarray(img)
    img = img.resize((NEW_WIDTH,NEW_HEIGHT))
    img = np.array(img)
    return img

# Where are the files
filtered_dir = 'data/training_data/filtered/'
processed_dir = 'data/training_data/processed/'
# List of the file names
filtered_list = os.listdir(filtered_dir)

# For each file in feature list: resize the images and save it to the processed folder
for item in filtered_list:
    data = np.load(filtered_dir+item)
    for idx in range(len(data)):
        data[idx][1] = resize(data[idx][1])

    name = processed_dir+item

    if name in os.listdir(processed_dir):
        name = name+'-new'

    name = name+'.npy'

    np.save(arr=data,file=name)

# Delete variables no longer being used
del filtered_list


# Get all files in processed list now

processed_list = os.listdir(processed_dir)

# Create sets of N time series inputs

'''
for item in 
'''

# Create one large file

data_total = []

for item in processed_list:
    data = np.load(processed_dir+item)

    for idx in range(len(data)):
        data_total.append(data[idx])

year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%H,%M,%S").split(',')

np.save(arr=data_total,file=f'data/training_data/full_data_set/Full-DataSet-{month}-{day}-{year}_{hour}-{minute}-{second}')
