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

########################
# constantes

HEIGHT = 800
WIDTH = 1200

SCORE_H = 30
SCORE_W = 100


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

tour = 0 #incrémentée à chaques tours, si pair alors tour du bleu sinon tour rouge 

nb_pions_r = 3
nb_pions_b = 3

r=0 #compteur du score rouge
b=0 #compteur du score bleu

position_prece = [1,1] #sert à connaitre la position du pion que l'on s'apprete à déplacer

fantome_de_tes_matrices_passées = [] #index chaques matrices de la manche dans l'éventualité d'un match nul

nb_ia = 0
########################
# fonctions

def recharger(): 
    """charger la grille depuis le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt", "r")
    fond.delete(cercle00,cercle01,cercle02,cercle10,cercle11,cercle12,cercle20,cercle21,cercle22)
    j = 0
    for ligne in fic:
        i = 0
        val = ligne.split()
        for e in val:
            if e == "0 ":
                x = i * 250 + 325
                y = j * 250 + 75
                cercle = fond.create_oval((x, y), (x + 50, y + 50), fill="grey")
         
            elif e =="1 " :
                x = i * 250 + 325
                y = j * 250 + 75
                cercle = fond.create_oval((x, y), (x + 50, y + 50), fill="red")
            elif e == "2 " :
                 x = i * 250 + 325
                 y = j * 250 + 75
                 cercle = fond.create_oval((x, y), (x + 50, y + 50), fill="blue")
            i += 1
        j += 1
    fic.close()  


def sauvegarder():
     """sauvegarder la grille vers le fichier sauvegarde.txt"""
     fic = open("sauvegarde.txt", "w")
     for j in range(3):
        for i in range(3):
            if matrice[i][j] == 0:
                (open("sauvegarde.txt", "w")).write("0 ")
            elif matrice[i][j] == 1:
                (open("sauvegarde.txt", "w")).write("1 ")
            elif matrice[i][j] == 2:
                (open("sauvegarde.txt", "w")).write("2 ")
        (open("sauvegarde.txt", "w")).write("\n")
     (open("sauvegarde.txt", "w")).close()


########################
# menu

menu = tk.Tk()
menu.title("Tapatan 97")

def couleur (r, g, b):  
    '''pour que ce soit plus zoli'''
    return '#{:02x}{:02x}{:02x}'.format (r, g, b)




def P0j():
    global nb_ia
    nb_ia = 2
    menu.destroy()

def P1j():
    global nb_ia 
    nb_ia = 1
    menu.destroy()

def P2j():
    global nb_ia
    nb_ia = 0
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
                   " 3 de ses jetons sur le plateau.", font=('comic sans ms','14'))
    regles.create_text(540, 20, text='RÈGLES DU JEU DU TAPATAN', font=('comic sans ms','20'))
    regles.grid(row=0)
    retour.grid(row=1)

fond = tk.Canvas(menu, height = 700, width = 1100)
bck = tk.Canvas(menu, bg = "RoyalBlue1", height = 150, width = 400)
titre = tk.Label(menu, text="Jeu Du Tapatan Win97", font=('comic sans ms', '21'), bg = "RoyalBlue1")
buttonII = tk.Button(menu, text="0 Joueur", command = P0j, font=('comic sans ms', '15'), bg = "coral1")
buttonHH = tk.Button(menu, text="1 Joueur", command = P1j, font=('comic sans ms', '15'), bg = "coral1")
buttonHI = tk.Button(menu, text="2 Joueurs", command = P2j, font=('comic sans ms', '15'), bg = "coral1")
button_rules = tk.Button(menu, text='Règles du jeu', command=regles, font=('comic sans ms', '15'), bg = "coral1")

fond.grid(row = 0, column = 0, columnspan = 3, rowspan = 5)
bck.grid(column = 0, row = 0, columnspan = 3,padx = 300)
titre.grid(column = 0, row = 0, columnspan = 3,padx = 300)
buttonII.grid(column = 0, row = 1, padx = 500, pady = 30)
buttonHH.grid(column = 0, row = 2, pady = 30, )
buttonHI.grid(column = 0, row = 3, pady = 30)
button_rules.grid(column=0, row=4, pady=30)


red, green, blue = rd.randint(5,250), rd.randint(5,250), rd.randint(5,250)
fr, fg, fb = rd.randint(-5, 5), rd.randint(-5, 5), rd.randint(-5, 5)
for i in range (175):
    red, green, blue = (red + fr) % 250, (green + fg) % 250 , (blue + fb) % 250
    fond.create_line(0, i * 4, 1100, i * 4 , fill = couleur (red, green, blue))




menu.mainloop()

########################
# plateau

plateau = tk.Tk()

canvas = tk.Canvas(plateau, height=HEIGHT, width=WIDTH)

bouton_sauvegarder = tk.Button(plateau, text='Sauvegarder la partie',
                               command=sauvegarder, font = ('comic sans ms', '9'))
bouton_recharger = tk.Button(plateau, text='Recharger la partie', command=recharger, font = ('comic sans ms', '9'))

score = tk.Canvas(plateau, height=60, width=300, bg='dark khaki')

score.create_text(SCORE_W, SCORE_H, text='SCORE : ', font=('comic sans ms', '16'))
score_rouge = score.create_text(SCORE_W+80, SCORE_H, text=r, font=('comic sans ms', '16'))
score.create_text(SCORE_W+100, SCORE_H, text='-', font=('comic sans ms', '16'))
score_bleu = score.create_text(SCORE_W+120, SCORE_H, text=b, font=('comic sans ms', '16'))

indictour = tk.Canvas(plateau, height=60, width=300, bg='light blue') #canvas dans lequel s'affiche à qui est le tour
tour_texte = indictour.create_text(SCORE_W, SCORE_H, text="tour de bleu", font=('comic sans ms', '16', ), fill = 'blue')

bouton_sauvegarder.grid(row=3, column=0)
bouton_recharger.grid(row=3, column=1)
canvas.grid(row=1, columnspan=2)
score.grid(row=0, columnspan=2)
indictour.grid(row = 2, columnspan=2)

rouge1 = canvas.create_oval((50, 500), (100, 550), fill = "red", outline = "red")
rouge2 = canvas.create_oval((50, 600), (100, 650), fill = "red", outline = "red")
rouge3 = canvas.create_oval((50, 700), (100, 750), fill = "red", outline = "red")

bleu1 = canvas.create_oval((1100, 500), (1150, 550), fill = "blue", outline = "blue")
bleu2 = canvas.create_oval((1100, 600), (1150, 650), fill = "blue", outline = "blue")
bleu3 = canvas.create_oval((1100, 700), (1150, 750), fill = "blue", outline = "blue")

canvas.create_line((350, 100), (850, 100), fill = "black")
canvas.create_line((350, 100), (350, 600), fill = "black")
canvas.create_line((350, 600), (850, 600), fill = "black")
canvas.create_line((350, 350), (850, 350), fill = "black")
canvas.create_line((350, 100), (850, 600), fill = "black")
canvas.create_line((350, 600), (850, 100), fill = "black")
canvas.create_line((600, 100), (600, 600), fill = "black")
canvas.create_line((850, 100), (850, 600), fill = "black")

cercle00 = canvas.create_oval((325, 75), (375, 125), fill = "grey", outline = "grey")
cercle01 = canvas.create_oval((325, 325), (375, 375), fill = "grey", outline = "grey")
cercle02 = canvas.create_oval((325, 575), (375, 625), fill = "grey", outline = "grey")
cercle10 = canvas.create_oval((575, 75), (625, 125), fill = "grey", outline = "grey")
cercle11 = canvas.create_oval((575, 325), (625, 375), fill = "grey", outline = "grey")
cercle12 = canvas.create_oval((575, 575), (625, 625), fill = "grey", outline = "grey")
cercle20 = canvas.create_oval((825, 75), (875, 125), fill = "grey", outline = "grey")
cercle21 = canvas.create_oval((825, 325), (875, 375), fill = "grey", outline = "grey")
cercle22 = canvas.create_oval((825, 575), (875, 625), fill = "grey", outline = "grey")



liCe = [[ cercle00, cercle01, cercle02], [ cercle10, cercle11, cercle12], [ cercle20, cercle21, cercle22]] 
# ^ liste comportant l'id de tous les cercles pour pouvoir les modifier plus facilement ^   

def matcheur_nul():
    global fantome_de_tes_matrices_passées
    '''ajoute dans fantome_de_tes_matrices_passées la derniere matrice en date et verifie si il existe trois matrices identiques, 
    si c'est le cas alors termine la manche en cours sans attribuer de points'''
    fantome_de_tes_matrices_passées.append(cp.deepcopy(matrice))
    for i in range (len(fantome_de_tes_matrices_passées)):
        for j in range (len (fantome_de_tes_matrices_passées)):
            for k in range (len (fantome_de_tes_matrices_passées)):
                if fantome_de_tes_matrices_passées [i] == fantome_de_tes_matrices_passées [j] and fantome_de_tes_matrices_passées [i] == fantome_de_tes_matrices_passées [k] and i != j and i != k and k != j:
                    print ("match nul")
                    msg = tk.Toplevel(plateau)
                    msg.title("Fin de partie")
                    nul = tk.Canvas(msg, height=100, width=300, bg='RoyalBlue1')
                    nul.create_text(130, 60, text='Match Nul', font=('comic sans ms', '16'))
                    nul.grid()
                    fantome_de_tes_matrices_passées = []
                    return 
                
                    
def mapla():
    '''~12) met à jour la couleur des pions sur le plateau'''
    for i in range (3):
        for j in range (3):
            if matrice [i][j] == 1 :
                canvas.itemconfig(liCe[i][j], fill = 'red', outline = "red")
            if matrice [i][j] == 2 :
                canvas.itemconfig(liCe[i][j], fill = 'blue', outline = "blue")
            if matrice [i][j] == 0 :
                canvas.itemconfig(liCe[i][j], fill = 'grey', outline = "grey")


def affiche_tour():
    '''met à jour le compteur de tour'''
    if tour % 2 != 0:
        indictour.itemconfig(tour_texte, fill = 'red')
        indictour.itemconfig(tour_texte, text = 'tour de rouge')
    elif tour % 2 == 0:
        indictour.itemconfig(tour_texte, fill = 'blue')
        indictour.itemconfig(tour_texte, text = 'tour de bleu')


def IA():
    '''jsp comment tu comptes exactement faire Hyacinte dcp je sais pas quoi faire'''
    print ("iam an ai")


def Place_Pion(event):
    '''place ou déplace un pion sur le cercle gris cliqué'''
    global tour, nb_pions_b, nb_pions_r
    x, y = event.x, event.y
    for i in range (3):
        for j in range (3):
            x1,y1,x2,y2 = canvas.coords(liCe[i][j]) 

            if nb_pions_b > 0 or nb_pions_r > 0: # permet de placer un pion si il en reste en stock
               #si: coord cliquées sont dans coord du cercle     & tour de bleu    & si case vide         & si la nouvelle position du pion est dans un rayon de 1 de la précédente position
                if x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 == 0 and matrice[i][j] == 0 and i - position_prece[0] <= 1 and i - position_prece[0] >= -1 and j - position_prece[1] <= 1 and j - position_prece[1] >= -1 and nb_ia < 2:
                    canvas.itemconfig(liCe[i][j], fill = 'blue', outline = "blue")
                    tour += 1 
                    nb_pions_b -= 1
                    if nb_pions_b == 2:
                        canvas.itemconfigure(bleu1, fill = "grey", outline="grey")
                    elif nb_pions_b == 1:
                        canvas.itemconfigure(bleu2, fill = "grey", outline="grey")
                    elif nb_pions_b == 0:
                        canvas.itemconfigure(bleu3, fill = "grey", outline="grey")
                    matrice[i][j] = 2 #j'ai rajouté ça là pour l'instant (NK)
                    affiche_tour()
                    mapla()
                    matcheur_nul()
                    position_prece[0], position_prece[1] = 1,1
                    if nb_ia == 1: # ajoute un delay avant d'executer l'ia si partie à 1 joueur
                        canvas.after(1, canvas.after(1500, IA))#affiche un msg d'erreur mais fonctionne?

                elif x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 != 0 and matrice[i][j] == 0 and i - position_prece[0] <= 1 and i - position_prece[0] >= -1 and j - position_prece[1] <= 1 and j - position_prece[1] >= -1 and nb_ia == 0:
                    canvas.itemconfig(liCe[i][j], fill = 'red', outline = "red")
                    tour += 1
                    nb_pions_r -= 1
                    if nb_pions_r == 2:
                        canvas.itemconfigure(rouge1, fill = "grey", outline="grey")
                    elif nb_pions_r == 1:
                        canvas.itemconfigure(rouge2, fill = "grey", outline="grey")
                    elif nb_pions_r == 0:
                        canvas.itemconfigure(rouge3, fill = "grey", outline="grey")
                    matrice[i][j] = 1 #j'ai rajouté ça là pour l'instant (NK)
                    affiche_tour()
                    mapla()
                    matcheur_nul()
                    position_prece[0], position_prece[1] = 1,1  
            else: #récuperre un pion placé et le remet en stock, tant que le pion n'est pas placé il est affiché dans une couleur différente
                if x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 == 0 and matrice[i][j] == 2:
                    canvas.itemconfig(liCe[i][j], fill = 'RoyalBlue1', outline = 'RoyalBlue1')
                    matrice[i][j] = 0
                    nb_pions_b += 1
                    position_prece[0], position_prece[1] = i,j
                elif x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 != 0 and matrice[i][j] == 1:
                    canvas.itemconfig(liCe[i][j], fill = 'coral1', outline = 'coral1')
                    matrice[i][j] = 0
                    nb_pions_r += 1
                    position_prece[0], position_prece[1] = i,j
                
    print (tour)
    print (position_prece)
                
    win_ckeck(matrice) #je l'ai associé ici, à voir (NK)
    

def win_ckeck(matrice):
    '''évalue après chaque tour si qqn a gagné. s'il y a un gagnant, un msg 
    s'affiche dans une nouvelle fenêtre. Lance une nouvelle partie'''
    global r, b, player
    player = ''
    for i in range(3):
        if matrice[i][0] == matrice[i][1] == matrice[i][2] == 1 or matrice[0][i] == matrice[1][i] == matrice[2][i] == 1:
            player = '1'
            msg_gagne()
            r += 1
            score.itemconfigure(score_rouge, text=r)
            fin_de_partie()
        elif matrice[i][0] == matrice[i][1] == matrice[i][2] == 2 or matrice[0][i] == matrice[1][i] == matrice[2][i] ==2:
            player = '2'
            msg_gagne()
            b += 1
            score.itemconfigure(score_bleu, text=b)
            fin_de_partie()
    if matrice[0][0] ==  matrice[1][1] == matrice[2][2] == 1 or matrice[2][0] ==  matrice[1][1] == matrice[0][2] == 1:
        player = '1'
        msg_gagne()
        r += 1
        score.itemconfigure(score_rouge, text=r)
        fin_de_partie()
    if matrice[2][0] ==  matrice[1][1] == matrice[0][2] == 2 or matrice[0][0] ==  matrice[1][1] == matrice[2][2] == 2:
        player = '2'
        msg_gagne()
        b += 1
        score.itemconfigure(score_bleu, text=b)
        fin_de_partie()


def msg_gagne():
    """"fenetre auxiliaire qui affiche message 'Gagné' par dessus le plateau"""
    global player
    msg = tk.Toplevel(plateau)
    msg.title("Fin de partie")
    gagné = tk.Canvas(msg, height=100, width=400, bg='dark khaki')
    gagné.create_text(130, 60, text='Joueur', font=('comic sans ms', '16'))
    gagné.create_text(190, 60, text=player, font=('comic sans ms', '16'))
    gagné.create_text(280, 60, text='a gagné !', font=('comic sans ms', '16'))
    gagné.grid()
    #def fermer_msg():
        #msg.destroy()
    
    #msg.after(3000, fermer_msg()) # ça marche pas????


def fin_de_partie():
    """relance une partie tant qu'il n'y a pas de vainqueur"""
    #global r, b
    #while r < 4 or b < 4:
    pass


canvas.bind("<Button-1>", Place_Pion)


plateau.mainloop()

########################
