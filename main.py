from tkinter import *
from window import Window
from player import Player

win = Window()
player = Player(win)
win.button.pack(anchor='ne')
win.canva.pack()
win.root.bind("<Key>", player.move)
win.root.bind("<KeyRelease>", player.stop_moving)
win.root.bind("<space>", player.shoot)







win.root.mainloop()