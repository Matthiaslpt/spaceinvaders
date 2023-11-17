from tkinter import *
from window import window
from player import player


win = window()
player = player(win)
win.canva.pack()
win.root.bind("<KeyPress>", player.move)
win.root.bind("<space>", player.shoot)

win.root.mainloop()