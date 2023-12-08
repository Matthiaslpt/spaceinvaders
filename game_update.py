from tkinter import *
from enemy import Enemy
import random as r

class Game_update:
    def __init__(self, win, player):
        self.win = win
        self.player = player
        self.enemy_rounds()
        self.check_collisions()

    def enemy_rounds(self):
        if len(self.win.enemy_liste) < 6 and not self.win.game_over:
            row, column = len(self.win.enemy_liste) // 6, len(self.win.enemy_liste) % 6
            self.win.enemy_liste.append(Enemy(self.win, row, column))
            self.win.root.after(r.randint(4000,7000), self.enemy_rounds)

    def check_collisions(self):
        if self.player.file_bullets != []:
            for bullet in self.player.file_bullets:
                bullet_coords = self.win.canva.coords(bullet.bullet_item)
                bullet_bbox = self.calculate_bbox(bullet_coords, 70, 70)

                overlapping_items = self.win.canva.find_overlapping(*bullet_bbox)

                overlapping_items = [item for item in overlapping_items if item not in [bullet.bullet_item, 1]]

                for enemy in self.win.enemy_liste:
                    if enemy.enemy_item in overlapping_items:
                        self.win.canva.delete(bullet.bullet_item)
                        self.win.canva.delete(enemy.enemy_item)
                        self.player.file_bullets.remove(bullet)
                        self.win.enemy_liste.remove(enemy)
                        enemy.shooting = False
                        self.player.score += 10  # Increase score on hitting an enemy
    
        if self.win.file_bullets != []:
            for bullet in self.win.file_bullets:
                bullet_coords = self.win.canva.coords(bullet.bullet_item)
                bullet_bbox = self.calculate_bbox(bullet_coords, 70, 70)

                overlapping_items = self.win.canva.find_overlapping(*bullet_bbox)

                overlapping_items = [item for item in overlapping_items if item not in [bullet.bullet_item, 1]]

                if self.player.player_item in overlapping_items:
                    self.win.canva.delete(bullet.bullet_item)
                    self.player.health -= 1
                    self.win.file_bullets.remove(bullet)
                    if self.player.health == 0:
                        self.win.game_over = True
                        self.win.display_game_over()

        if not self.win.game_over:
            self.win.root.after(10, self.check_collisions)

    def calculate_bbox(self, coords, width, height):
        x1, y1 = coords[0], coords[1]
        x2, y2 = x1 + width, y1 + height
        return x1, y1, x2, y2