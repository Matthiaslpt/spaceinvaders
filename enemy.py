from tkinter import *
import random as r

class Enemy:
    def __init__(self, win):
        self.win = win
        self.p = [r.randint(0, win.winfo_screenwidth()), 200]
        self.direction = 1
        self.speed = 2
        larg, haut = win.winfo_screenwidth(), win.winfo_screenheight()  
        self.pos = (larg, haut)
        self.can_enemy = Canvas(win, width=larg, height=500, background='white')
        self.image_png = PhotoImage(file='image/alien.png')
        self.enemy_item = self.can_enemy.create_image(larg/2, haut/2, image=self.image_png)
        self.move()

    def move(self):
        if self.p[0] < 15 or self.p[0] > 1900:
            self.direction *= -1
        elif self.p[0] < 10:
            self.p[1] += 100
        self.p[0] += self.speed * self.direction
        self.can_enemy.move(self.enemy_item, self.speed * self.direction, 0)  
        self.win.after(10, self.move)


