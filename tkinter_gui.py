from tkinter import *  
from PIL import ImageTk,Image  
import time

# https://stackoverflow.com/questions/43768894/loop-through-images-with-tkinter-canvas-in-python

# https://www.tutorialspoint.com/python/python_gui_programming.htm


HEIGHT = 650 
WIDTH = 1300

SNES_HEIGHT = 295
SNES_WIDTH = 560

BUTTON_OFFSET = 10

Y_OFFSET = 10

root = Tk()  

snes_frame = Frame(root,height = HEIGHT, width = WIDTH)

# Putting Snes image on Frame
img_file = Image.open("data/snes_560by295.jpg")
render = ImageTk.PhotoImage(img_file)
snes_img = Label(root,image=render)
snes_img.image = render
snes_img.place(x = 50, y = 150) 

# Putting image on Frame
img_file = Image.open("data/mario-kart.png")
render = ImageTk.PhotoImage(img_file)
controller_img = Label(root,image=render)
controller_img.image = render
controller_img.place(x= WIDTH/2 + 50, y = 75) 


# Setting up the menu on the top of the window
# TODO get a command to load the file
menu = Menu(root)
root.config(menu=menu)
menu.add_command(label='Load File',command = '')

# Pause/play button
pause_play = Button(root, text="Play/Pause")
pause_play.place(x = WIDTH/2-BUTTON_OFFSET, y = Y_OFFSET)

# Forward/Reverse Frame

fwd = Button(root,text = 'Fwd')
fwd.place(x = WIDTH/2 + 200, y = Y_OFFSET)

rev = Button(root,text = 'Rev')
rev.place(x = WIDTH/2 +200-40, y = Y_OFFSET)

# Frame display
f = 500
frame_display = Label(root,text = f'Frame:  {f}')
frame_display.place(x = 20, y = Y_OFFSET)

# Enter Frame
enter_time_text = Label(text = 'Enter Time: ')
enter_time_text.place(x = 120, y = Y_OFFSET)

enter_time = Entry(root)
enter_time.place(x = 200, y = Y_OFFSET)

# Pack it all together
snes_frame.pack()


root.mainloop() 



