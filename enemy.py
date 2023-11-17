from tkinter import *
import random as r


class enemy :
    def __init__(self,window) :
        self.p=[r.randint(window.winfo_screenwidth(),window.winfo_screenwidth()),200]
        self.direction=1
        self.speed=2
        larg = window.winfo_screenmmwidth()
        haut=window.winfo_screenmmwidth()
        self.can_enemy=Canvas(window , width=larg, height=haut, background='black')
        self.image_png = PhotoImage(file='image/alien.png')
        self.enemy_item = self.can_enemy.create_image(larg/2,haut/2,image=self.image_png)

    def move(self):
        if self.pos[0]<15 or self.pos[0]>1900:
            self.direction*=-1
        if self.pos[0]<10:
            self.pos[1]+=100
        self.pos[0]+=self.speed*self.direction
        self.can_enemy.move(self.enemy_item,self.pos[0],self.pos[1])