from tkinter import *
from player import player


win = Tk()
win.title('Space Invaders')
win.attributes('-fullscreen', True)
win['bg'] = 'black'
player = player(win)
player.can_player.place(relx=0.5, rely=0.9)
win.mainloop()