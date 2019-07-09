from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk,Image  
import time
import numpy as np

# https://stackoverflow.com/questions/43768894/loop-through-images-with-tkinter-canvas-in-python

# https://www.tutorialspoint.com/python/python_gui_programming.htm

# https://stackoverflow.com/questions/7573031/when-i-use-update-with-tkinter-my-label-writes-another-line-instead-of-rewriti/7582458#7582458

# https://www.reddit.com/r/learnpython/comments/6cs6xb/dynamically_update_element_of_a_tkinter_window/


HEIGHT = 600 
WIDTH = 1300

SNES_HEIGHT = 295
SNES_WIDTH = 560

BUTTON_OFFSET = 10

Y_OFFSET = 20

    # c (forward)                           [1,0,0,0,0,0]
    # c (forward), left                     [0,1,0,0,0,0]
    # c (forward), right                    [0,0,1,0,0,0]
    # c (forward), right, x (drift)         [0,0,0,1,0,0]
    # c (forward), left, x (drift)          [0,0,0,0,1,0]
    # no input                              [0,0,0,0,0,1]


def array_to_img(self,arr):
    if arr[0] == 1:
        controller = self.controller_img_list[0]
    elif arr[1] == 1:
        controller =  self.controller_img_list[1]
    elif arr[2] == 1:
        controller = self.controller_img_list[2]
    elif arr[3] == 1:
        controller = self.controller_img_list[3]
    elif arr[4] == 1:
        controller = self.controller_img_list[4]
    else:
        controller = self.controller_img_list[5]

    return controller

def array_to_desc(arr):
    if arr[0] == 1:
        controller = 'forward'
    elif arr[1] == 1:
        controller =  'forward_left'
    elif arr[2] == 1:
        controller = 'forward_right'
    elif arr[3] == 1:
        controller = 'forward_right_drift'
    elif arr[4] == 1:
        controller = 'forward_left_drift'
    else:
        controller = 'no_input' 

    return controller

dict_desc_to_img_name = {

    'forward':'controller_images/snes_560by295_forward.jpg',

    'forward_left': 'controller_images/snes_560by295_forward_left.jpg',

    'forward_right': 'controller_images/snes_560by295_forward_right.jpg',

    'forward_right_drift': 'controller_images/snes_560by295_forward_right_drift.jpg',

    'forward_left_drift': 'controller_images/snes_560by295_forward_left_drift.jpg',

    'no_input': 'controller_images/snes_560by295.jpg'    
}

