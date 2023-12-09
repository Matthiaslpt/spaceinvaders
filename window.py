from tkinter import *
from PIL import Image,ImageTk
from player import Player
from game_update import Game_update
from ilots import Ilots

class Window:
    def __init__(self):
        self.root = Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canva = Canvas(self.root, width=self.w, height=self.h, background='black',borderwidth=0, highlightthickness=0)
        self.image = Image.open('image/bckgrnd.png')
        self.image = self.image.resize((self.w*2, self.h*2))
        self.image = ImageTk.PhotoImage(self.image)
        self.bckgrnd = self.canva.create_image(0 ,0 ,image= self.image)
        self.root.geometry("%dx%d" % (self.w,self.h))
        self.root.title('Space Invaders')
        self.root.attributes('-fullscreen', True)
        self.root['bg'] = 'black'
        self.button= Button(self.root,text='Tchao', command=self.root.destroy)
        self.file_bullets = []
        self.enemy_liste = []
        self.ilots_list = []
        self.game_over = False
        self.player = Player(self)
        updt = Game_update(self, self.player)
        self.button.pack(anchor='ne')
        self.root.bind("<Key>", self.player.move)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
    
    def display_game_over(self):

        game_over_width = int(self.w * 1/4)
        game_over_height = int(self.h * 1/4)

        # Calculate the coordinates to place the canvas at the center
        x = (self.w - game_over_width) // 2
        y = (self.h - game_over_height) // 2

        # Create a canvas for game over elements
        self.game_over_canvas = Canvas(self.root, width=game_over_width, height=game_over_height, background='black', borderwidth=0, highlightthickness=0)
        self.game_over_canvas.place(x=x, y=y)


            # Create a game over label
        game_over_label = Label(
            self.game_over_canvas, text="Game Over", font=("Helvetica", 24), fg="red", background='black'
        )
        game_over_label.place(relx=0.5, rely=0.3, anchor="center")

        # Display final score
        final_score_label = Label(
            self.game_over_canvas, text=f"Score final: {self.player.score}", font=("Helvetica", 16), fg="white", background='black'
        )
        final_score_label.place(relx=0.5, rely=0.4, anchor="center")

        # Display player's rank (based on the score)
        rank_label = Label(
            self.game_over_canvas, text=f"Rang: {self.get_player_rank()}", font=("Helvetica", 16), fg="white", background='black'
        )
        rank_label.place(relx=0.5, rely=0.5, anchor="center")

        # Create restart button
        restart_button = Button(self.game_over_canvas, text="Rejouer", command=self.restart_game)
        restart_button.place(relx=0.4, rely=0.7, anchor="center")

        # Create quit button
        quit_button = Button(self.game_over_canvas, text="Quitter", command=self.quit_game)
        quit_button.place(relx=0.6, rely=0.7, anchor="center")

    def restart_game(self):
        # Reset game state and restat
        self.game_over_canvas.destroy()
        self.canva.destroy()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canva = Canvas(self.root, width=self.w, height=self.h, background='black',borderwidth=0, highlightthickness=0)
        self.image = Image.open('image/bckgrnd.png')
        self.image = self.image.resize((self.w*2, self.h*2))
        self.image = ImageTk.PhotoImage(self.image)
        self.bckgrnd = self.canva.create_image(0 ,0 ,image= self.image)
        self.root.geometry("%dx%d" % (self.w,self.h))
        self.root.title('Space Invaders')
        self.root.attributes('-fullscreen', True)
        self.root['bg'] = 'black'
        self.button= Button(self.root,text='Tchao', command=self.root.destroy)
        self.file_bullets = []
        for enemy in self.enemy_liste:
            enemy.shooting = False
        self.enemy_liste = []
        self.game_over = False
        self.player = Player(self)
        self.canva.pack()
        self.root.bind("<Key>", self.player.move)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        updt = Game_update(self, self.player)

        # Add additional reset logic if needed

    def get_player_rank(self):
        # Implement a simple rank calculation based on the final score
        if self.player.score >= 100:
            return "Space Ace"
        elif self.player.score >= 50:
            return "Galactic Warrior"
        else:
            return "Star Cadet"


    def quit_game(self):
            # Quit the game
            self.root.destroy()

        
