# Done by Frannecklp


import win32gui, win32ui, win32con, win32api
import numpy as np
from PIL import ImageGrab
import cv2
import pdb
import time
import pyautogui


#def get_screen(title = None,width = 80, height = 60):
# http://docs.activestate.com/activepython/3.3/pywin32/win32gui.html

# http://timgolden.me.uk/pywin32-docs/win32ui.html
# http://docs.activestate.com/activepython/3.3/pywin32/win32gui.html
# 


def grab_screen(title=None):


    if not title:
        # When we load the Super Mario Kart ROM into Snes9X this is what the title of the window becomes
        title = 'Super Mario Kart (USA) - Snes9x 1.60'
    # Creating window handle
    hwin = win32gui.FindWindow(None, title)
    # This provides the coordinates of our window. 'left' and 'right' are the x-axis; 'top' and 'bottom' are the y-axis
    bbox = win32gui.GetWindowRect(hwin)

    img = ImageGrab.grab(bbox)


    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    # return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)



if __name__ == "__main__":
    show_time = False
    last_time = time.time()
    while True:
        screen = grab_screen()
        cv2.imshow('test',screen)
        if show_time:
            print(f'Loop took {time.time()-last_time}')
        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break