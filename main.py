from tkinter import *
from player import player


win = Tk()
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("%dx%d" % (w,h))
win.title('Space Invaders')
win.attributes('-fullscreen', True)
win['bg'] = 'black'
player = player(win)
player.can_player.pack()

win.mainloop()