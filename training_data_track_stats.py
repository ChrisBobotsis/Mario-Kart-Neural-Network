# This script will go through all filtered training data and see how many samples there are for each track. 
# We want the same amount for each track

import numpy as np
import pandas as pd
import os


'''
Mushroom Cup:

Mario Circuit 1
Donut Plains 1
Ghost Valley 1
Bowser Castle 1
Mario Circuit 2

Flow Cup:

Choco Island 1
Ghost Valley 2
Donut Plains 2
Bowser Castle 2
Mario Circuit 3

Star Cup:

Koopa Beach 1
Choco Island 2
Vanilla Lake 1
Bowser Castle 3
Mario Circuit 4

'''

class Mushroom_Cup(object):

    def __init__(self):
        self.Mario_Circuit_1 = 0
        self.Donut_Plains_1 = 0
        self.Ghost_Valley_1 = 0
        self.Bowser_Castle_1 = 0
        self.Mario_Circuit_2 = 0

class Flower_Cup(object):

    def __init__(self):

        self.Choco_Island_1 = 0
        self.Ghost_Valley_2 = 0
        self.Donut_Plains_2 = 0
        self.Bowser_Castle_2 = 0
        self.Mario_Circuit_3 = 0

class Star_Cup(object):

    def __init__(self):

        self.Koopa_Beach_1 = 0
        self.Choco_Island_2 = 0
        self.Vanilla_Lake_1 = 0
        self.Bowser_Castle_3 = 0
        self.Mario_Circuit_4 = 0

mushroom_cup = Mushroom_Cup()
flower_cup = Flower_Cup()
star_cup = Star_Cup()

data_list = os.listdir('data/training_data/filtered')

data_path = 'data/training_data/filtered/'

unknown = 0

for item in data_list:

    samples = len(np.load(data_path+item))

    if 'Mario_Circuit_1' in item:
        mushroom_cup.Mario_Circuit_1 += samples
    elif 'Donut_Plains_1' in item:
        mushroom_cup.Donut_Plains_1 += samples
    elif 'Ghost_Valley_1' in item:
        mushroom_cup.Ghost_Valley_1 += samples
    elif 'Bowser_Castle_1' in item:
        mushroom_cup.Bowser_Castle_1 += samples
    elif 'Mario_Circuit_2' in item:
        mushroom_cup.Mario_Circuit_2 += samples
    elif 'Choco_Island_1' in item:
        flower_cup.Choco_Island_1 += samples
    elif 'Ghost_Valley_2' in item:
        flower_cup.Ghost_Valley_2 += samples
    elif 'Donut_Plains_2' in item:
        flower_cup.Donut_Plains_2 += samples
    elif 'Bowser_Castle_2' in item:
        flower_cup.Bowser_Castle_2 += samples
    elif 'Mario_Circuit_3' in item:
        flower_cup.Mario_Circuit_3 += samples
    elif 'Koopa_Beach_1' in item:
        star_cup.Koopa_Beach_1 += samples
    elif 'Choco_Island_2' in item:
        star_cup.Choco_Island_2 += samples
    elif 'Vanilla_Lake_1' in item:
        star_cup.Vanilla_Lake_1 += samples
    elif 'Bowser_Castle_3' in item:
        star_cup.Bowser_Castle_3 += samples
    elif 'Mario_Circuit_4' in item:
        star_cup.Mario_Circuit_4 += samples
    else:
        unknown += 1


cups = [mushroom_cup,flower_cup,star_cup]

for cup in cups:

    print('\n\n')
    
    values = vars(cup)

    for track in values.keys():
        print(track+':    '+str(values[track]))
    
print('\n\n')   

print('Uknown Tracks:   '+str(unknown))



