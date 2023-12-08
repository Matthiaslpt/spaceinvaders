from tkinter import *
from PIL import Image, ImageTk
from bullet import Bullet
import time

class Player:
    def __init__(self, win):
        self.win = win
        self.health = 3
        self.pos = [self.win.w / 2, self.win.h - 100]
        self.image = Image.open('image/player.png')
        self.image = self.image.resize((150, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.player_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.file_bullets = []
        self.nb_tirs = 0
        self.win.root.bind("<space>", self.shoot)
        self.cooldown_time = 0.3
        self.last_shot_time = 0.0


        win.root.bind("<q>", self.left)
        win.root.bind("<d>", self.right)
        win.root.bind("<KeyRelease>", self.stop)
        win.root.bind("<space>", self.shoot)
        # Start the update loop for bullets
        self.update_bullets()


    def left(self):
        self.win.canva.move(self.player_item, -30, 0)
        self.pos[0] -= 30

    def right(self):
        self.win.canva.move(self.player_item, 30, 0)
        self.pos[0] += 30

    def move(self, event):
        if not self.win.game_over:
            touche = event.keysym
            if touche == 'q' and self.pos[0] > 80:
                self.win.canva.move(self.player_item, -30, 0)
                self.pos[0] -= 30
            elif touche == 'd' and self.pos[0] < self.win.w - 80:
                self.win.canva.move(self.player_item, 30, 0)
                self.pos[0] += 30
            
            elif touche == 'k':
                self.health = 0
                self.win.game_over = True
                self.win.display_game_over()

    def stop(self, event):
        pass

    def shoot(self, event=None):
        if not self.win.game_over:
            current_time = time.time()
            if current_time - self.last_shot_time >= self.cooldown_time:
                new_bullet = Bullet(self, 1, self.win)
                self.file_bullets.append(new_bullet)
                self.last_shot_time = current_time

    def update_bullets(self):
        for bullet in self.file_bullets:
            bullet.move()
        for bullet in self.win.file_bullets:
            bullet.move()

        if not self.win.game_over:
            self.win.root.after(10, self.update_bullets)
