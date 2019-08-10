# This script when run will play an open window of super mario kart from a snes9x window

import numpy as np
import win32gui
import keyboard
import time

from win32gui_screen import grab_screen
from preprocess_data import resize, PREPROCESS_HEIGHT, PREPROCESS_WIDTH

from tensorflow.keras.models import load_model

from PIL import Image

from conv_net import remove_mario


inputs = {

    'forward':              'c',
    'forward_left':         'c+left',
    'forward_right':        'c+right',
    'forward_right_drift':  'c+right+x',
    'forward_left_drift':   'c+left+x',
    'no_input':             None

}


def resize_32by32(img):

    img = Image.fromarray(img)
    img = img.resize((32,32))
    img = np.array(img)

    return img

def vec_to_input(vec):
    #import pdb; pdb.set_trace()
    index = vec.argmax()
    if index == 0:
        input = 'forward'
    elif index == 1:
        input = 'forward_left'
    elif index == 2:
        input = 'forward_right'
    elif index == 3:
        input = 'forward_right_drift'
    elif index == 4:
        input = 'forward_left_drift'
    else:
        input = 'no_input'

    return input

def img_to_input(img,model):

    vec = model.predict(img)

    input = vec_to_input(vec)
    print(input)
    input = inputs[input]

    return input


def keyboard_release():

    keyboard.release('c')
    keyboard.release('x')
    keyboard.release('left')
    keyboard.release('right')

    return


if __name__ == "__main__":

    filepath_dir = 'data/models/'
    file_name = 'conv_net_custom-08-03-2019_23-37-06'
    
    filepath = filepath_dir+file_name

    model = load_model(
        filepath,
        custom_objects=None,
        compile=True
    )

    s_flag = True
    count = 0

    valid_response = False

    while valid_response == False:
        input_option = input('Are you using:\n(a) 32 by 100 images\nOR\n(b) 32 by 32 images? (a/b): ')

        if input_option not in ['a','b']:
            print('Enter a valid input!')
        else:
            valid_response = True

    while s_flag==True:
        if count%20000 == 0:
            print('Waiting to start (press \'s\')')
        if keyboard.is_pressed('s'):
            s_flag = False
        count += 1

    play_on = True
    loop = True

    freq = 100
    count = 1

    X_values = []
    Y_values = []

    for i in range(5)[::-1]:
        print(i)
        time.sleep(i)
    

    # Having this loop True means the program will not end
    while loop == True:
        # This loop actually runs the model and algorithm to play mario kart
        while play_on == True:

            t = time.time()
            img = grab_screen()
            img = remove_mario(img)
            img = resize(img)
            if input_option == 'a':
                img = img.reshape(1,32,100,1)
            elif input_option == 'b':
                img = resize_32by32(img)
                img = img.reshape(1,32,32,1)

            X_values.append(img)

            img = img/255

            Y_values.append(model.predict(img))

            prediction = img_to_input(img,model)

            keyboard_release()

            if count%freq==0: 
                keyboard_release()
            elif prediction!=None:
                keyboard.press(prediction)
            
            #time.sleep(0.1)
            count+=1

            print(f'Time for loop: {time.time()-t}')
            print(f'Frequency is:   {freq}')

            if keyboard.is_pressed('w'):
                play_on = False
                keyboard_release()
                print('...Model Paused...')
                

        if keyboard.is_pressed('1'):
            freq = 1
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('2')&(not keyboard.is_pressed('down')):
            freq = 2
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('3'):
            freq = 3
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('4')& (not keyboard.is_pressed('left')):
            freq = 4
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('5'):
            freq = 5
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('6')&(not keyboard.is_pressed('right')):
            freq = 6
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('7'):
            freq = 7
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('8')&(not keyboard.is_pressed('up')):
            freq = 8
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('9'):
            freq = 9
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed('0'):
            freq = 10
            print(f'Frequency is:   {freq}')
        elif keyboard.is_pressed(']'):
            freq = 100
            print(f'Frequency is:   {freq}')

        if keyboard.is_pressed('r'):
            play_on = True
            print('...Ready to Restart!...')

        # Outer loop while model is not being used used to quit completely            
        if keyboard.is_pressed('q'):
            loop = False
            print('...Quit...')

    valid_input = False

    while not valid_input:
    
        i = input('Do you want to save that file? (Y/N):     ')

        if i not in ['Y','N']:
            print('Invalid Input, try again')
        else:
            valid_input = True

    data = []

    if i == 'Y':
        for idx in range(len(X)):
            data.append([Y[idx],X[idx]])
        np.save(arr=data,file=('data/model_analysis/'+file_name))
    elif i == 'N':
        print('Not saving file')


    
        
