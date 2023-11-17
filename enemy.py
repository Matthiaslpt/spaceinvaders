from tkinter import *
import random as r


class enemy :
    def __init__(self,win) :
        self.p=[r.randint(win.winfo_screenwidth(),win.winfo_screenwidth()),200]
        self.direction=1
        self.speed=2
        larg, haut = win.winfo_screenmmwidth(), win.winfo_screenmmwidth()
        self.can_enemy=Canvas(win , width=larg, height=500, background='white')
        self.image_png = PhotoImage(file='image/alien.png')
        self.enemy_item = self.can_enemy.create_image(larg/2,haut/2,image=self.image_png)

    def move(self):
        if self.pos[0]<15 or self.pos[0]>1900:
            self.direction*=-1
        elif self.pos[0]<10:
            self.pos[1]+=100
        self.pos[0]+=self.speed*self.direction
        self.can_enemy.move(self.enemy_item,self.pos[0],self.pos[1])
        self.after(10,self.move)


