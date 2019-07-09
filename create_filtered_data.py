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

'train-data_01-07-2019_14-09-05.npy': [[2808,2865]],

'train-data_01-07-2019_14-29-03.npy': [[0,1],2681,2843[]],

#'train-data_01-07-2019_14-42-36.npy':# [[965,1082]]  No inputs...

#'train-data_01-07-2019_14-43-46.npy': # no inputs... all from the same track...

#'train-data_01-07-2019_14-45-53.npy' # no inputs again...

'train-data_01-07-2019_14-55-47.npy': [[0,3],[1520,1540],[3520,3564]], # a lot of bumping in this one that I didn't remove

'train-data_01-07-2019_15-00-53.npy': [[0,8],[2420,2523]], # one bump in this that I didn't remove

'train-data_02-07-2019_22-49-06.npy': [[0,33],[3281,3289]], # going off road once that I didn't remove

'train-data_02-07-2019_22-53-42.npy': [[0,3],[750,826]],



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
