# This python script records a set of keys pressed in batches (pressing the )

# https://github.com/boppreh/keyboard#api


'''class keyboard.KeyboardEvent
KeyboardEvent.device
KeyboardEvent.event_type
KeyboardEvent.is_keypad
KeyboardEvent.modifiers
KeyboardEvent.name
KeyboardEvent.scan_code
KeyboardEvent.time
KeyboardEvent.to_json(self, ensure_ascii=False)'''

import keyboard
import time
import numpy as np

#######
'''recorded = keyboard.record(until='esc')

import pdb; pdb.set_trace()'''
#######


def key_letter_to_vector(key_list):
    # The output vector will be 6*1
    # Options for Key_presses:

    # c (forward)                           [1,0,0,0,0,0]
    # c (forward), left                     [0,1,0,0,0,0]
    # c (forward), right                    [0,0,1,0,0,0]
    # c (forward), right, x (drift)         [0,0,0,1,0,0]
    # c (forward), left, x (drift)          [0,0,0,0,1,0]
    # no input                              [0,0,0,0,0,1]

    c_flag, left_flag, right_flag, x_flag = (False,False,False,False)

    for key in key_list:
        if key == 'c':
            c_flag = True
        if key == 'x':
            x_flag = True
        if key == 'left':
            left_flag = True
        if key == 'right':
            right_flag = True

    if (c_flag & left_flag & x_flag):
        key_list = np.array([0,0,0,0,1,0])
    elif (c_flag & right_flag & x_flag):
        key_list = np.array([0,0,0,1,0,0])
    elif (c_flag & left_flag):
        key_list = np.array([0,1,0,0,0,0])
    elif (c_flag & right_flag):
        key_list = np.array([0,0,1,0,0,0])
    elif (c_flag):
        key_list = np.array([1,0,0,0,0,0])
    else:
        key_list = np.array([0,0,0,0,0,1])

    key_list = key_list.reshape(6,1) # It is currently shape (6,)

    return key_list

def keyboard_event_to_key_letter(key_list):
    key_list = (list(set([i.name for i in key_list if i.event_type == 'down'])))
    return key_list

def key_list(recorded):

    # This function will take 
    return None

if __name__ == "__main__":

    key_list = []

    loop1 = True
    esc_pressed = False

    

    while loop1:       
        
        loop2 = True
        loop3 = True
        
        keyboard.start_recording()
        
        while loop2:
            print('First Loop')
            if keyboard.is_pressed('esc'):
                loop2 = False
         

        # Note that it can contain multiple of the same types of presses (i.e. [KeyboardEvent(f down), KeyboardEvent(f down), KeyboardEvent(f down)] )
        recorded = keyboard.stop_recording()

        # This just appends a list of keys that were pressed down
        key_list.append(list(set([i.name for i in recorded if i.event_type == 'down'])))

        while loop3:
            print('Second Loop')
            if keyboard.is_pressed('q'):
                loop3 = False
                # the q tends to spill over into the keyboard.start_recording(), that's why I'm using the time.sleep
                time.sleep(0.25)
            if keyboard.is_pressed('w'):
                loop1 = False
                loop3 = False

    import pdb; pdb.set_trace()

    # Test to see what keyboard.write does. It does -> KeyboardEvent(f down), KeyboardEvent(f up)
    '''keyboard.wait(hotkey='esc')

    keyboard.write(text='f')'''