from tkinter import *
from PIL import Image,ImageTk
from player import Player
from game_update import Game_update

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
        self.game_over = False
        self.player = Player(self)
        updt = Game_update(self, self.player)
        self.button.pack(anchor='ne')


        self.root.bind("<Key>", self.player.move)
        self.root.bind("<KeyRelease>", self.player.stop_moving)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
    
    def display_game_over(self):

        self.game_over_canvas = Canvas(self.root, width=self.w, height=self.h, background='black', borderwidth=0, highlightthickness=0)
        self.game_over_canvas.place(relx=0, rely=0)


        # Create a game over label
        game_over_label = Label(
            self.game_over_canvas, text="Game Over", font=("Helvetica", 24), fg="red"
        )
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")

        # Create restart button
        restart_button = Button(self.game_over_canvas, text="Restart", command=self.restart_game)
        restart_button.place(relx=0.4, rely=0.6, anchor="center")


        # Create quit button
        quit_button = Button(self.game_over_canvas, text="Quit", command=self.quit_game)
        quit_button.place(relx=0.6, rely=0.6, anchor="center")

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
        self.root.bind("<KeyRelease>", self.player.stop_moving)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        updt = Game_update(self, self.player)

        # Add additional reset logic if needed


    def quit_game(self):
            # Quit the game
            self.root.destroy()

        
