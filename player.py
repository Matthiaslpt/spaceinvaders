from tkinter import *
from PIL import Image,ImageTk
from bullet import bullet

class player:
    def __init__(self, win):
        self.win = win
        self.health = 100 
        self.w , self.h = win.root.winfo_screenwidth(), win.root.winfo_screenheight()  
        self.pos=[self.w/2, self.h -100]
        self.image = Image.open('image/player.png')
        self.image = self.image.resize((150, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.player_item = self.win.canva.create_image(self.pos[0],self.pos[1],image=self.image)
        self.file_bullets = []
        self.nb_tirs = 0
        
    def move(self,event):
        touche = event.keysym
        if touche == 'q' and self.pos[0] > 80:
            self.win.canva.move(self.player_item,-30,0)
            self.pos[0]-=30
        elif touche == 'd' and self.pos[0] < self.win.root.winfo_screenwidth() - 80:
            self.win.canva.move(self.player_item,30,0)
            self.pos[0]+=30

    def shoot(self,event=None):
        self.file_bullets.append(bullet(self, self.nb_tirs))
        self.nb_tirs+=1
        print("tir")
        for i in self.file_bullets:
            i.move()


    def afficher_projectiles(self):
        if len(self.file_bullets)>0:
            for bullet in self.file_bullets:
                bullet.place()