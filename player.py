from tkinter import *
from PIL import ImageTk

class player:
    def __init__(self, win):
        self.health = 100 
        self.pos = (0,0)
        self.image = ImageTk.PhotoImage(file='image/player.png')  
        self.can_player = Canvas(win , width=win.winfo_screenmmwidth(), height=win.winfo_screenmmwidth(), background='black')
        self.player_item = self.can_player.create_image(0,0,image=self.image)
        
    def move(self,event):
        touche = event.keysym
        if touche == 'q':
            self.pos[0] -= 15
        elif touche == 'd':
            self.pos[0] += 15
        self.can_player.coords(self.player_item, self.pos[0],self.pos[1] )
        self.can_player.bind('<Key>', move)