from tkinter import *
from PIL import Image, ImageTk
from bullet import Bullet



class Enemy:
    def __init__(self, win, row, column):
        self.win = win
        self.win.w, self.win.h = win.root.winfo_screenwidth(), win.root.winfo_screenheight()
        self.row = row
        self.column = column
        self.pos = [50 + 100 * self.column, 60 + 80 * self.row]
        self.direction = 1
        self.speed = 4
        self.image = Image.open('image/alien.png')
        self.image = self.image.resize((200, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.enemy_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.shooting = True
        self.move()
        self.shoot()

    def move(self):
        if not self.win.game_over:
            self.pos[0] += self.speed * self.direction
            self.win.canva.move(self.enemy_item, self.speed * self.direction, 0)

            if self.pos[0] <= 50 or self.pos[0] >= self.win.w - 50:
                self.direction *= -1  # Reverse direction when reaching the screen edges
                self.pos[1] += 100  # Move down one row
                self.win.canva.move(self.enemy_item, 0, 100)

            self.win.root.after(10, self.move)

            if self.pos[1] > 950:
                self.health = 0
                self.win.game_over = True
                self.win.display_game_over()

    def shoot(self):
        if self.shooting and not self.win.game_over:
            new_bullet = Bullet(self, -1, self.win)
            self.win.file_bullets.append(new_bullet)
            self.win.root.after(6000, self.shoot)