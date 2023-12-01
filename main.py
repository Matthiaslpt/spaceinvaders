from tkinter import *
from window import Window
from player import Player
from enemy import Enemy
from game_update import Game_update

win = Window()
player = Player(win)
updt = Game_update(win, player)
win.button.pack(anchor='ne')
win.canva.pack()
win.root.bind("<Key>", player.move)
win.root.bind("<KeyRelease>", player.stop_moving)
win.root.bind("<space>", player.shoot)
win.root.bind("<Escape>", lambda event: win.root.destroy())


win.root.mainloop()