from tkinter import *
from PIL import Image, ImageTk

class bullet:
    def __init__(self,player, id):
        self.player = player
        self.pos= player.pos
        self.image = Image.open('image/bullet.png')
        self.image = self.image.resize((70, 70))
        self.image = ImageTk.PhotoImage(self.image)
        self.bullet_item = self.player.win.canva.create_image(self.pos[0],self.pos[1] - 80, image=self.image)
        self.id = id

    def move(self):
        self.player.win.canva.move(self.bullet_item ,0, -30)
        self.pos[1]-=30
        print(self.player.file_bullets)
        if self.pos[1]>100:
            self.player.win.root.after(10,self.move)
        else:
            # Remove the bullet when it goes off the canvas
            self.player.win.canva.delete(self.bullet_item)
            self.player.file_bullets.remove(self)
            self.pos= self.player.pos
            print("done")

    def place(self):
        # Update the position of the bullet on the canvas
        self.player.win.canva.coords(self.bullet_item, self.pos[0], self.pos[1] - 80)

