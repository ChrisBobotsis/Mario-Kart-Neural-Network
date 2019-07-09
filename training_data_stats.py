import os
import numpy as np


raw_dir = 'data/training_data/raw/'
filtered_dir = 'data/training_data/filtered/'

raw_list = os.listdir(raw_dir)
filtered_list = os.listdir(filtered_dir)



    # c (forward)                           [1,0,0,0,0,0]
    # c (forward), left                     [0,1,0,0,0,0]
    # c (forward), right                    [0,0,1,0,0,0]
    # c (forward), right, x (drift)         [0,0,0,1,0,0]
    # c (forward), left, x (drift)          [0,0,0,0,1,0]
    # no input                              [0,0,0,0,0,1]

'''input_to_vector = {

    'forward' :              np.array([1,0,0,0,0,0]).reshape(1,6),
    'forward_left' :         np.array([0,1,0,0,0,0]).reshape(1,6),
    'forward_right' :        np.array([0,0,1,0,0,0]).reshape(1,6),
    'forward_right_drift' :  np.array([0,0,0,1,0,0]).reshape(1,6),  
    'forard_left_drift' :    np.array([0,0,0,0,1,0]).reshape(1,6),
    'no_input' :             np.array([0,0,0,0,0,1]).reshape(1,6)

}'''


class Stats:
    def __init__(self):
        self.training_num = 0
        self.forward = 0
        self.forward_right = 0
        self.forward_left = 0
        self.forward_right_drift = 0
        self.forward_left_drift = 0
        self.no_input = 0

raw_stats = Stats()
filtered_stats = Stats()

#raw_training_num = 0
#filtered_training_num = 0

print('...Processing Raw Data...')
if len(raw_list) == 0:
    print('No raw data!')
else:
    for raw_data_item in raw_list:
        x = np.load(raw_dir+raw_data_item)
        length = len(x)
        raw_stats.training_num += length
        for i in range(length):
            tmp = x[i][0]
            if tmp[0] == 1:
                raw_stats.forward += 1
            elif tmp[1] == 1:
                raw_stats.forward_left += 1
            elif tmp[2] == 1:
                raw_stats.forward_right += 1
            elif tmp[3] == 1:
                raw_stats.forward_right_drift += 1
            elif tmp[4] == 1:
                raw_stats.forward_left_drift += 1
            elif tmp[5] == 1:
                raw_stats.no_input += 1
        del x

print('...Processing Filtered Data...')
if len(filtered_list) == 0:
    print('No filtered data!')
else:
    for filtered_data_item in filtered_list:
        x = np.load(filtered_dir+filtered_data_item)
        length = len(x)
        filtered_stats.training_num += length
        for i in range(length):
            tmp = x[i][0]
            if tmp[0] == 1:
                filtered_stats.forward += 1
            elif tmp[1] == 1:
                filtered_stats.forward_left += 1
            elif tmp[2] == 1:
                filtered_stats.forward_right += 1
            elif tmp[3] == 1:
                filtered_stats.forward_right_drift += 1
            elif tmp[4] == 1:
                filtered_stats.forward_left_drift += 1
            elif tmp[5] == 1:
                filtered_stats.no_input += 1
        del x

# Displaying all data

print('RAW TRAINING DATA:')
print(f'Total Number of Training Sets:\t\t\t{raw_stats.training_num}')
print(f'Total Number of Forward Training Sets:\t\t\t{raw_stats.forward}')
print(f'Total Number of Forward_Left Training Sets:\t\t\t{raw_stats.forward_left}')
print(f'Total Number of Forward_Left_Drift Training Sets:\t\t\t{raw_stats.forward_left_drift}')
print(f'Total Number of Forward_Right Training Sets:\t\t\t{raw_stats.forward_right}')
print(f'Total Number of Forward_Right_Drift Training Sets:\t\t\t{raw_stats.forward_right_drift}')
print(f'Total Number of No_Input Training Sets:\t\t\t{raw_stats.no_input}')
print('\n\n')
print('FILTERED TRAINING DATA:')
print(f'Total Number of Filtered Training Sets:\t{filtered_stats.training_num}')
print(f'Total Number of Forward Training Sets:\t\t\t{filtered_stats.forward}')
print(f'Total Number of Forward_Left Training Sets:\t\t\t{filtered_stats.forward_left}')
print(f'Total Number of Forward_Left_Drift Training Sets:\t\t\t{filtered_stats.forward_left_drift}')
print(f'Total Number of Forward_Right Training Sets:\t\t\t{filtered_stats.forward_right}')
print(f'Total Number of Forward_Right_Drift Training Sets:\t\t\t{filtered_stats.forward_right_drift}')
print(f'Total Number of No_Input Training Sets:\t\t\t{filtered_stats.no_input}')