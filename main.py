from tkinter import *
from window import window
from player import player
from enemy import enemy

win = window()
player = player(win)
win.canva.pack()
win.root.bind("<KeyPress>", player.move)
win.root.bind("<space>", player.shoot)
win.button.pack(anchor='ne')
enemy = enemy(win.root)
enemy.can_enemy.pack()





win.root.mainloop()