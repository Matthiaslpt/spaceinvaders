from tkinter import *
from window import Window
from player import Player

win = Window()
player = Player(win)
win.button.pack(anchor='ne')
win.canva.pack()








win.root.mainloop()