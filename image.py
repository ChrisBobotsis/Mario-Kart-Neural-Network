# Done by Frannecklp


import win32gui, win32ui, win32con, win32api
import numpy as np
from PIL import ImageGrab
import cv2
import pdb
import time


#def get_screen(title = None,width = 80, height = 60):
# http://docs.activestate.com/activepython/3.3/pywin32/win32gui.html


def grab_screen(title=None,show_time=True):


    if not title:
        # When we load the Super Mario Kart ROM into Snes9X this is what the title of the window becomes
        title = 'Super Mario Kart (USA) - Snes9x 1.60'
    # Creating window handler (handle?,) 
    # TODO check what it's called
    hwin = win32gui.FindWindow(None, title)
    # This provides the coordinates of our window. 'left' and 'right' are the x-axis; 'top' and 'bottom' are the y-axis
    (left,top,right,bottom) = win32gui.GetWindowRect(hwin)
    
    # Bar is the menu bar of the emulator that is included in the dimensions above
    bar_height = 0

    top += bar_height

    width = (right - left)
    height = (bottom - top)


    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top+100), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_RGB2BGRA)



if __name__ == "__main__":
    screen = grab_screen()
    #screen = screen[:,:]
    #crop_img = img[y:y+h, x:x+w]
    cv2.imshow("cropped", screen)
    cv2.waitKey(0)