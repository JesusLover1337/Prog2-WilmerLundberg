from tkinter import *
import random
root = Tk()
b_sten = Button(root, text ="Sten")
b_sax = Button(root, text ="Sax")
b_pase = Button(root, text ="Påse")
player_score = 0 
bot_score = 0
def click_handler(self: Event):
    #game blet
    x=["Sten","Sax","Påse"]
    rng = random.randint(0,2)
    bot=x[rng]
    player = self.widget["text"]
    if bot == player:
        lbl["text"] = "Draw"
    elif player == "Sten" and bot == "Sax":
        lbl["text"] = "You win" 
    elif player == "Sax" and bot == "Sten":
        lbl["text"] = "You lose" 
    elif player == "Påse" and bot == "Sten":
        lbl["text"] = "You win" 
    elif player == "Sten" and bot == "Påse":
        lbl["text"] = "You lose" 
    elif player == "Påse" and bot == "Sax":
        lbl["text"] = "You lose" 
    elif player == "Sax" and bot == "Påse":
        lbl["text"] = "You win" 

b_sten.bind("<Button-1>", click_handler)
b_sax.bind("<Button-1>", click_handler)
b_pase.bind("<Button-1>", click_handler)


b_sten.pack()
b_sax.pack()
b_pase.pack()
lbl = Label(root)
lbl.pack()
root.mainloop()
