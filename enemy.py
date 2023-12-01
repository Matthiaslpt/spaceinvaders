from tkinter import *
import random as r
from PIL import Image, ImageTk

class Enemy:
    def __init__(self, win):
        self.larg, self.haut = win.root.winfo_screenwidth(), win.root.winfo_screenheight()
        self.win = win
        self.p = [r.randint(50, self.larg-90), 60]
        self.direction = 1
        self.speed = 4
        self.image = Image.open('image/alien.png')
        self.image = self.image.resize((200, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.pos = (self.larg, self.haut)
        self.enemy_item = self.win.canva.create_image(self.p[0], self.p[1], image=self.image)
        self.move()

    def move(self):
        if self.p[0] < +40 or self.p[0] > self.larg -80:
            self.direction *= -1
        elif self.p[0] < 45:
            self.p[1] += 100
            self.win.canva.move(self.enemy_item, 0, 100)  
            self.direction *= -1 
        self.p[0] += self.speed * self.direction
        self.win.canva.move(self.enemy_item, self.speed * self.direction, 0)  
        self.win.root.after(10, self.move)



    def shoot(self, event=None):
        new_bullet = Bullet(self, -1)
        self.file_bullets_alien.append(new_bullet)

