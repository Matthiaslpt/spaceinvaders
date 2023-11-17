from tkinter import *
from PIL import Image, ImageTk

class bullet:
    def __init__(self,player):
        self.player = player
        self.pos= player.pos
        self.image = Image.open('image/bullet.png')
        self.image = self.image.resize((70, 70))
        self.image = ImageTk.PhotoImage(self.image)
        self.bullet_item = self.player.win.canva.create_image(self.pos[0],self.pos[1] - 80, image=self.image)

    def move(self):
        self.player.win.canva.move(self.bullet_item ,0, -30)
        if self in self.player.file_bullets:
            self.player.win.update(self.move)
