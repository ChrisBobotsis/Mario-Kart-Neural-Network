# The goal of this script is to go through all of the raw data and filter out frames that I have labeled as unwanted

import numpy as np
import os

raw_dir = 'data/training_data/raw/'
filtered_dir = 'data/training_data/filtered/'

raw_list = os.listdir(raw_dir)

# Input all of the files here to get a dictionary of what frames we want to remove
'''
This is how 

'''
del_frames = {

# [[start_of_frame_removal,end_of_frame_removal]]  it will remove the start_of_frame_removal and the end_of_frame_removal

#'train-data_21-06-2019_19-04-17.npy': [[0,38],[100,120]]

'train-data_01-07-2019_14-09-05_Bowser_Castle_1.npy': [[2808,2865]],

'train-data_01-07-2019_14-29-03_Bowser_Castle_1.npy': [[0,1],[2681,2843]],

'train-data_01-07-2019_14-55-47_Ghost_Valley_2.npy': [[0,3],[1520,1540],[3520,3564]], # a lot of bumping in this one that I didn't remove

'train-data_01-07-2019_15-00-53_Ghost_Valley_2.npy': [[0,8],[2420,2523]], # one bump in this that I didn't remove

'train-data_02-07-2019_22-49-06_Mario_Circuit_3.npy': [[0,33],[3281,3289]], # going off road once that I didn't remove

'train-data_02-07-2019_22-53-42_Mario_Circuit_3.npy': [[0,3],[750,826]],

'train-data_02-07-2019_23-01-48-32FPS_Mario_Circuit_3.npy': [[0,15],[1327,1368],[3586,3606]],   #close to the pipe at (1350), on the edge at (2071), near the pipe at (2480), near the edge at (3145), on the edge at (3413), near pipe at (3520)

'train-data_02-07-2019_23-12-11-34FPS_Donut_Plains_2.npy': [[0,10],[3126,3138]],   # near the edge (1835), on edge at (3023),

'train-data_02-07-2019_23-26-22-34FPS_Donut_Plains_2.npy': [[0,0],[1111,1182],[3317,3374]],   # offroad at (1304), offroad at (2533), offroad at (2719)

'train-data_02-07-2019_23-36-09-34FPS_Bowser_Castle_2.npy': [[0,10],[1637,1747],[2812,2955],[3867,3997]], #

'train-data_02-07-2019_23-38-16-34FPS_Bowser_Castle_2.npy': [[0,17],[1600,1725],[3036,3191]], # knock into block at (2506), knock into block at (2830)

'train-data_22-06-2019_20-37-18_Mario_Circuit_1.npy': [[0,0],[3348,3381]], #

'train-data_22-06-2019_20-40-34_Mario_Circuit_1.npy': [[0,0],[3343,3378]], # offroad at (650), slightly offroad at (3309)

'train-data_22-06-2019_20-46-49_Ghost_Valley_1.npy': [[0,10],[3257,3283]],

'train-data_22-06-2019_20-51-34_Ghost_Valley_1.npy': [[0,8],[3254,3296]],

'train-data_22-06-2019_20-54-08_Ghost_Valley_1.npy': [[0,13],[3307,3341]], # bumped on edge at (1936)

'train-data_22-06-2019_21-15-06_Donut_Plains_1.npy': [[0,1],[2670,2674]], # on edge at (920 ),

'train-data_22-06-2019_21-21-48_Donut_Plains_1.npy': [[0,29],[1893,1906]],

'train-data_17-07-2019_18-22-39-33FPS_Mario_Circuit_1.npy': [[0,0],[3355,3361]],

'train-data_17-07-2019_18-26-30-34FPS_Donut_Plains_1.npy': [[0,6],[4271,4300]],

# removing since we have over 10k; 'train-data_17-07-2019_18-33-40-33FPS_Bowser_Castle_1.npy': [[0,8],[2355,2450],[3288,3377],[3720,3781],[4430,4627],[4960,4990]],  # bumping into the sides a lot on this one

'train-data_17-07-2019_18-36-41-33FPS_Bowser_Castle_1.npy': [[0,12],[4748,4784]],  # left hitting a block at 1750

# removing since we have over 10k; 'train-data_17-07-2019_18-39-23-33FPS_Ghost_Valley_2.npy': [[0,0],[1750,1967],[3641,3676]], # bumped a bit

'train-data_17-07-2019_18-41-49-33FPS_Ghost_Valley_2.npy': [[0,10],[3557,3584]], # bumped a number of times in this one

# removing since we have over 10k;  'train-data_17-07-2019_18-45-43-34FPS_Donut_Plains_2.npy': [[0,78],[5031,5059]], # offroad at (416,1812,2206,3000), and quite a bit later offroad as well

'train-data_17-07-2019_18-49-36-33FPS_Donut_Plains_2.npy': [[0,6],[4965,4987]], # offroad at (1621,1765) quite a bit of offroad touching

'train-data_17-07-2019_21-09-58-32FPS_Bowser_Castle_2.npy': [[0,15],[1586,1840],[2700,2850]], # bumped into side at 3067

# removing because we have over 10k; 'train-data_17-07-2019_21-13-17-33FPS_Bowser_Castle_2.npy': [[0,10],[850,928],[1809,1940],[2865,2900],[4058,4114],[4806,5637]],

# removing since we have over 10k for this track; 'train-data_17-07-2019_21-18-16-32FPS_Bowser_Castle_2.npy': [[0,10],[1822,2124],[3079,3494]],

# removing 3000 to 5411 just to limit the frames
'train-data_17-07-2019_21-23-17-32FPS_Mario_Circuit_3.npy': [[0,40],[1338,1549],[3000,5411],[5411,5416]],

'train-data_21-07-2019_17-08-21-29FPS_Donut_Plains_1.npy': [[0,1],[350,479],[700,815],[1300,1489]],

'train-data_21-07-2019_17-19-04-30FPS_Choco_Island_1.npy': [[0,5],[476,535],[2334,2401],[2700,2800],[3064,3112]],

'train-data_21-07-2019_17-25-48-30FPS_Choco_Island_1.npy': [[0,0],[1050,1145],[2870,2906]],

'train-data_21-07-2019_17-49-42-29FPS_Choco_Island_1.npy': [[0,28],[2877,2907]],

# Chopping off 1500 to 3308 because we have too much data 
'train-data_21-07-2019_22-06-10-35FPS_Choco_Island_1.npy': [[0,19],[1500,3308],[3308,3363]]

}

