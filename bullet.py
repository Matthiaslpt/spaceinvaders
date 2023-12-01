from tkinter import *
from PIL import Image, ImageTk

class Bullet:
    def __init__(self, player, direction):
        self.player = player
        self.pos = [player.pos[0], player.pos[1]]
        print(self.pos)
        self.image = Image.open('image/bullet.png')
        self.image = self.image.resize((70, 70))
        self.image = ImageTk.PhotoImage(self.image)
        self.bullet_item = player.win.canva.create_image(self.pos[0], self.pos[1] - 80, image=self.image)
        self.direction = direction

    def move(self):
        self.player.win.canva.move(self.bullet_item, 0, -1)
        self.pos[1] -= 1* self.direction
        if self.pos[1] > 0:
            # Call the move method recursively after a delay (e.g., 10 milliseconds)
            self.player.win.root.after(10, self.move)
        else:
            if self in self.player.file_bullets_player:
                self.player.win.canva.delete(self.bullet_item)
                self.player.file_bullets_player.remove(self)

    def place(self):
        # Update the position of the bullet on the canvas
        self.player.win.canva.coords(self.bullet_item, self.pos[0], self.pos[1] - 80)