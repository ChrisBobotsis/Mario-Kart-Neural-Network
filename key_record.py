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

#######
'''recorded = keyboard.record(until='esc')

import pdb; pdb.set_trace()'''
#######


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
        key_list.append(list(set([i.name for i in recorded if i.event_type != 'down'])))

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