from tkinter import *
from enemy import Enemy

class Game_update:
    def __init__(self,win, player):
        self.win = win
        self.player = player
        self.enemy_liste = []
        self.file_bullets_aliens = []
        self.enemy_rounds()
        self.check_collisions()


    def enemy_rounds(self):
        if len(self.enemy_liste) < 6:
            self.enemy_liste.append(Enemy(self.win))
            self.win.root.after(5000, self.enemy_rounds)


    def check_collisions(self):
        for bullet in self.player.file_bullets_player:
            bullet_coords = self.win.canva.coords(bullet.bullet_item)
            bullet_width, bullet_height = 70, 70
            for enemy in self.enemy_liste:
                enemy_coords = self.win.canva.coords(enemy.enemy_item)
                enemy_width, enemy_height = 200, 150
                # Calculate the full bounding box for bullets and enemies
                bullet_bbox = (
                    bullet_coords[0], bullet_coords[1],
                    bullet_coords[0] + bullet_width, bullet_coords[1] + bullet_height
                )

                enemy_bbox = (
                    enemy_coords[0], enemy_coords[1],
                    enemy_coords[0] + enemy_width, enemy_coords[1] + enemy_height
                )

                # Check for collision using the full bounding boxes
                if (
                    bullet_bbox[0] < enemy_bbox[2] and
                    bullet_bbox[2] > enemy_bbox[0] and
                    bullet_bbox[1] < enemy_bbox[3] and
                    bullet_bbox[3] > enemy_bbox[1]
                ):
                    # Handle the collision here (e.g., remove bullet and enemy)
                    self.win.canva.delete(bullet.bullet_item)
                    self.win.canva.delete(enemy.enemy_item)
                    self.player.file_bullets_player.remove(bullet)
                    self.enemy_liste.remove(enemy)

        # Call the check_collisions method recursively after a delay (e.g., 10 milliseconds)
        self.win.root.after(10, self.check_collisions)
            




            