class Window(Frame):    

    def __init__(self,master=None):   # data_file, frame ?

        Frame.__init__(self,master)

        self.master = master
        #self.master.height = HEIGHT
        #self.master.width = WIDTH
        self.master.geometry(f'{WIDTH}x{HEIGHT}')
        self.data_file = None
        self.frame = 0
        self.max_frame = None
        self.pause = True
        self.fps = 5
        self.controller_img_list = []

        self.frame_display = None
        self.snes_img = None
        self.controller_img = None

        self.enter_time = None

        self.initialize()

        
    

    def initialize(self):

        self.add_pause_play_button()
        self.add_fwd_rev_button()
        self.add_frame_display()
        self.add_frame_selection_entry()
        self.add_menu()
        self.add_controller_label()
        self.add_emulator_label()

        self.add_fps_button()

        self.add_controller_images()
        


    # Putting controller image on Frame

    def add_controller_label(self):

        self.controller_img = Label(self.master)#,image=self.data_file[self.frame][1])
        #controller_img.image = self.data_file[frame][1]
        self.controller_img.place(x = 50, y = 150) 


        
    def update_controller_label(self):

        img = array_to_img(self,self.data_file[self.frame][0]) # We now have the image name for the controller

        self.controller_img.configure(image=img)
        self.controller_img.image = img
        

        
    # Putting snes image on Frame

    def add_emulator_label(self):

        self.snes_img = Label(self.master)#,image=render)

        

    def update_emulator_label(self):

        

        img = Image.fromarray(self.data_file[self.frame][1])
        img = ImageTk.PhotoImage(img)
        self.snes_img.configure(image=img)
        self.snes_img.image = img



    # Setting up the menu on the top of the window
    # TODO get a command to load the file

    def add_menu(self):

        menu = Menu(self.master)
        self.master.config(menu=menu)
        menu.add_command(label='Load File',command = self.open_file)

        

    # Pause/play button

    def add_pause_play_button(self):

        pause_play = Button(self.master, text="Play/Pause", command=self.not_pause)
        pause_play.place(x = WIDTH/2-BUTTON_OFFSET, y = Y_OFFSET)

   

    def not_pause(self):

        self.pause = not(self.pause)
        if self.frame == self.max_frame:
            self.frame = 0

      

    # Forward/Reverse Frame

    def add_fwd_rev_button(self):

        fwd = Button(self.master,text = 'Fwd', command=self.frame_forward)
        fwd.place(x = WIDTH/2 + 200, y = Y_OFFSET)

        rev = Button(self.master,text = 'Rev', command=self.frame_rev)
        rev.place(x = WIDTH/2 +200-40, y = Y_OFFSET)



    def frame_forward(self):

        if self.pause == True:
            if self.frame != self.max_frame:
                self.frame = self.frame + 1
                self.update_controller_label()
                self.update_emulator_label()
                self.update_frame_display()
            else:
                self.frame = 0
                self.update_controller_label()
                self.update_emulator_label()
                self.update_frame_display()


    def frame_rev(self):

        if self.pause == True:
            if self.frame != 0:
                self.frame = self.frame - 1
                self.update_controller_label()
                self.update_emulator_label()
                self.update_frame_display()
            else:
                self.frame = self.max_frame
                self.update_controller_label()
                self.update_emulator_label()
                self.update_frame_display()
    # Frame display

    def add_frame_display(self):

        self.frame_display = Label(self.master,text='Frame:')
        self.frame_display.place(x = 20, y = Y_OFFSET)

    def update_frame_display(self):

        f = self.frame #+ 1
        self.frame_display.configure(text=f'Frame:  {f}')
        self.frame_display.text = f'Frame:    {f}'

    # Enter Frame

    def add_frame_selection_entry(self):

        enter_time_text = Label(text = 'Enter Frame: ')
        enter_time_text.place(x = 120, y = Y_OFFSET)

        self.enter_time = Entry(self.master)
        self.enter_time.place(x = 200, y = Y_OFFSET)
        self.enter_time.bind('<Return>',self.update_frame_entry)

  
    def update_frame_entry(self, event=None):

        frame = int(self.enter_time.get())

        if frame>=0 and frame<=self.max_frame:
            self.frame = frame

        self.update_controller_label()
        self.update_emulator_label()
        self.update_frame_display()


    def open_file(self):
        # Open window to select file
        self.data_file = filedialog.askopenfile(initialdir="/", title ="Select File",filetypes=(("Numpy Files",".npy"),("All Files",".")))
        # Get full directory of file -> C:/Users/...
        name = self.data_file.name
        # Close the file since we don't need it now
        self.data_file.close()
        self.data_file = np.load(name)
        self.max_frame = len(self.data_file)-1 # len doesn't include 0 index

        # Auto centering snes image regardles of image size
        snes_height = self.data_file[0][1].shape[0]
  
        snes_height = (HEIGHT - snes_height)/2 - 10
       
        self.snes_img.place(x = WIDTH/2 + 70, y = snes_height) 
        
        self.frame = 0

        self.update_controller_label()
        self.update_emulator_label()

        
        self.update_frame_display()
        self.update_frame()
        #import pdb; pdb.set_trace()
        

    def update_frame(self):
        #print("Updating Frame")
        if self.pause != True :
            if self.frame == self.max_frame:
                self.update_controller_label()
                self.update_emulator_label()
                #self.frame = 0
                self.pause = True
                
            else:
                self.update_controller_label()
                self.update_emulator_label()
                self.update_frame_display()
                self.frame = self.frame + 1
            
        self.master.after(ms=int(1000/self.fps),func=self.update_frame)



    def add_controller_images(self):


        img_file = Image.open('controller_images/snes_560by295_forward.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)

        img_file = Image.open('controller_images/snes_560by295_forward_left.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)

        img_file = Image.open('controller_images/snes_560by295_forward_right.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)

        img_file = Image.open('controller_images/snes_560by295_forward_right_drift.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)

        img_file = Image.open('controller_images/snes_560by295_forward_left_drift.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)
    
        img_file = Image.open('controller_images/snes_560by295.jpg')
        render = ImageTk.PhotoImage(img_file)
        img_file.close()
        self.controller_img_list.append(render)

                
    def add_fps_button(self):

        fps = Button(self.master,text='Change FPS',command=self.update_fps)
        fps.place(x=WIDTH/2 - 200,y=Y_OFFSET)


    def update_fps(self):

        #if self.pause == True:
        self.fps = self.fps+5

        if self.fps > 30:
            self.fps = 5

if __name__ == "__main__":
    
    root = Tk()  
   
   
    snes_window = Window(root)
    #snes_window.master.after(delay=int(1000/snes_window.fps),callback=snes_window.update_frame())
  


    root.mainloop()