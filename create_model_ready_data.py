
import os
import numpy as np

file_name_list = os.listdir('data/training_data/5-final_data_set/')

assert len(file_name_list) == 1, 'There is more than one file in \'data/training_data/5-final_data_set/\''

file_name = file_name_list[0]

training_data = np.load('data/training_data/5-final_data_set/'+file_name)

X = []
Y = []

for idx in range(len(training_data)):
    X.append(training_data[idx][1])
    Y.append(training_data[idx][0])
    if idx%1000 == 0:
        print(idx)

X = np.array(X).reshape(len(X),32,100,1)
Y = np.array(Y).reshape(len(Y),6)

np.save(file='data/training_data/6-ready_for_model/'+'X_'+file_name,arr=X)
np.save(file='data/training_data/6-ready_for_model/'+'Y_'+file_name,arr=Y)