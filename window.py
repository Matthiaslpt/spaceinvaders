from tkinter import *

class window:
    def __init__(self):
        self.root = Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.w,self.h))
        self.root.title('Space Invaders')
        self.root.attributes('-fullscreen', True)
        self.root['bg'] = 'black'
        self.button=Button(self.root,text='Tchao', command=self.root.destroy)   