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

SCORE_H = 30
SCORE_W = 100
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
    
def regles():
    """fonction liée au bouton 'Règles du jeu'. Ouvre une fenêtre auxiliaire
    avec explication des règles. Quand on appuie sur le bouton 'Retour', la fenêtre
    se ferme et on revient au menu"""
    rules = tk.Toplevel(menu)
    rules.title("Règles du jeu")
    regles = tk.Canvas(rules, height=400, width=1000, bg='white')
    def close():
        rules.destroy()
    retour = tk.Button(rules, text='Retour', command=close)
    regles.create_text(500, 200, text="Chacun des deux joueurs "
                   "dispose de 3 jetons.\nUne fois tous les pions posés,\n"
                   "chaque joueur peut à son tour déplacer un pion d'une case\n horizontale,"
                   "verticale ou diagonale\nLe vainqueur est le premier joueur à\naligner"
                   " 3 de ses jetons sur le plateau.", font=('helvetica','14'))
    regles.create_text(540, 20, text='RÈGLES DU JEU DU TAPATAN', font=('helvetica','20'))
    regles.grid(row=0)
    retour.grid(row=1)

bck = tk.Canvas(menu, bg = "red", height = 150, width = 400)
titre = tk.Label(menu, text="Jeu Du Tapatan Win97")
buttonII = tk.Button(menu, text="0 Joueurs", command = P0j)
buttonHH = tk.Button(menu, text="1 Joueur", command = P1j)
buttonHI = tk.Button(menu, text="2 Joueurs", command = P2j)
button_rules = tk.Button(menu, text='Règles du jeu', command=regles)


bck.grid(column = 0, row = 0, columnspan = 3,padx = 300)
titre.grid(column = 0, row = 0, columnspan = 3,padx = 300)
buttonII.grid(column = 0, row = 1, padx = 500, pady = 30)
buttonHH.grid(column = 0, row = 2, pady = 30, )
buttonHI.grid(column = 0, row = 3, pady = 30)
button_rules.grid(column=0, row=4, pady=30)


menu.mainloop()

########################
# plateau

plateau = tk.Tk()

r=0
b=0

canvas = tk.Canvas(plateau, height=HEIGHT, width=WIDTH)

bouton_sauvegarder = tk.Button(plateau, text='Sauvegarder la partie',
                               command=sauvegarder)
bouton_recharger = tk.Button(plateau, text='Recharger la partie', command=recharger)

score = tk.Canvas(plateau, height=60, width=300, bg='dark khaki')

score.create_text(SCORE_W, SCORE_H, text='SCORE : ', font=('helvetica', '16'))
score_rouge = score.create_text(SCORE_W+80, SCORE_H, text=r, font=('helvetica', '16'))
score.create_text(SCORE_W+100, SCORE_H, text='-', font=('helvetica', '16'))
score_bleu = score.create_text(SCORE_W+120, SCORE_H, text=b, font=('helvetica', '16'))


#digit1 = tk.Label(plateau, text="0", width = 5, height = 5)
#digit2 = tk.Label(plateau, text="-", width = 30, height = 5)
#digit3 = tk.Label(plateau, text="0", width = 5, height = 5)
#digit1.grid(column = 0, row = 0)
#digit2.grid(column = 1, row = 0)
#digit3.grid(column = 2, row = 0)

bouton_sauvegarder.grid(row=3, column=0)
bouton_recharger.grid(row=3, column=1)
canvas.grid(row=1, columnspan=2)
score.grid(row=0, columnspan=2)

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
    '''place un pion sur le cercle gris cliqué'''
    x, y = event.x, event.y
    for i in range (3):
        for j in range (3):
            x1,y1,x2,y2 = canvas.coords(liCe[i][j])

            if x <= x2 and y <= y2 and x >= x1 and y >= y1:
                canvas.itemconfig(liCe[i][j], fill = 'blue')
                matrice[i][j] = 2 #j'ai rajouté ça là pour l'instant (NK)
    won_ckeck(matrice) #je l'ai associé ici, à voir (NK)
    
def won_ckeck(matrice):
    '''évalue après chaque tour si qqn a gagné. s'il y a un gagnant, un msg 
    s'affiche dans une nouvelle fenêtre. Lance une nouvelle partie'''
    global r, b
    for i in range(3):
        if matrice[i][0] == matrice[i][1] == matrice[i][2] == 1:
            print( "Joueur 1 a gagné!!!!!!")
            r += 1
            fin_de_partie()
        elif matrice[i][0] == matrice[i][1] == matrice[i][2] == 2:
            msg_gagne()
            b += 1
            score.itemconfigure(score_bleu, text=b)
            fin_de_partie()
    for j in range(3):
        if  matrice[0][j] == matrice[1][j] == matrice[2][j] == 1:
            print( "Joueur 1 a gagné!!!!!!")
            r += 1
            fin_de_partie()
        elif matrice[0][j] == matrice[1][j] == matrice[2][j] == 2:
            msg_gagne() 
            b += 1
            score.itemconfigure(score_bleu, text=b)
            fin_de_partie()
    if matrice[0][0] ==  matrice[1][1] == matrice[2][2]:
        if matrice[0][0] == 1:
            print( "Joueur 1 a gagné!!!!!!")
            r += 1
            fin_de_partie()
        elif matrice[0][0] == 2:
            msg_gagne()
            b += 1
            score.itemconfigure(score_bleu, text=b)
            fin_de_partie()
    if matrice[2][0] ==  matrice[1][1] == matrice[0][2]:
        if matrice[i][j] == 1:
            print( "Joueur 1 a gagné!!!!!!")
            r += 1
            fin_de_partie()
        elif matrice[2][0] == 2:
            msg_gagne()
            b += 1
            score.itemconfigure(score_bleu, text=b)
            fin_de_partie()


def msg_gagne():
    """"fenetre auxiliaire qui affiche message 'Gagné' par dessus le plateau"""
    msg = tk.Toplevel(plateau)
    msg.title("Fin de partie")
    gagné = tk.Canvas(msg, height=100, width=400, bg='dark khaki')
    gagné.create_text(130, 60, text='Joueur', font=('helvetica', '16'))
    gagné.create_text(190, 60, text='2', font=('helvetica', '16'))
    gagné.create_text(280, 60, text='a gagné !', font=('helvetica', '16'))
    gagné.grid()
    #msg.after(3000, msg.destroy()) # ça marche pas????


def fin_de_partie():
    """relance une partie tant qu'il n'y a pas de vainqueur"""
    #global r, b
    #while r < 4 or b < 4:
    pass


canvas.bind("<Button-1>", dePion)



plateau.mainloop()

########################

