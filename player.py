from tkinter import *

class player:
    def __init__(self):
        self.health = 100
        self.pos = (x,y)
        self.damage = 5
        self.can_player = Canvas(win , width = 300, height=300)
        self.image_png = PhotoImage(file='image/player.gif')
        self.player_item = self.can_player.create_image(300,300, image=self.image_png)
