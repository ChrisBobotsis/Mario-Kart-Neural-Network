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

WIDTH = 568
HEIGHT = 525

# Constants to remove black background from emulator window
MENU_BAR_HEIGHT = 52
TOP_BAR = 6
BOTTOM_BAR = 18
SIDE_BAR = 18

def grab_screen(title=None):


    if not title:
        # When we load the Super Mario Kart ROM into Snes9X this is what the title of the window becomes
        title = 'Super Mario Kart (USA) - Snes9x 1.60'
    # Creating window handle
    hwin = win32gui.FindWindow(None, title)
    # This provides the coordinates of our window. 'left' and 'right' are the x-axis; 'top' and 'bottom' are the y-axis
    (left,top,right,bottom) = win32gui.GetWindowRect(hwin)
    
    # Bar is the menu bar of the emulator that is included in the dimensions above
    #bar_height = 0

    #top += bar_height

    width = (right - left)
    height = (bottom - top)

    # width, height = shrink(width,height)

    # Width:   568, Height:   525

    # This is done so that I have the same window size for the image data. 
    win32gui.MoveWindow(hwin,left,top,WIDTH,HEIGHT,True)

    #pdb.set_trace()

    #returns int, the device context (DC) for the entire window, including title bar, menus, and scroll bars.
    hwindc = win32gui.GetWindowDC(hwin)

    # Creates a DC object from an integer handle
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    # Creates a memory device context (DC) compatible with the specified device.
    memdc = srcdc.CreateCompatibleDC()
    # CreateBitmap(width, height , cPlanes , cBitsPerPixel , bitmap bits ),  Creates a bitmap
    ''' Parameters
        dc : int
        handle to DC'''

    bmp = win32ui.CreateBitmap()

    # Creates a bitmap compatible with the device that is associated with the specified device context.
    ''' Parameters
        hdc : int
        handle to DC
        width : int
        width of bitmap, in pixels
        height : int
        height of bitmap, in pixels'''

    bmp.CreateCompatibleBitmap(srcdc, width, height)
    
     # Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.

    ''' Parameters
        hdc : int
        handle to DC
        object : int
        The GDI object'''
    
    memdc.SelectObject(bmp)

    # Performs a bit-block transfer of the color data corresponding to a rectangle of pixels from the specified source device context into a destination device context.

    ''' Parameters
        hdcDest : int
        handle to destination DC
        x : int
        x-coord of destination upper-left corner
        y : int
        y-coord of destination upper-left corner
        width : int
        width of destination rectangle
        height : int
        height of destination rectangle
        hdcSrc : int
        handle to source DC
        nXSrc : int
        x-coordinate of source upper-left corner
        nYSrc : int
        y-coordinate of source upper-left corner
        dwRop : int
        raster operation code'''
        # seems like the second (0,0) tuple fixed the issue with moving the emulator screen causing the output to shift
    memdc.BitBlt((0,0), (width, height), srcdc, (0,0), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    # (Pdb) screen.shape
    # (525, 568, 3)
    img = shrink(img)
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    # return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

def shrink(img):
    #global MENU_BAR_HEIGHT, TOP_BAR, BOTTOM_BAR, SIDE_BAR
    img = img[(MENU_BAR_HEIGHT+TOP_BAR):-BOTTOM_BAR,SIDE_BAR:-SIDE_BAR,:]
    return img

if __name__ == "__main__":
    show_time = False
    last_time = time.time()
    count = 0
    while True:
        screen = grab_screen()
        if count == 0:
            cv2.imwrite('mario-kart.png',screen)
            count = count + 1
        #import pdb; pdb.set_trace()
        cv2.imshow('test',screen)
        if show_time:
            print(f'Loop took {time.time()-last_time}')
        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break