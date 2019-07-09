# This script contains the convolutional neural network that this repo will use to play Super Mario Kart

# Things to consider (https://towardsdatascience.com/a-guide-for-building-convolutional-neural-networks-e4eefd17f4fd)
#
# Filters:
#
# 3*3 filter is probably best, not much more effective to use 5*5, 7*7 or more
# 1*1 convolutions can also be used at certain points in the networks to reduce the dimensionality of the feature maps before processing with a 3*3
# ---> I assume that the reason you can reduce dimensionality using a 1*1 filter is by having a larger stride though...
#
# Activations:
#
# Generally just stick with ReLU, then afterward with find tuning you can try: ELU, PReLU, or LeakyReLU
#
# Pooling:
#
# Pooling is used for freature summarization while downsampling (applying conv layers?) as you go deeper into the network
# As a default use max pooling throughout the network and then global aeverage pooling at the very end before the dense layer + softmax
#
# Network Depth and Structure:
# 
# Increased depth =>   Higher Accuracy, Lower Speed
# MobileNet-v2 / Depthwise Separable convoltuions and low resolution for speed 
# SENet / Squeeze-Excitation or NASNet and high resolution for accuracy 
# A regular ResNet / Residual Blocks for a balance
#
# Data Preprocessing and Augmentation:
#
# Augmentation almost always increases accuracy, but make sure it is relevant to your use case (if you are doing image enhacement, not a great idea to standardize)
#
# Regularization:
# 
# Dropout by default for ease of use (mainly in latter level of CNN)
# If dropout fails explore others which can be customized like L1/L2
#
# Training:
#
# Start with Adam optimizer
# Possibly switch to SGD midway of training 


import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D

from tensorflow.keras.callbacks import TensorBoard

import time
import numpy as np
import os


def conv_net_custom(input_shape=None,num_classifiers=None):
    
    if not input_shape or not num_classifiers:
        print('You have to pass an input shape AND a number of classifiers!')
    else:

        year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%H,%M,%S").split(',')
        model_name = f'conv_net_custom-{month}-{day}-{year}_{hour}-{minute}-{second}'
        os.mkdir(f'logs/{model_name}')

        #create model
        model = Sequential()
        #add model layers
        model.add(Conv2D(64, kernel_size=5, activation='relu', input_shape=input_shape))        
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(AveragePooling2D(pool_size=(2,2)))
        model.add(Dropout(0.5))

        model.add(Flatten())

        model.add(Dense(16, activation='relu'))
        model.add(Dense(16,activation='relu'))

        model.add(Dense(units=num_classifiers,activation='softmax'))

        #Tensorboard
        # have to use backslash (\) instead of forward slash (/) here for some reason 
        t_board= TensorBoard(log_dir=f'\logs\{model_name}')

        #compile model using accuracy to measure model performance
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        #train the model
        '''

        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, callbacks=[t_board])

        '''

        return model,t_board

if __name__ == "__main__":

    model, t_board = conv_net_custom(input_shape=(32,100,1),num_classifiers=6) 

    # model.fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)    

    '''
    Set the input_shape to (286,384,1). Now the model expects an input with 4 dimensions. 
    This means that you have to reshape your image with .reshape(n_images, 286, 384, 1). 
    Now you have added an extra dimension without changing the data and your model is ready to run. 
    Basically, you need to reshape your data to (n_images, x_shape, y_shape, n_steps).

    Y values should be of shape (n_samples,number of classifications)

    '''

    training_dir = None
    validation_dir = None

    training_data = np.load('data/training_data/processed/train-data_21-06-2019_19-04-17.npy.npy')

    X_train = np.empty(shape=(1,32,100,1))
    Y_train = np.empty(shape=(1,6))

    X_val = np.empty(shape=(1,32,100,1))
    Y_val = np.empty(shape=(1,6))

    for idx in range(0,5):
        X_train = np.append(X_train,training_data[idx][1].reshape(1,32,100,1),axis=0)
        Y_train = np.append(Y_train,training_data[idx][0].reshape(1,6),axis=0)

        X_val = np.append(X_val,training_data[idx+5][1].reshape(1,32,100,1),axis=0)
        Y_val = np.append(Y_val,training_data[idx+5][0].reshape(1,6),axis=0)   

    X_train = X_train[1:]
    Y_train = Y_train[1:]    
    X_val = X_val[1:]
    Y_val = Y_val[1:]

    #X_train = X_train.reshape(5,32,100,1)
    #X_val = X_val.reshape(5,32,100,1)

    #import pdb; pdb.set_trace()

    model.fit(x=X_train,y=Y_train,validation_data=[X_val,Y_val],epochs=10,callbacks=[t_board])   # ,callbacks=[t_board]

    #import pdb; pdb.set_trace()
    
