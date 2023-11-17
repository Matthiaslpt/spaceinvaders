from tkinter import *
from window import window
from player import player







win = window()
player = player(win.root)
player.can_player.pack(side=BOTTOM)
win.root.bind("<KeyPress>", player.move)
win.root.mainloop()