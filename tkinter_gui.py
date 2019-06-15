from tkinter import *  
from PIL import ImageTk,Image  
import time

# https://stackoverflow.com/questions/43768894/loop-through-images-with-tkinter-canvas-in-python

# https://www.tutorialspoint.com/python/python_gui_programming.htm

# https://stackoverflow.com/questions/7573031/when-i-use-update-with-tkinter-my-label-writes-another-line-instead-of-rewriti/7582458#7582458


HEIGHT = 600 
WIDTH = 1300

SNES_HEIGHT = 295
SNES_WIDTH = 560

BUTTON_OFFSET = 10

Y_OFFSET = 20

class Window(Frame):    

    def __init__(self,master=None):

        Frame.__init__(self,master)

        self.master = master
        #self.master.height = HEIGHT
        #self.master.width = WIDTH
        self.master.geometry(f'{WIDTH}x{HEIGHT}')
        self.initialize()
    

    def initialize(self):

        self.add_pause_play_button()
        self.add_fwd_rev_button()
        self.add_frame_display()
        self.add_frame_selection_entry()
        self.add_menu()


    # Putting Snes image on Frame

    def add_controller_label(self):

        img_file = Image.open("data/snes_560by295.jpg")
        render = ImageTk.PhotoImage(img_file)
        snes_img = Label(self.master,image=render)
        snes_img.image = render
        snes_img.place(x = 50, y = 150) 

    # Putting image on Frame

    def add_emulator_label(self):

        img_file = Image.open("data/mario-kart.png")
        render = ImageTk.PhotoImage(img_file)
        controller_img = Label(self.master,image=render)
        controller_img.image = render
        controller_img.place(x= WIDTH/2 + 50, y = 75) 


    # Setting up the menu on the top of the window
    # TODO get a command to load the file

    def add_menu(self):

        menu = Menu(self.master)
        self.master.config(menu=menu)
        menu.add_command(label='Load File',command = '')

    # Pause/play button

    def add_pause_play_button(self):

        pause_play = Button(self.master, text="Play/Pause")
        pause_play.place(x = WIDTH/2-BUTTON_OFFSET, y = Y_OFFSET)

    # Forward/Reverse Frame

    def add_fwd_rev_button(self):

        fwd = Button(self.master,text = 'Fwd')
        fwd.place(x = WIDTH/2 + 200, y = Y_OFFSET)

        rev = Button(self.master,text = 'Rev')
        rev.place(x = WIDTH/2 +200-40, y = Y_OFFSET)

    # Frame display

    def add_frame_display(self):

        f = 500
        frame_display = Label(self.master,text = f'Frame:  {f}')
        frame_display.place(x = 20, y = Y_OFFSET)

    # Enter Frame

    def add_frame_selection_entry(self):

        enter_time_text = Label(text = 'Enter Frame: ')
        enter_time_text.place(x = 120, y = Y_OFFSET)

        enter_time = Entry(self.master)
        enter_time.place(x = 200, y = Y_OFFSET)

# Pack it all together

''' snes_frame.pack()


root.mainloop() '''



if __name__ == "__main__":
    
    root = Tk()  
   
   
    snes_window = Window(root)
    snes_window.add_controller_label()
    snes_window.add_emulator_label()


    root.mainloop()