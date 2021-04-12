########################
# Groupe 2 LDDMP
# Arthur CHAUVEAU
# Noémie KAUFMANN
# Titouan BIGET
# Diary ANDRIANARIVO
# Mohamed IBOUROI
# Hyacinthe MORASSE
# https://github.com/uvsq22001704/Jeu_du_Tapatan
########################


#import des librairies
#####################
import tkinter as tk
import copy as cp
import random as rd


import tkinter.font as tkF
menu = tk.Tk()
menu.title("Tapatan 97")
bb = tk.Canvas(menu, bg = "red", height = 150, width = 400)

fontStyle = tkF.Font(family="Comic sans MS", size=20)
fontStyle2 = tkF.Font(family="Comic sans MS", size=10)

titre = tk.Label(menu, text="Jeu Du Tapatan Win97", font = fontStyle)
buttonII = tk.Button(menu, text="0 Joueurs", font = fontStyle2)
buttonHH = tk.Button(menu, text="1 Joueur", font = fontStyle2)
buttonHI = tk.Button(menu, text="2 Joueurs", font = fontStyle2)

bb.grid(column = 0, row = 0, columnspan = 3,padx = 300)
titre.grid(column = 0, row = 0, columnspan = 3,padx = 300)
buttonII.grid(column = 0, row = 1, padx = 500, pady = 30)
buttonHH.grid(column = 0, row = 2, pady = 30, )
buttonHI.grid(column = 0, row = 3, pady = 30)


menu.mainloop()
