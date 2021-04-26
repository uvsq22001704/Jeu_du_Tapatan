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

########################
# import des librairies

import tkinter as tk
import copy as cp
import random as rd
from tkinter import font as tkFont

########################
# constantes

HEIGHT = 800
WIDTH = 1200
#helv26 = tkFont.Font(family='Comic Sans MS', size=16, weight='bold')
#fontStyle = tkFont.Font(family="Comic sans MS", size=20)
#fontStyle2 = tkFont.Font(family="Comic sans MS", size=10)


matrice = []   #~3) on créer une liste 2D dans laquelle se trouvent la couleur de chaque cases du plateau
for i in range (3):
    matrice.append([])

for j in range (3):
    for i in range (3):
        matrice[i].append(0)
print (matrice)

#0 gris
#1 rouge
#2 bleu


########################
# fonctions

def recharger():
    pass

def sauvegarder():
    pass

########################
# menu

menu = tk.Tk()
menu.title("Tapatan 97")

def P0j():
    menu.destroy()

def P1j(): 
    menu.destroy()

def P2j():
    menu.destroy()

bck = tk.Canvas(menu, bg = "red", height = 150, width = 400)
titre = tk.Label(menu, text="Jeu Du Tapatan Win97")
buttonII = tk.Button(menu, text="0 Joueurs", command = P0j)
buttonHH = tk.Button(menu, text="1 Joueur", command = P1j)
buttonHI = tk.Button(menu, text="2 Joueurs", command = P2j)

bck.grid(column = 0, row = 0, columnspan = 3,padx = 300)
titre.grid(column = 0, row = 0, columnspan = 3,padx = 300)
buttonII.grid(column = 0, row = 1, padx = 500, pady = 30)
buttonHH.grid(column = 0, row = 2, pady = 30, )
buttonHI.grid(column = 0, row = 3, pady = 30)


menu.mainloop()

########################
# plateau

plateau = tk.Tk()

canvas = tk.Canvas(plateau, height=HEIGHT, width=WIDTH)

bouton_sauvegarder = tk.Button(plateau, text='Sauvegarder la partie',
                               command=sauvegarder)
bouton_recharger = tk.Button(plateau, text='Recharger la partie', command=recharger)

#score = tk.Label(plateau, text=('SCORE : ',r,' - ',b))

#score.grid(row=0, columnspan=2)

r=0
b=0

#digit1 = tk.Label(plateau, text="0", width = 5, height = 5)
#digit2 = tk.Label(plateau, text="-", width = 30, height = 5)
#digit3 = tk.Label(plateau, text="0", width = 5, height = 5)
#digit1.grid(column = 0, row = 0)
#digit2.grid(column = 1, row = 0)
#digit3.grid(column = 2, row = 0)

bouton_sauvegarder.grid(row=3, column=0)
bouton_recharger.grid(row=3, column=1)
canvas.grid(row=0, columnspan=2)

rouge1 = canvas.create_oval((50, 500), (100, 550), fill="red", outline="red")
rouge2 = canvas.create_oval((50, 600), (100, 650), fill="red", outline="red")
rouge3 = canvas.create_oval((50, 700), (100, 750), fill="red", outline="red")

bleu1 = canvas.create_oval((1100, 500), (1150, 550), fill="blue", outline="blue")
bleu2 = canvas.create_oval((1100, 600), (1150, 650), fill="blue", outline="blue")
bleu3 = canvas.create_oval((1100, 700), (1150, 750), fill="blue", outline="blue")

canvas.create_line((350,100),(850,100),fill="black")
canvas.create_line((350,100),(350,600),fill="black")
canvas.create_line((350,600),(850,600),fill="black")
canvas.create_line((350,350),(850,350),fill="black")
canvas.create_line((350,100),(850,600),fill="black")
canvas.create_line((350,600),(850,100),fill="black")
canvas.create_line((600,100),(600,600),fill="black")
canvas.create_line((850,100),(850,600),fill="black")

cercle00 = canvas.create_oval((325,75),(375,125),fill="grey", outline="grey")
cercle01 = canvas.create_oval((325,325),(375,375),fill="grey", outline="grey")
cercle02 = canvas.create_oval((325,575),(375,625),fill="grey", outline="grey")
cercle10 = canvas.create_oval((575,75),(625,125),fill="grey", outline="grey")
cercle11 = canvas.create_oval((575,325),(625,375),fill="grey", outline="grey")
cercle12 = canvas.create_oval((575,575),(625,625),fill="grey", outline="grey")
cercle20 = canvas.create_oval((825,75),(875,125),fill="grey", outline="grey")
cercle21 = canvas.create_oval((825,325),(875,375),fill="grey", outline="grey")
cercle22 = canvas.create_oval((825,575),(875,625),fill="grey", outline="grey")



liCe = [[ cercle00, cercle01, cercle02], [ cercle10, cercle11, cercle12], [ cercle20, cercle21, cercle22]] 
# ^ liste comportant l'id de tous les cercles pour pouvoir les modifier plus facilement ^   

def mapla():
    '''~12) met à jour la couleur des pions sur le plateau'''
    for i in range (3):
        for j in range (3):
            if matrice [j][i] == 1 :
                canvas.itemconfig(liCe[i][j], fill = 'red')
            if matrice [j][i] == 2 :
                canvas.itemconfig(liCe[i][j], fill = 'blue')

matrice [1][2] = 1 #juste un pour tester la fonct mapla
mapla()



def dePion(event):
    x, y = event.x, event.y
    for i in range (3):
        for j in range (3):
            x1,y1,x2,y2 = canvas.coords(liCe[i][j])

            if x <= x2 and y <= y2 and x >= x1 and y >= y1:
                canvas.itemconfig(liCe[i][j], fill = 'blue')


canvas.bind("<Button-1>", dePion)



plateau.mainloop()

########################

