from tkinter import *
from PIL import Image, ImageTk

class Bullet:
    def __init__(self, item, direction, win):
        self.item = item
        self.win = win
        self.h = win.root.winfo_screenwidth()
        self.pos = [item.pos[0], item.pos[1]]
        self.image = Image.open('image/bullet.png')
        self.image = self.image.resize((70, 70))
        self.image = ImageTk.PhotoImage(self.image)
        self.bullet_item = item.win.canva.create_image(self.pos[0], self.pos[1] - 80*direction, image=self.image)
        self.direction = direction

    def move(self):
        self.item.win.canva.move(self.bullet_item, 0, -1*self.direction)
        self.pos[1] -= 1* self.direction
        if self.pos[1] > 0 and self.pos[1] < self.h:
            # Call the move method recursively after a delay (e.g., 10 milliseconds)
            self.item.win.root.after(10, self.move)
        else:
            if self.direction == 1:
                if self in self.item.file_bullets:
                    self.item.win.canva.delete(self.bullet_item)
                    self.item.file_bullets.remove(self)
            elif self.direction == -1: 
                if self in self.win.file_bullets:
                    self.item.win.canva.delete(self.bullet_item)
                    self.win.file_bullets.remove(self)
        

    def place(self):
        # Update the position of the bullet on the canvas
        self.item.win.canva.coords(self.bullet_item, self.pos[0], self.pos[1] - 80)