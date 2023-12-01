from tkinter import *
from PIL import Image, ImageTk
from bullet import Bullet

class Player:
    def __init__(self, win):
        self.win = win
        self.health = 100
        self.w, self.h = win.root.winfo_screenwidth(), win.root.winfo_screenheight()
        self.pos = [self.w / 2, self.h - 100]
        self.image = Image.open('image/player.png')
        self.image = self.image.resize((150, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.player_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.file_bullets_player = []
        self.nb_tirs = 0

        # Start the update loop for bullets
        self.update_bullets()

    def move(self, event):
        touche = event.keysym
        if touche == 'q' and self.pos[0] > 80:
            self.win.canva.move(self.player_item, -30, 0)
            self.pos[0] -= 30
        elif touche == 'd' and self.pos[0] < self.win.root.winfo_screenwidth() - 80:
            self.win.canva.move(self.player_item, 30, 0)
            self.pos[0] += 30

    def stop_moving(self, event):
        # Add logic to stop continuous movement if needed
        pass

    def shoot(self, event=None):
        new_bullet = Bullet(self, 1)
        self.file_bullets_player.append(new_bullet)

    def update_bullets(self):
        for bullet in self.file_bullets_player:
            bullet.move()

        self.win.root.after(10, self.update_bullets)

    def afficher_projectiles(self):
        if len(self.file_bullets_player) > 0:
            for bullet in self.file_bullets_player:
                bullet.place()
