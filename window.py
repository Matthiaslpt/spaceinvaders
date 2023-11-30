from tkinter import *
from PIL import Image,ImageTk

class Window:
    def __init__(self):
        self.root = Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canva = Canvas(self.root, width=self.w, height=self.h, background='black',borderwidth=0, highlightthickness=0)
        self.image = Image.open('image/bckgrnd.png')
        self.image = self.image.resize((self.w*2, self.h*2))
        self.image = ImageTk.PhotoImage(self.image)
        self.bckgrnd = self.canva.create_image(0 ,0 ,image= self.image)
        self.root.geometry("%dx%d" % (self.w,self.h))
        self.root.title('Space Invaders')
        self.root.attributes('-fullscreen', True)
        self.root['bg'] = 'black'
        self.button= Button(self.root,text='Tchao', command=self.root.destroy)


        