count = 1
total = len(del_frames)

for raw_file_name in del_frames.keys():
    
    # Load file from list of raw files
    raw_file = np.load(raw_dir+raw_file_name)

    # Assume we are adding all training sets to the filtered list
    mask = [True]*len(raw_file)
    
    # Set mask for frames to delete as False
    for frames_to_delete in del_frames[raw_file_name]:
        for i in range(frames_to_delete[0],(frames_to_delete[1]+1)):   # +1 because it doesn't go to the end
            mask[i] = False

    # Create a filtered data list
    filtered_data = []
    file_count = 1
    last_state = None
    # Adding filtered data from raw, saving each segment as an individual file (to 'data/training_data/filtered/') so as to create sequences later on
    for idx in range(len(mask)):
        if mask[idx] == True:
            
            filtered_data.append(raw_file[idx])
            #if last_state == False and file_count != 1:
            #    file_count += 1
            
            last_state = True

            if idx == (len(mask)-1):
                #file_count += 1
                #import pdb; pdb.set_trace()

                if raw_file_name in os.listdir(filtered_dir):
                    name = raw_file_name[:-4]+'-new-File-'+str(file_count)
                else:
                    name = raw_file_name[:-4]+'-File-'+str(file_count)

                np.save(arr=filtered_data,file=filtered_dir+name)
                filtered_data = []


        elif len(filtered_data)>0:
            #import pdb;pdb.set_trace()
            if raw_file_name in os.listdir(filtered_dir):
                name = raw_file_name[:-4]+'-new-File-'+str(file_count)
            else:
                name = raw_file_name[:-4]+'-File-'+str(file_count)

            np.save(arr=filtered_data,file=filtered_dir+name)
            filtered_data = []

            if last_state == True:
                file_count += 1
            
            last_state = False

        

    '''
    if raw_file_name in os.listdir(filtered_dir):
        name = raw_file_name+'-new'
    else:
        name = raw_file_name

    np.save(arr=filtered_data,file=filtered_dir+name)
    '''

    print(f'One file saved, starting the next...{total-count} to go')
    count += 1
