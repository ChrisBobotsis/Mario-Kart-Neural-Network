# This scripts is used to generate training data to be analyzed by the gui

import time
import keyboard
import numpy as np
from win32gui_screen import grab_screen
from key_record import keyboard_event_to_key_letter, key_letter_to_vector



# Initialize some variables

train_on = True

screen_list = []
key_list = []

# Start countdown

for i in range(5):
    print(5-i)
    time.sleep(1)



while train_on:
    print('Recording_keys')
    # Start key_board recording   TODO maybe this isn't enough time to get the keyspresses, not sure...

    keyboard.start_recording()

    # Get screen of emulator

    screen_list.append(grab_screen())

    # Delay time

    time.sleep(0.01)

    # Finish keyboard recording

    keys = keyboard.stop_recording()

    key_list.append(keys) 

    # Check if stop key pressed

    for key in keys:
        if key.name == 'q':
            train_on = False
            break # No need to waste time checking more key names

    
# Postprocessing: Change keys to names and then one-hot vectors, cut off X number of frames (and therefore inputs) since they will be pressing escape

assert len(key_list) == len(screen_list), "Number of keys and frames not equal!"

for idx in range(len(key_list)):
    key_list[idx] = key_letter_to_vector(keyboard_event_to_key_letter(key_list[idx])) # key_list should be a one-hot array of (6,1)


# Add them to a numpy file

output = []

for idx in range(len(key_list)):
    output.append(np.array((key_list[idx],screen_list[idx])))

# Save to a file

year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%H,%M,%S").split(',')
# We save the time to the file so that we don't overwrite anything
np.save(arr = output, file = f'data/training_data/raw/train-data_{day}-{month}-{year}_{hour}-{minute}-{second}') 

print('Done')


'''>>> c = []
>>> c.append(np.array((a,b))
... )
>>> c.append(np.array((a,b)))
>>> c
[array([array([1, 1, 1, 1, 1]),
       array([[[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]],

       [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]])], dtype=object), array([array([1, 1, 1, 1, 1]),
       array([[[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]],

       [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]])], dtype=object)]'''