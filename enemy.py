from tkinter import *
import random as r
from PIL import Image, ImageTk
from bullet import Bullet

class Enemy:
    def __init__(self, win):
        self.larg, self.haut = win.root.winfo_screenwidth(), win.root.winfo_screenheight()
        self.win = win
        self.pos = [r.randint(50, self.larg-90), 60]
        self.direction = 1
        self.speed = 4
        self.image = Image.open('image/alien.png')
        self.image = self.image.resize((200, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.enemy_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.shooting = True
        self.move()
        self.shoot()

    def move(self):
        if self.pos[0] < +40 or self.pos[0] > self.larg -80:
            self.direction *= -1
        elif self.pos[0] < 45:
            self.pos[1] += 100
            self.win.canva.move(self.enemy_item, 0, 100)  
            self.direction *= -1 
        self.pos[0] += self.speed * self.direction
        self.win.canva.move(self.enemy_item, self.speed * self.direction, 0)  
        self.win.root.after(10, self.move)



    def shoot(self):
        if self.shooting:
            new_bullet = Bullet(self, -1, self.win)
            self.win.file_bullets.append(new_bullet)
            self.win.root.after(6000, self.shoot)

