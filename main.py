from tkinter import *
from player import player
from enemy import enemy


win = Tk()
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("%dx%d" % (w,h))
win.title('Space Invaders')
win.attributes('-fullscreen', True)
win['bg'] = 'black'
player = player(win)
player.can_player.pack()
enemy = enemy(win)
enemy.can_enemy.pack()
quit=Button(win,text='Tchao', command=win.destroy)
quit.pack(anchor='ne',side='top')

win.mainloop()