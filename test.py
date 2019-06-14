import win32gui, win32ui, win32con, win32api
import numpy as np
import time

title = 'Super Mario Kart (USA) - Snes9x 1.60'

# Creating window handle
hwin = win32gui.FindWindow(None, title)
# This provides the coordinates of our window. 'left' and 'right' are the x-axis; 'top' and 'bottom' are the y-axis
(left,top,right,bottom) = win32gui.GetWindowRect(hwin)

width = right - left
height = bottom - top

while True:

    win32gui.MoveWindow(hwin,left,top,width+50,height+50,True)
    time.sleep(5)
    win32gui.MoveWindow(hwin,left,top,width-50,height-50,True)
    time.sleep(5)


