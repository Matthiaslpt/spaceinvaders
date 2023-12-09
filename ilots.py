from tkinter import *
from PIL import Image, ImageTk
import random

class Ilots:
    def __init__(self, win):
        self.win = win
        self.row = 1
        self.column = 0
        self.pos = [0, 0]
        self.image_paths = ['image/ilots.png', 'image/ilots_2.png']
        self.current_image_index = 0
        self.load_image()
        self.ilots_item = None
        self.health = 3
        self.max_health = 3
        self.regeneration_rate = 1
        self.regeneration_interval = 5000

        self.regenerate()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 80))
        self.image = ImageTk.PhotoImage(self.image)

    def create_ilots(self, column):
        self.column = column
        player_hitbox = self.win.canva.bbox(self.win.player.player_item)
        x = player_hitbox[0] + (player_hitbox[2] - player_hitbox[0]) // 2 + 100 * column
        y = player_hitbox[1] - 100
        self.pos = [x, y]
        self.ilots_item = self.win.canva.create_image(x, y, image=self.image)

    def destroy_ilots(self):
        self.win.canva.delete(self.ilots_item)

    def damage(self):
        self.health -= 1
        if self.health <= 0:
            self.destroy_ilots()
            self.win.ilots_list.remove(self)
        else:
            self.update_ilots_image()

    def update_ilots_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_image()
        self.win.canva.itemconfig(self.ilots_item, image=self.image)

    def regenerate(self):
        if self.health < self.max_health:
            self.health += 1
            self.update_ilots_image()
        self.win.root.after(self.regeneration_interval, self.regenerate)
