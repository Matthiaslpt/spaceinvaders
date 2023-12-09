from tkinter import *
from PIL import Image, ImageTk
from bullet import Bullet
import time

class Player:
    def __init__(self, win):
        self.win = win
        self.health = 3
        self.score = 0  # Add a score variable
        self.pos = [self.win.w / 2, self.win.h - 100]
        self.image = Image.open('image/player.png')
        self.image = self.image.resize((150, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.player_item = self.win.canva.create_image(self.pos[0], self.pos[1], image=self.image)
        self.file_bullets = []
        self.nb_tirs = 0
        self.win.root.bind("<space>", self.shoot)
        self.cooldown_time = 0.6
        self.last_shot_time = 0.0

        # Add labels for life counter and score display
        self.life_label = Label(self.win.root, text=f"Vies: {self.health}", font=("Helvetica", 16), fg="white", bg="black")
        self.life_label.place(relx=0.05, rely=0.05, anchor="w")

        self.score_label = Label(self.win.root, text=f"Score: {self.score}", font=("Helvetica", 16), fg="white", bg="black")
        self.score_label.place(relx=0.95, rely=0.05, anchor="e")

        self.update_labels()  # Start updating labels in the game loop

        win.root.bind("<KeyRelease>", self.stop)
        win.root.bind("<space>", self.shoot)
        self.update_bullets()

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
            self.win.root.after(50, self.update_bullets)


    def update_labels(self):
        # Update the life counter and score display
        self.life_label.config(text=f"Vies: {self.health}")
        self.score_label.config(text=f"Score: {self.score}")

        # Check game over condition and update labels in the game loop
        if not self.win.game_over:
            self.win.root.after(100, self.update_labels)


    def update_obstacle_collision(self):
        if self.file_bullets:
            for bullet in self.file_bullets:
                bullet_coords = self.win.canva.coords(bullet.bullet_item)
                bullet_bbox = self.calculate_bbox(bullet_coords, 70, 70)

                for ilot in self.win.ilots_list:
                    ilot_coords = self.win.canva.coords(ilot.ilots_item)
                    if self.check_collision(bullet_bbox, ilot_coords):
                        ilot.damage()
                        self.win.canva.delete(bullet.bullet_item)
                        self.file_bullets.remove(bullet)