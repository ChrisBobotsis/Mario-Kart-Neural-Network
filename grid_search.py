# This script checks for the optimal hyperparaemters to use for a model from conv_net.py

# https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/

from conv_net import conv_net_custom

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D

from tensorflow.keras.callbacks import TensorBoard

import numpy as np

from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import GridSearchCV

from tensorflow.keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam


if __name__ == "__main__":

    data_dir = 'data/training_data/6-ready_for_model/'

    X_name = 'X_Full-DataSet-07-21-2019_22-30-46.npy'
    X_file = data_dir+X_name

    Y_name = 'Y_Full-DataSet-07-21-2019_22-30-46.npy'
    Y_file = data_dir+Y_name

    X = np.load(X_file)
    Y = np.load(Y_file)

    model = KerasClassifier(build_fn=conv_net_custom)


    # Layers:

    #         Layer 1:

    layer1_filters = [64,32]
    layer1_kernel = [3,5]
    layer1_maxpool = [(2,2),(3,3)]
    layer1_dropout = [0.2,0.5]
            
    #         Layer 2:

    layer2_filters = [64,32]
    layer2_kernel = [3,5]
    layer2_avgpool = [(2,2),(3,3)]
    layer2_dropout = [0.2,0.5]
            
    #         Layer 3:

    layer3_units = [4,8,16]
            
    #         Layer 4:

    layer4_units = [4,8,16]

    # Learning Rate and Momentum:

    learn_rate = [0.0001, 0.0005, 0.001, 0.005, 0.01]
    # momentum = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9]

    # Weight Initializers:

    optimizer = [SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam]

    # Batch Size and Epochs:
    batch_size = [16,32,64]
    epochs = [1] # I am using 1 epoch just because I don't want to spend too much time on each possible grid


    score_params_list = []

    '''# GRID SEARCH FOR LAYER 1

    param_grid = dict(  layer1_filters=layer1_filters, layer1_kernel=layer1_kernel, layer1_maxpool=layer1_maxpool, layer1_dropout=layer1_dropout,
                        epochs=epochs
                        )

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')

    # GRID SEARCH FOR LAYER 2

    param_grid = dict(layer2_filters=layer2_filters, layer2_kernel=layer2_kernel, layer2_avgpool=layer2_avgpool, layer2_dropout=layer2_dropout,
                        epochs=epochs
                        )

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')
    
    # GRID SEARCH FOR LAYER 3

    param_grid = dict(layer3_units=layer3_units,
                        epochs=epochs
                        )

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')
                        
    # GRID SEARCH FOR LAYER 4

    param_grid = dict(layer4_units=layer4_units,
                        epochs=epochs
                        )

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')

    '''# GRID SEARCH FOR LEARNING RATE FOR ADAM OPTIMIZER
    
    param_grid = dict(learn_rate=learn_rate,
                        optimizer=[RMSprop],
                        epochs=epochs
                        )

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')

    '''# GRID SEARCH FOR OPTIMIZER

    param_grid = dict(optimizer=optimizer,
                        epochs=epochs)
                        
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')

    # GRID SEARCH FOR BATCH SIZE

    param_grid = dict(batch_size=batch_size,
                        epochs=epochs)

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

    grid_result = grid.fit(X,Y)
    score_params_list.append([grid_result.best_score_, grid_result.best_params_])
    print(f'Best: {grid_result.best_score_} using {grid_result.best_params_}')'''

    


    for items in score_params_list:
        print(f'Best: {items[0]} using {items[1]}')



    

    '''# summarize results
    print(f'Best: {grid_result.best_score_} using {grid_results.best_params}')
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print(f'{mean} {stdev} with: {param}')'''