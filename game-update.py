from tkinter import *
from enemy import enemy

class Game_update:
    def __init__(self,win):
        self.win = win
        self.enemy_liste = []

        self.enemy_rounds()

    def enemy_rounds(self):
        if self.enemy_amount < 6:
            self.enemy_liste.append(enemy(self.win))

    def render_enemy(self):
        for enemy in self.enemy_liste:
            enemy.place()
        
        




        