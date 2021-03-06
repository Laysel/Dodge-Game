from tkinter import *
from tkinter import ttk
import tkinter as tk
import dodge_game

class Home(Frame):
    
    def __init__(self, master = None):
        
        Frame.__init__(self, master)
        self.master = master
        self.screen()
        self.buttons()

    def screen(self):
        
        self.master.title("Dodge")
        self.pack(fill = BOTH, expand = YES)

        self.playImage = PhotoImage(file = "menu_images/play.gif")
        self.helpImage = PhotoImage(file = "menu_images/help.gif")
        self.quitImage = PhotoImage(file = "menu_images/quit.gif")
        self.backImage = PhotoImage(file = "menu_images/back.gif")
        self.helpbgImage = PhotoImage(file = "menu_images/helpbg.gif")
        
        self.pack(fill = BOTH, expand = YES)
        
        background = PhotoImage(file = "menu_images/bg.gif")
        self.bgImage = Label(self, image = background)
        self.bgImage.image = background
        self.bgImage.place(x = -2, y = -2)
        
    def buttons(self):

        self.playButton = Button(self.bgImage, bd = 0, bg = "black", image = self.playImage, command = self.play)
        self.playButton.configure(image = self.playImage)
        self.playButton.place(x = 450, y = 250)

        self.helpButton = Button(self.bgImage, bd = 0, bg = "black", image = self.helpImage, command = self.help)
        self.helpButton.configure(image = self.helpImage)
        self.helpButton.place(x = 450, y = 350)
        
        self.quitButton = Button(self.bgImage, bd = 0, bg = "black", image = self.quitImage, command = root.destroy)
        self.quitButton.configure(image = self.quitImage)
        self.quitButton.place(x = 450, y = 450)

    def play(self):
        
        dodge_game.main()
        self.master.withdraw()

    def help_bg(self, panel):

        self.screen()
        self.bgImage.configure(image = self.helpbgImage)

        img = PhotoImage(file = "menu_images/"+panel+".gif")
        panel = Label(self, image = img)
        panel.image = img
        panel.place(x = 0, y = 0)

        self.back_btn = Button(self, bd = 0, bg = "black", image = self.backImage, command = self.menu)
        self.back_btn.configure(image = self.backImage)
        self.back_btn.place(x = 450, y = 60)

    def help(self):

        self.help_bg("helpbg")

    def menu(self):

        self.screen()
        self.buttons()


root = Tk()
root.geometry("800x600")
root.resizable(0,0)

app = Home(root)

root.mainloop()
