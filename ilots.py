from tkinter import *
from PIL import Image, ImageTk


class Ilots:
    def __init__(self, win, row, column):
        self.win = win
        self.row = row
        self.column = column
        self.pos = [50 + 100 * self.column, self.win.h - 120 - 80 * self.row]
        self.image = Image.open('image/ilots.png')
        self.image = self.image.resize((100, 80))
        self.image = ImageTk.PhotoImage(self.image)
        self.ilots_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.health = 3  # Initial health of the obstacle

    def damage(self):
        self.health -= 1
        if self.health <= 0:
            self.win.canva.delete(self.ilots_item)
            self.win.ilots_list.remove(self)