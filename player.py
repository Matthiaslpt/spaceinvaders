from tkinter import *

class player:
    def __init__(self, win):
        self.win = win
        self.health = 100 
        self.image = PhotoImage(file='image/player.png')
        larg , hauteur = win.winfo_screenwidth(), win.winfo_screenheight()  
        self.pos=[larg/2, 40]
        self.can_player = Canvas(win , width=larg, height=150, background='white')
        self.player_item = self.can_player.create_image(self.pos[0],self.pos[1],image=self.image)
        
    def move(self,event):
        touche = event.keysym
        if touche == 'q' and self.pos[0] > 30:
            self.can_player.move(self.player_item,-10,0)
            self.pos[0]-=10
        elif touche == 'd' and self.pos[0] < self.win.winfo_screenwidth() -30:
            self.can_player.move(self.player_item,10,0)
            self.pos[0]+=10

    def shoot(self,event):
        touche = event.keysymds