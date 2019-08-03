
import numpy as np
import os
from PIL import Image
from random import shuffle

    # c (forward)                           [1,0,0,0,0,0]
    # c (forward), left                     [0,1,0,0,0,0]
    # c (forward), right                    [0,0,1,0,0,0]
    # c (forward), right, x (drift)         [0,0,0,1,0,0]
    # c (forward), left, x (drift)          [0,0,0,0,1,0]
    # no input                              [0,0,0,0,0,1]


class Input_List(object):

    def __init__(self):
        self.forward = []
        self.forward_left = []
        self.forward_right = []
        self.forward_right_drift = []
        self.forward_left_drift = []
        self.no_input = []

    def append_data(self,vec,img):

        if (vec[0] == 1)[0]:

            self.forward.append([vec,img])

        elif (vec[1] == 1)[0]:

            self.forward_left.append([vec,img])

        elif (vec[2] == 1)[0]:

            self.forward_right.append([vec,img])

        elif (vec[3] == 1)[0]:

            self.forward_right_drift.append([vec,img])

        elif (vec[4] == 1)[0]:

            self.forward_left_drift.append([vec,img])

        elif (vec[5] == 1)[0]:

            self.no_input.append([vec,img])

    def min(self):

        min = len(self.forward)

        if len(self.forward_left) < min:

            min = len(self.forward_left)

        if len(self.forward_right) < min:

            min = len(self.forward_right)

        if len(self.forward_right_drift) < min:

            min = len(self.forward_right_drift)

        if len(self.forward_left_drift) < min:

            min = len(self.forward_left_drift)

        return min

    def trim_lists(self,min):

        shuffle(self.forward)
        shuffle(self.forward_left)
        shuffle(self.forward_right)
        shuffle(self.forward_right_drift)
        shuffle(self.forward_left_drift)

        self.forward = self.forward[0:min]
        self.forward_left = self.forward_left[0:min]
        self.forward_right = self.forward_right[0:min]
        self.forward_right_drift = self.forward_right_drift[0:min]
        self.forward_left_drift = self.forward_left_drift[0:min]



def shuffle_input_list(input_list):

    data = []

    for item in input_list.forward:

        data.append(item)

    for item in input_list.forward_left:

        data.append(item)

    for item in input_list.forward_right:

        data.append(item)

    for item in input_list.forward_right_drift:

        data.append(item)

    for item in input_list.forward_left_drift:

        data.append(item)

    for item in input_list.no_input:

        data.append(item)

    shuffle(data)

    return data
        


keys_to_vec = {

                    'forward': np.array([1,0,0,0,0,0]).reshape(6,1),

                    'forward_left': np.array([0,1,0,0,0,0]).reshape(6,1),

                    'forward_right': np.array([0,0,1,0,0,0]).reshape(6,1),

                    'forward_right_drift': np.array([0,0,0,1,0,0]).reshape(6,1),

                    'forward_left_drift': np.array([0,0,0,0,1,0]).reshape(6,1),

                    'no_input': np.array([0,0,0,0,0,1]).reshape(6,1)
}


def isMirrorable(vec):
    mirrorable = False

    vec_test = np.array([0,1,1,1,1,0]).reshape(1,6)

    if np.dot(vec_test,vec)[0][0] > 0:
        mirrorable = True
    
    return mirrorable

def mirror_img(img):

    img = Image.fromarray(img)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = np.array(img)
    
    return img


def mirror(vec,img):

    def mirror_img(img):
    
        img = Image.fromarray(img)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img = np.array(img)
        
        return img
    #import pdb; pdb.set_trace()
    if (vec[1] == 1)[0] == True: # implies forward left

        new_vec = keys_to_vec['forward_right']
        new_img = mirror_img(img)

    elif (vec[2] == 1)[0] == True: # implies forward right

        new_vec = keys_to_vec['forward_left']
        new_img = mirror_img(img)

    elif (vec[3] == 1)[0] == True: # implies forward right drift

        new_vec = keys_to_vec['forward_left_drift']
        new_img = mirror_img(img)

    elif (vec[4] == 1)[0] == True: # implies forward left drift

        new_vec = keys_to_vec['forward_right_drift']
        new_img = mirror_img(img)

    return new_vec,new_img



if __name__ == "__main__":

    full_data_set_dir = 'data/training_data/4-full_data_set/'
    final_dataset_dir = 'data/training_data/5-final_data_set/'

    file_name = os.listdir(full_data_set_dir)
    assert len(file_name) == 1, f'There is more than one file in {full_data_set_dir}'
    file_name = file_name[0]
    training_data = np.load(full_data_set_dir+file_name)

    input_list = Input_List()

    for idx in range(len(training_data)):

        vec = training_data[idx][0]
        img = training_data[idx][1]

        input_list.append_data(vec,img)

        if isMirrorable(vec) == True:

            mirror_vec,mirror_img = mirror(vec,img)

            input_list.append_data(mirror_vec,mirror_img)
        

    assert input_list.min() > len(input_list.no_input), "More \'no_inputs\' than another type!"
    #import pdb; pdb.set_trace()
    input_list.trim_lists(input_list.min())
    print(f'Min: {input_list.min()}')
    final_dataset = shuffle_input_list(input_list)

    np.save(file=final_dataset_dir+file_name,arr=final_dataset)



