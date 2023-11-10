from tkinter import *
from PIL import ImageTk

class player:
    def __init__(self, win):
        self.health = 100   
        self.image = ImageTk.PhotoImage(file='image/player.png')  
        self.can_player = Canvas(win , width=self.image.width(), height=self.image.height())
        self.player_item = self.can_player.create_image(0,0,image=self.image)


    def move(self):
        pass