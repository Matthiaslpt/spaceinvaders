from tkinter import *
from PIL import Image, ImageTk


class Ilots:
    def __init__(self, win):
        self.win=win
        self.image = Image.open('image/bullet.png')
        self.image = self.image.resize((70, 70))
        self.image = ImageTk.PhotoImage(self.image)
        
