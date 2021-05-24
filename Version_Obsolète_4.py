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


matrice = []   # on créer une liste 2D dans laquelle se trouvent la couleur de chaque cases du plateau
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

r = 0 #compteur du score rouge
b = 0 #compteur du score bleu

position_prece = [1,1] #sert à connaitre la position du pion que l'on s'apprete à déplacer

fantome_de_tes_matrices_passées = [] #index chaques matrices de la manche dans l'éventualité d'un match nul

nb_ia = 0

pommeau_pathétiquement_croustillant = [[[350, 100], [350,350], [350, 600]], [[600,100] , [600, 350], [600, 600]], [[850, 100], [850, 350], [850, 600]]]

########################
# fonctions




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
    menu.iconify()
    open_plateau()

def P1j():
    global nb_ia 
    nb_ia = 1
    menu.iconify()
    open_plateau()

def P2j():
    global nb_ia
    nb_ia = 0
    menu.iconify()
    open_plateau()
    
def regles():
    """fonction liée au bouton 'Règles du jeu'. Ouvre une fenêtre auxiliaire
    avec explication des règles. Quand on appuie sur le bouton 'Retour', la fenêtre
    se ferme et on revient au menu"""
    rules = tk.Toplevel(menu)
    rules.title("Jvous jure ça marche comme ça")
    regles = tk.Label(rules, text ='REGLES DU JEU DU TAPATAN', font=('comic sans ms','20'), padx = 10, pady = 17, bg='white')
    regless = tk.Label(rules, text ="Les joueurs disposent de 3 jetons.\n A tour de rôle, chaque joueur"
                        ' pose un pion sur une case disponible (en gris).\n Une fois les 6 pions placés,'
                        "les joueurs dépalcent un de leur pion\n d'une case selon les lignes (horizontales,"
                        " verticales, diagonales).\n Le gagnant est le premier joueur à aligner 3 pions sur le"
                        " plateau.\n Si durant la partie, le plateau revient 3 fois à la\n même configuration de pions,"
                        " il y a match nul. Une partie se joue en 3 manches", font = ('comic sans ms','16'), bg = 'white', anchor = 'w')
    retour = tk.Button(rules, text='Retour', command=rules.destroy)
    regles.grid(row = 0, sticky='E'+'W')
    regless.grid(row = 1)
    retour.grid(row = 2)

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






########################
# plateau
def open_plateau():
    global nb_ia, tour, nb_pions_b, nb_pions_r, r, b, position_prece, fantome_de_tes_matrices_passées
    plateau = tk.Toplevel()

    
    def mapla():
        ''' met à jour la couleur des pions sur le plateau'''
        pions_cote()
        affiche_tour()
        print("tiiuyftdfg", tour)
        for i in range (3):
            for j in range (3):
                if matrice [i][j] == 1 :
                    canvas.itemconfig(liCe[i][j], fill = 'red', outline = "red")
                if matrice [i][j] == 2 :
                    canvas.itemconfig(liCe[i][j], fill = 'blue', outline = "blue")
                if matrice [i][j] == 0 :
                    canvas.itemconfig(liCe[i][j], fill = 'grey', outline = "grey")


    def recharger(): 
        """charger la grille depuis le fichier sauvegarde.txt"""
        global matrice, tour, position_prece, nb_pions_b, nb_pions_r, r, b
        fic = open("sauvegarde.txt", "r")
        j = 0
        for ligne in fic:
            i = 0
            val = ligne.split()
            for e in val:
                if e == "0":
                    matrice[i][j] = 0
                elif e =="1" :
                    matrice[i][j] = 1
                elif e == "2" :
                    matrice[i][j] = 2
                i += 1
            j += 1
        fic.close()  
        mapla()

        fic2 = open("sauvegarde2.txt","r")
        tour_txt = fic2.read()
        tour = int(tour_txt)
        fic2.close()

        fic4 = open("sauvegarde4.txt","r")
        nb_pions_b_txt = fic4.read()
        nb_pions_b = int(nb_pions_b_txt)
        fic4.close()

        fic5 = open("sauvegarde5.txt","r")
        nb_pions_r_txt = fic5.read()
        nb_pions_r = int(nb_pions_r_txt)
        fic5.close()
        
        fic6 = open("sauvegarde6.txt","r")
        r_txt = fic6.read()
        r = int(r_txt)
        fic6.close()

        affiche_tour()

        fic7 = open("sauvegarde7.txt","r")
        b_txt = fic7.read()
        b = int(b_txt)
        fic7.close()

        affiche_tour()
    
        return tour, position_prece, nb_pions_b, nb_pions_r, r, b

    def sauvegarder():
        """sauvegarder la grille vers le fichier sauvegarde.txt"""
        global matrice, tour, position_prece, nb_pions_b, nb_pions_r, r, b
        fic = open("sauvegarde.txt", "w")
        for j in range(3):
            for i in range(3):
                if matrice[i][j] == 0:
                    fic.write("0 ")
                elif matrice[i][j] == 1:
                    fic.write("1 ")
                elif matrice[i][j] == 2:
                    fic.write("2 ")
            fic.write("\n")
        fic.close()
        
        fic2 = open("sauvegarde2.txt","w")
        fic2.write(str(tour))
        fic2.close()
            
        fic3 = open("sauvegarde3.txt","w")
        fic3.write(str(position_prece))
        fic3.close()
        
        fic4 = open("sauvegarde4.txt","w")
        fic4.write(str(nb_pions_b))
        fic4.close()
            
        fic5 = open("sauvegarde5.txt","w")
        fic5.write(str(nb_pions_r))
        print(nb_pions_r)
        fic5.close()

        fic6 = open("sauvegarde6.txt","w")
        fic6.write(str(r))
        fic6.close()

        fic7 = open("sauvegarde7.txt","w")
        fic7.write(str(b))
        fic7.close()

    canvas = tk.Canvas(plateau, height=HEIGHT, width=WIDTH, bg = "white")
    bouton_sauvegarder = tk.Button(plateau, text='Sauvegarder la partie',
                                command = sauvegarder, font = ('comic sans ms', '9'))
    bouton_recharger = tk.Button(plateau, text='Recharger la partie', command = recharger, font = ('comic sans ms', '9'))
    score = tk.Label(plateau, text='SCORE : ' + str(r) + ' - ' + str(b), font=('comic sans ms', '16'), pady=10, padx=20, bg='dark khaki')


    tour_rouge = canvas.create_text(175, 250, text="Au tour des rouges", font=('comic sans ms', '20', ), fill = "white")
    tour_bleu = canvas.create_text(1025, 250, text="Au tour des bleus", font=('comic sans ms', '20', ), fill = "white")
    bouton_sauvegarder.grid(row=0, column=0)
    bouton_recharger.grid(row=0, column=1)
    canvas.grid(row=1, columnspan=2)
    score.grid(row=0, columnspan=2)

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
                        msg = tk.Toplevel()
                        msg.lift()
                        msg.title("Fin de partie")
                        nul = tk.Canvas(msg, height=100, width=300, bg='RoyalBlue1')
                        nul.create_text(130, 60, text='Match Nul', font=('comic sans ms', '16'))
                        nul.grid()
                        fantome_de_tes_matrices_passées = []
                        return 
                    
                        
    

    def affiche_tour():
        '''met à jour le compteur de tour'''
        if tour % 2 != 0:
            canvas.itemconfigure(tour_rouge, fill="red")
            canvas.itemconfigure(tour_bleu, fill="white")
        elif tour % 2 == 0:
            canvas.itemconfigure(tour_bleu, fill="blue") 
            canvas.itemconfigure(tour_rouge, fill="white")


    def bouge_pion_rouge (a, b, c, d):
        """bouge un pion du cercle(a,b) vers le cercle(c,d)"""
        global tour, krokmou
        matrice[a][b] = 0
        matrice[c][d] = 1
        mapla()
        tour += 1
        krokmou = 1
        win_ckeck(matrice)
        if nb_ia == 2:
            IA_bleu()
        affiche_tour()


    def bouge_pion_bleu (a, b, c, d):
        """bouge un pion du cercle(a,b) vers le cercle(c,d)"""
        global tour, krokmou
        krokmou = 1
        matrice[a][b] = 0
        matrice[c][d] = 2
        mapla()
        tour += 1
        win_ckeck(matrice)
        if nb_ia == 2:
            IA_rouge()


    def placement_IA():
        print("zebi placement_ia()")

        global tour, nb_pions_r, nb_pions_b
        print("nb_pions_b", nb_pions_b, "    pions_bleus    nb_pions_r", nb_pions_r)
        """place les pions au début de l'IA (supposément que pour une partie 0 joueurs ?!)"""

        if nb_pions_b == 3 and nb_pions_r == 3:
            print('la peut etre?')
            Coup_rd()
            print('first coup rd')
            return
        if nb_pions_b == 2 and nb_pions_r == 3:
            print("censé etre la ptn")
            Coup_rd()
            print('second coup rd')
            return
        if nb_pions_b == 2 and nb_pions_r == 2:
            Coup_rd()
            print('third coup rd')
            return
        # aux rouges de jouer pour bloquer les bleus
        if nb_pions_b == 1 and nb_pions_r == 2:
            #alignement horizontal
            print('papaoutai')
            for i in range(3):
                if matrice[i][0] == matrice[i][1] == 2 and matrice[i][2] == 0:
                    matrice[i][2] = 1
                    mapla()
                    tour += 1 
                    nb_pions_r -= 1
                    #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                    return
                elif matrice[i][0] == matrice[i][2] == 2 and matrice[i][1] == 0:
                    matrice[i][1] = 1
                    mapla()
                    tour += 1
                    nb_pions_r -= 1
                    #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                    return
                elif matrice[i][2] == matrice[i][1] == 2 and matrice[i][0] == 0:
                    matrice[i][0] = 1
                    mapla()
                    tour += 1
                    nb_pions_r -= 1
                    return
            #alignement vertical
            for j in range(3):
                if matrice[0][j] == matrice[1][j] == 2 and matrice[2][j] == 0:
                    matrice[2][j] = 1
                    mapla()
                    tour += 1
                    nb_pions_r -= 1
                    #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                    return
                elif matrice[0][j] == matrice[2][j] == 2 and matrice[1][j] == 0:
                    matrice[1][j] = 1
                    mapla()
                    tour += 1
                    nb_pions_r -= 1
                    #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                    return
                elif matrice[2][j] == matrice[1][j] == 2 and matrice[0][j] == 0:
                    matrice[0][j] = 1
                    mapla()
                    tour += 1
                    nb_pions_r -= 1
                    #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                    return
            #alignement diagonal
            if 2 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                matrice[2][2] = 1
                mapla()
                tour += 1
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            elif 2 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                matrice[0][0] = 1
                mapla()
                tour += 1
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            elif 2 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                matrice[1][1] = 1
                mapla()
                tour += 1
                
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            elif 2 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                matrice[1][1] = 1
                mapla()
                tour += 1
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            elif 2 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                matrice[0][2] = 1
                mapla()
                tour += 1
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            elif 2 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                matrice[2][0] = 1
                mapla()
                tour += 1
                nb_pions_r -= 1
                #if nb_ia == 2:
                        #canvas.after(1000, IA_bleu())
                return
            else:
                Coup_rd()
                nb_pions_r -= 1
            pions_cote()
            if nb_ia == 2:
                    canvas.after(1000, IA_bleu)
                    return
        # aux bleus de jouer pour bloquer les rouges

        elif nb_pions_b == 1 and nb_pions_r == 1:
            #alignement horizontal
            print('where are uuu?')
            for i in range(3):
                if matrice[i][0] == matrice[i][1] == 1 and matrice[i][2] == 0:
                    matrice[i][2] = 2
                    
                    tour += 1 
                    nb_pions_b -= 1
                    mapla()
                    return
                if matrice[i][0] == matrice[i][2] == 1 and matrice[i][1] == 0:
                    matrice[i][1] = 2
                    
                    tour += 1
                    nb_pions_b -= 1
                    mapla()
                    return
                if matrice[i][2] == matrice[i][1] == 1 and matrice[i][0] == 0:
                    matrice[i][0] = 2
                    
                    tour += 1
                    nb_pions_b -= 1
                    mapla()
                    return
            #alignement vertical
            for j in range(3):
                if matrice[0][j] == matrice[1][j] == 1 and matrice[2][j] == 0:
                    matrice[2][j] = 2
                    tour += 1
                    nb_pions_b -= 1
                    mapla()

                    return
                if matrice[0][j] == matrice[2][j] == 1 and matrice[1][j] == 0:
                    matrice[1][j] = 2
                    
                    tour += 1
                    nb_pions_b -= 1
                    mapla()
                    return
                if matrice[2][j] == matrice[1][j] == 1 and matrice[0][j] == 0:
                    matrice[0][j] = 2
                    tour += 1
                    nb_pions_b -= 1
                    mapla()
                    return
            #alignement diagonal
            if 1 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                matrice[2][2] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            if 1 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                matrice[0][0] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            if 1 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                matrice[1][1] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            if 1 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                matrice[1][1] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            if 1 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                matrice[0][2] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            if 1 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                matrice[2][0] = 2
                tour += 1
                nb_pions_b -= 1
                mapla()
                return
            else:
                Coup_rd()
                nb_pions_b -= 1
            pions_cote()
            if nb_ia == 2:
                        canvas.after(1000, IA_rouge)
        # aux rouges de jouer pour bloquer les bleus
        elif nb_pions_b == 0 and nb_pions_r == 1:
            #alignement horizontal
            print('go back to sleep and starve')
            for i in range(3):
                if matrice[i][0] == matrice[i][1] == 2 and matrice[i][2] == 0:
                    matrice[i][2] = 1
                    tour += 1 
                    nb_pions_r -= 1
                    mapla()
                    return
                if matrice[i][0] == matrice[i][2] == 2 and matrice[i][1] == 0:
                    matrice[i][1] = 1
                    tour += 1
                    nb_pions_r -= 1
                    mapla()
                    return
                if matrice[i][2] == matrice[i][1] == 2 and matrice[i][0] == 0:
                    matrice[i][0] = 1
                    tour += 1
                    nb_pions_r -= 1
                    mapla()
                    return
            #alignement vertical
            for j in range(3):
                if matrice[0][j] == matrice[1][j] == 2 and matrice[2][j] == 0:
                    matrice[2][j] = 1
                    tour += 1
                    nb_pions_r -= 1
                    mapla()
                    return
                if matrice[0][j] == matrice[2][j] == 2 and matrice[1][j] == 0:
                    matrice[1][j] = 1
                    tour += 1
                    nb_pions_r -= 1
                    mapla()
                    return
                if matrice[2][j] == matrice[1][j] == 2 and matrice[0][j] == 0:
                    matrice[0][j] = 1
                    tour += 1
                    nb_pions_r -= 1
                    mapla()
                    return

            #alignement diagonal
            if 2 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                matrice[2][2] = 1
                tour += 1
                nb_pions_r -= 1
                mapla()
                return
            if 2 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                matrice[0][0] = 1
                tour += 1
                nb_pions_r -= 1
                mapla()
                return
            if 2 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                matrice[1][1] = 1
                tour += 1
                nb_pions_r -= 1
                mapla()
                print("gjgytctfytguifytfyfjhgjhg", tour, nb_pions_r)
                return
            if 2 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                matrice[1][1] = 1
                tour += 1
                nb_pions_r -= 1
                mapla()
                return
            if 2 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                matrice[0][2] = 1
                tour += 1
                nb_pions_r -= 1
                mapla()
                return
            if 2 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                matrice[2][0] = 1
                tour += 1  
                nb_pions_r -= 1 
                mapla()
                return
            else:
                Coup_rd()
                nb_pions_r -= 1
            pions_cote()
            if nb_ia == 2:
                        canvas.after(1000, IA_bleu)
                        return


    def depl_rd_b():
        print("depl_rd_b()")
        posx = rd.randint(0,2)
        posy = rd.randint(0,2)
        while matrice[posy][posx] != 2:
            posx = rd.randint(0,2)
            posy = rd.randint(0,2)
        print ("choisit de déplacer b",posy, posx)
        Place_Pion(pommeau_pathétiquement_croustillant[posy][posx][0],pommeau_pathétiquement_croustillant[posy][posx][1])

        posx = rd.randint(0,2)
        posy = rd.randint(0,2)
        while matrice[posy][posx] != 0 or posy - position_prece[0] > 1 or posy - position_prece[0] < -1 or posx - position_prece[1] > 1 or posx - position_prece[1] < -1:
            posx = rd.randint(0,2)
            posy = rd.randint(0,2)
        print ("vers b ",posy, posx)
        Place_Pion(pommeau_pathétiquement_croustillant[posy][posx][0],pommeau_pathétiquement_croustillant[posy][posx][1])
        affiche_tour()


    def depl_rd_r():
        print("depl_rd_r()")
        posx = rd.randint(0,2)
        posy = rd.randint(0,2)
        while matrice[posy][posx] != 1:
            posx = rd.randint(0,2)
            posy = rd.randint(0,2)
        print ("choisit de déplacer r",posy, posx)
        Place_Pion(pommeau_pathétiquement_croustillant[posy][posx][0],pommeau_pathétiquement_croustillant[posy][posx][1])

        posx = rd.randint(0,2)
        posy = rd.randint(0,2)
        while matrice[posy][posx] != 0 or posy - position_prece[0] > 1 or posy - position_prece[0] < -1 or posx - position_prece[1] > 1 or posx - position_prece[1] < -1:
            posx = rd.randint(0,2)
            posy = rd.randint(0,2)
        print ("vers r ",posy, posx)
        Place_Pion(pommeau_pathétiquement_croustillant[posy][posx][0],pommeau_pathétiquement_croustillant[posy][posx][1])
        affiche_tour()


    def IA_rouge():
        """intelligence artificielle du jeu pour un pion rouge"""
        global tour, pommeau_pathétiquement_croustillant, krokmou
        print("IA_rouge()")
            #IA coup gagnant :
            #cas 1
        krokmou = 0
        if tour >5:
            if 1 == matrice[0][0] == matrice[0][1] and matrice[0][2] == 0:
                if matrice[0][0] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 2)
                    return
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 0, 2)
                    return
            #cas 2 
            if 1 == matrice[0][1] == matrice[0][2] and matrice[0][0] == 0:
                if matrice[0][1] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 0)
                    return
                elif matrice[0][1] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 0, 0)
                    return
            #cas 3
            if 1 == matrice[1][0] == matrice[1][1] and matrice[1][2] == 0:
                if matrice[1][0] == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 2)
                    return
                elif matrice[1][0] == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 2)
                    return
            #cas 4
            if 1 == matrice[1][1] == matrice[1][2] and matrice[1][0] == 0:
                if matrice[1][1] == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 0)
                    return
                elif matrice[1][1] == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 0)
                    return
            #cas 5
            if 1 == matrice[2][0] == matrice[2][1] and matrice[2][2] == 0:
                if matrice[2][0] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 2)
                    return
                elif matrice[2][0] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 2)
                    return
            #cas 6
            if 1 == matrice[2][1] == matrice[2][2] and matrice[2][0] == 0:
                if matrice[2][1] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 0)
                    return
                elif matrice[2][1] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 0)
                    return
            #cas 7
            if 1 == matrice[0][0] == matrice[1][0] and matrice[2][0] == 0:
                if matrice[0][0] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 0)
                    return
                elif matrice[0][0] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 0)
                    return
            #cas 8
            if 1 == matrice[1][0] == matrice[2][0] and matrice[0][0] == 0:
                if matrice[1][0] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 0)
                    return
                elif matrice[1][0] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 0)
                    return
            #cas 9
            if 1 == matrice[0][1] == matrice[1][1] and matrice[2][1] == 0:
                if matrice[0][1] == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 2, 1)
                    return
                elif matrice[0][1] == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 2, 1)
                    return
            #cas 10
            if 1 == matrice[1][1] == matrice[2][1] and matrice[0][1] == 0:
                if matrice[1][1] == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 0, 1)
                    return
                elif matrice[1][1] == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 0, 1)
                    return
            #cas 11
            if 1 == matrice[0][2] == matrice[1][2] and matrice[2][2] == 0:
                if matrice[0][2] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 2)
                    return
                elif matrice[0][2] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 2)
                    return
            #cas 12
            if 1 == matrice[1][2] == matrice[2][2] and matrice[0][2] == 0:
                if matrice[1][2] == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 2)
                    return
                elif matrice[1][2] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 2)
                    return
            #cas 13
            if 1 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                if matrice[0][0] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 2)
                    return
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 2, 2)
                    return
            #cas 14
            if 1 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                if matrice[1][1] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 0)
                    return
                elif matrice[1][1] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 0, 0)
                    return
            #cas 15
            if 1 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                if matrice[0][0] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif matrice[0][0] == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif matrice[0][0] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif matrice[0][0] == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif matrice[0][0] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
            #cas 16
            if 1 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                if matrice[2][0] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif matrice[2][0] == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif matrice[2][0] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif matrice[2][0] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif matrice[2][0] == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return
                elif matrice[2][0] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
            #cas 17
            if 1 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                if matrice[1][1] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 2)
                    return
                elif matrice[1][1] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 0, 2)
                    return
            #cas 18
            if 1 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                if matrice[1][1] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 0)
                    return
                elif matrice[1][1] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 0)
                    return
            #cas 19
            if 1 == matrice[0][0] == matrice[2][0] == matrice[1][1] and matrice[1][0] == 0:
                    bouge_pion_rouge(1, 1, 1, 0)
                    return
            #cas 20
            if 1 == matrice[2][0] == matrice[2][2] == matrice[1][1] and matrice[2][1] == 0:
                    bouge_pion_rouge(1, 1, 2, 1)
                    return
            #cas 21
            if 1 == matrice[0][0] == matrice[0][2] == matrice[1][1] and matrice[0][1] == 0:
                    bouge_pion_rouge(1, 1, 0, 1)
                    return
            #cas 22
            if 1 == matrice[0][2] == matrice[2][2] == matrice[1][1] and matrice[1][2] == 0:
                    bouge_pion_rouge(1, 1, 1, 2)
                    return
            #cas 23
            if 1 == matrice[1][0] == matrice[1][2] and matrice[1][1] == 0:
                if matrice[1][0] == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif matrice[1][0] == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif matrice[1][0] == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif matrice[1][0] == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif matrice[1][0] == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
                elif matrice[1][0] == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return
            #cas 24
            if 1 == matrice[0][1] == matrice[2][1] and matrice[1][1] == 0:
                if matrice[0][1] == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif matrice[0][1] == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif matrice[0][1] == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif matrice[0][1] == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif matrice[0][1] == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif matrice[0][1] == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return

            #IA coup pour empecher l'autre de gagner :
            #cas 1
            if 2 == matrice[0][0] == matrice[0][1] and matrice[0][2] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 2)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 0, 2)
                    return
            #cas 2 
            if 2 == matrice[0][1] == matrice[0][2] and matrice[0][0] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 0)
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 0, 0)
                    return
            #cas 3
            if 2 == matrice[1][0] == matrice[1][1] and matrice[1][2] == 0:
                if 1 == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 2)
                    return
                elif 1 == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 2)
                    return
            #cas 4
            if 2 == matrice[1][1] == matrice[1][2] and matrice[1][0] == 0:
                if 1 == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 0)
                    return
                elif 1 == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 0)
                    return
            #cas 5
            if 2 == matrice[2][0] == matrice[2][1] and matrice[2][2] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 2)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 2)
                    return
            #cas 6
            if 2 == matrice[2][1] == matrice[2][2] and matrice[2][0] == 0:
                if 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 0)
                    return
                elif 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 0)
                    return
            #cas 7
            if 2 == matrice[0][0] == matrice[1][0] and matrice[2][0] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 0)
                    return
                elif 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 0)
                    return
            #cas 8
            if 2 == matrice[1][0] == matrice[2][0] and matrice[0][0] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 0)
                    return
                elif 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 0)
                    return
            #cas 9
            if 2 == matrice[0][1] == matrice[1][1] and matrice[2][1] == 0:
                if 1 == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 2, 1)
                    return
                elif 1 == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 2, 1)
                    return
            #cas 10
            if 2 == matrice[1][1] == matrice[2][1] and matrice[0][1] == 0:
                if 1 == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 0, 1)
                    return
                elif 1 == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 0, 1)
                    return
            #cas 11
            if 2 == matrice[0][2] == matrice[1][2] and matrice[2][2] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 2, 2)
                    return
                elif 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 2)
                    return
            #cas 12
            if 2 == matrice[1][2] == matrice[2][2] and matrice[0][2] == 0:
                if 1 == matrice[1][1]:
                    bouge_pion_rouge(1, 1, 0, 2)
                    return
                elif 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 2)
                    return
            #cas 13
            if 2 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                if 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 2)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 2, 2)
                    return
            #cas 14
            if 2 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                if 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 0)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 0, 0)
                    return
            #cas 15
            if 2 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                if 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif 1 == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif 1 == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
            #cas 16
            if 2 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                if 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif 1 == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif 1 == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return
                elif 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
            #cas 17
            if 2 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                if 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 0, 2)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 0, 2)
                    return
            #cas 18
            if 2 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                if 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 2, 0)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 2, 0)
                    return
            #cas 19
            if 2 == matrice[0][0] == matrice[2][0] and 1 == matrice[1][1] and matrice[1][0] == 0:
                    bouge_pion_rouge(1, 1, 1, 0)
                    return
            #cas 20
            if 2 == matrice[2][0] == matrice[2][2] and 1 == matrice[1][1] and matrice[2][1] == 0:
                    bouge_pion_rouge(1, 1, 2, 1)
                    return
            #cas 21
            if 2 == matrice[0][0] == matrice[0][2] and 1 == matrice[1][1] and matrice[0][1] == 0:
                    bouge_pion_rouge(1, 1, 0, 1)
                    return
            #cas 22
            if 2 == matrice[0][2] == matrice[2][2] and 1 == matrice[1][1] and matrice[1][2] == 0:
                    bouge_pion_rouge(1, 1, 1, 2)
                    return
            #cas 23
            if 2 == matrice[1][0] == matrice[1][2] and matrice[1][1] == 0:
                if 1 == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif 1 == matrice[0][1]:
                    bouge_pion_rouge(0, 1, 1, 1)
                    return
                elif 1 == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif 1 == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif 1 == matrice[2][1]:
                    bouge_pion_rouge(2, 1, 1, 1)
                    return
                elif 1 == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return
            #cas 24
            if 2 == matrice[0][1] == matrice[2][1] and matrice[1][1] == 0:
                if 1 == matrice[0][0]:
                    bouge_pion_rouge(0, 0, 1, 1)
                    return
                elif 1 == matrice[1][0]:
                    bouge_pion_rouge(1, 0, 1, 1)
                    return
                elif 1 == matrice[0][2]:
                    bouge_pion_rouge(0, 2, 1, 1)
                    return
                elif 1 == matrice[2][0]:
                    bouge_pion_rouge(2, 0, 1, 1)
                    return
                elif 1 == matrice[1][2]:
                    bouge_pion_rouge(1, 2, 1, 1)
                    return
                elif 1 == matrice[2][2]:
                    bouge_pion_rouge(2, 2, 1, 1)
                    return
            if krokmou == 0 and tour > 5:
                depl_rd_r()
        # coup random
        else:
            placement_IA()


    def IA_bleu():
        global krokmou
        """intelligence artificielle du jeu pour un pion bleu"""
        print("IA_bleu()")
        global tour ,pommeau_pathétiquement_croustillant
        krokmou = 0
        if tour > 5 and nb_ia == 2:
            
            #IA coup gagnant :
            #cas 1
            if 2 == matrice[0][0] == matrice[0][1] and matrice[0][2] == 0:
                if matrice[0][0] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 2)
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 0, 2)
            #cas 2 
            if 2 == matrice[0][1] == matrice[0][2] and matrice[0][0] == 0:
                if matrice[0][1] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 0)
                elif matrice[0][1] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 0, 0)
            #cas 3
            if 2 == matrice[1][0] == matrice[1][1] and matrice[1][2] == 0:
                if matrice[1][0] == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 2)
                elif matrice[1][0] == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 2)
            #cas 4
            if 2 == matrice[1][1] == matrice[1][2] and matrice[1][0] == 0:
                if matrice[1][1] == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 0)
                elif matrice[1][1] == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 0)
            #cas 5
            if 2 == matrice[2][0] == matrice[2][1] and matrice[2][2] == 0:
                if matrice[2][0] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 2)
                elif matrice[2][0] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 2)
            #cas 6
            if 2 == matrice[2][1] == matrice[2][2] and matrice[2][0] == 0:
                if matrice[2][1] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 0)
                elif matrice[2][1] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 0)
            #cas 7
            if 2 == matrice[0][0] == matrice[1][0] and matrice[2][0] == 0:
                if matrice[0][0] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 0)
                elif matrice[0][0] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 0)
            #cas 8
            if 2 == matrice[1][0] == matrice[2][0] and matrice[0][0] == 0:
                if matrice[1][0] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 0)
                elif matrice[1][0] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 0)
            #cas 9
            if 2 == matrice[0][1] == matrice[1][1] and matrice[2][1] == 0:
                if matrice[0][1] == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 2, 1)
                elif matrice[0][1] == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 2, 1)
            #cas 10
            if 2 == matrice[1][1] == matrice[2][1] and matrice[0][1] == 0:
                if matrice[1][1] == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 0, 1)
                elif matrice[1][1] == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 0, 1)
            #cas 11
            if 2 == matrice[0][2] == matrice[1][2] and matrice[2][2] == 0:
                if matrice[0][2] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 2)
                elif matrice[0][2] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 2)
            #cas 12
            if 2 == matrice[1][2] == matrice[2][2] and matrice[0][2] == 0:
                if matrice[1][2] == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 2)
                elif matrice[1][2] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 2)
            #cas 13
            if 2 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                if matrice[0][0] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 2)
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 2, 2)
            #cas 14
            if 2 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                if matrice[1][1] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 0)
                elif matrice[1][1] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 0, 0)
            #cas 15
            if 2 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                if matrice[0][0] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif matrice[0][0] == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif matrice[0][0] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif matrice[0][0] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif matrice[0][0] == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif matrice[0][0] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
            #cas 16
            if 2 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                if matrice[2][0] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif matrice[2][0] == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif matrice[2][0] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif matrice[2][0] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif matrice[2][0] == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)
                elif matrice[2][0] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
            #cas 17
            if 2 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                if matrice[1][1] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 2)
                elif matrice[1][1] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 0, 2)
            #cas 18
            if 2 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                if matrice[1][1] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 0)
                elif matrice[1][1] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 0)
            #cas 19
            if 2 == matrice[0][0] == matrice[2][0] == matrice[1][1] and matrice[1][0] == 0:
                    bouge_pion_bleu(1, 1, 1, 0)
            #cas 20
            if 2 == matrice[2][0] == matrice[2][2] == matrice[1][1] and matrice[2][1] == 0:
                    bouge_pion_bleu(1, 1, 2, 1)
            #cas 21
            if 2 == matrice[0][0] == matrice[0][2] == matrice[1][1] and matrice[0][1] == 0:
                    bouge_pion_bleu(1, 1, 0, 1)
            #cas 22
            elif 2 == matrice[0][2] == matrice[2][2] == matrice[1][1] and matrice[1][2] == 0:
                    bouge_pion_bleu(1, 1, 1, 2)
            #cas 23
            if 2 == matrice[1][0] == matrice[1][2] and matrice[1][1] == 0:
                if matrice[1][0] == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif matrice[1][0] == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif matrice[1][0] == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif matrice[1][0] == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif matrice[1][0] == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
                elif matrice[1][0] == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)
            #cas 24
            if 2 == matrice[0][1] == matrice[2][1] and matrice[1][1] == 0:
                if matrice[0][1] == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif matrice[0][1] == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif matrice[0][1] == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif matrice[0][1] == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif matrice[0][1] == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif matrice[0][1] == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)

            #IA coup pour empecher l'autre de gagner :
            #cas 1
            if 1 == matrice[0][0] == matrice[0][1] and matrice[0][2] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 2)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 0, 2)
            #cas 2 
            if 1 == matrice[0][1] == matrice[0][2] and matrice[0][0] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 0)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 0, 0)
            #cas 3
            if 1 == matrice[1][0] == matrice[1][1] and matrice[1][2] == 0:
                if 2 == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 2)
                elif 2 == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 2)
            #cas 4
            if 1 == matrice[1][1] == matrice[1][2] and matrice[1][0] == 0:
                if 2 == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 0)
                elif 2 == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 0)
            #cas 5
            if 1 == matrice[2][0] == matrice[2][1] and matrice[2][2] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 2)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 2)
            #cas 6
            if 1 == matrice[2][1] == matrice[2][2] and matrice[2][0] == 0:
                if 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 0)
                elif 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 0)
            #cas 7
            if 1 == matrice[0][0] == matrice[1][0] and matrice[2][0] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 0)
                elif 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 0)
            #cas 8
            if 1 == matrice[1][0] == matrice[2][0] and matrice[0][0] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 0)
                elif 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 0)
            #cas 9
            if 1 == matrice[0][1] == matrice[1][1] and matrice[2][1] == 0:
                if 2 == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 2, 1)
                elif 2 == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 2, 1)
            #cas 10
            if 1 == matrice[1][1] == matrice[2][1] and matrice[0][1] == 0:
                if 2 == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 0, 1)
                elif 2 == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 0, 1)
            #cas 11
            if 1 == matrice[0][2] == matrice[1][2] and matrice[2][2] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 2, 2)
                elif 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 2)
            #cas 12
            if 1 == matrice[1][2] == matrice[2][2] and matrice[0][2] == 0:
                if 2 == matrice[1][1]:
                    bouge_pion_bleu(1, 1, 0, 2)
                elif 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 2)
            #cas 13
            if 1 == matrice[0][0] == matrice[1][1] and matrice[2][2] == 0:
                if 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 2)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 2, 2)
            #cas 14
            if 1 == matrice[1][1] == matrice[2][2] and matrice[0][0] == 0:
                if 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 0)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 0, 0)
            #cas 15
            if 1 == matrice[0][0] == matrice[2][2] and matrice[1][1] == 0:
                if 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif 2 == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif 2 == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
            #cas 16
            if 1 == matrice[2][0] == matrice[0][2] and matrice[1][1] == 0:
                if 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif 2 == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif 2 == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)
                elif 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
            #cas 17
            if 1 == matrice[1][1] == matrice[2][0] and matrice[0][2] == 0:
                if 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 0, 2)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 0, 2)
            #cas 18
            if 1 == matrice[1][1] == matrice[0][2] and matrice[2][0] == 0:
                if 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 2, 0)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 2, 0)
            #cas 19
            if 1 == matrice[0][0] == matrice[2][0] and 2 == matrice[1][1] and matrice[1][0] == 0:
                    bouge_pion_bleu(1, 1, 1, 0)
            #cas 20
            if 1 == matrice[2][0] == matrice[2][2] and 2 == matrice[1][1] and matrice[2][1] == 0:
                    bouge_pion_bleu(1, 1, 2, 1)
            #cas 21
            if 1 == matrice[0][0] == matrice[0][2] and 2 == matrice[1][1] and matrice[0][1] == 0:
                    bouge_pion_bleu(1, 1, 0, 1)
            #cas 22
            if 1 == matrice[0][2] == matrice[2][2] and 2 == matrice[1][1] and matrice[1][2] == 0:
                    bouge_pion_bleu(1, 1, 1, 2)
            #cas 23
            if 1 == matrice[1][0] == matrice[1][2] and matrice[1][1] == 0:
                if 2 == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif 2 == matrice[0][1]:
                    bouge_pion_bleu(0, 1, 1, 1)
                elif 2 == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif 2 == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif 2 == matrice[2][1]:
                    bouge_pion_bleu(2, 1, 1, 1)
                elif 2 == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)
            #cas 24
            if 1 == matrice[0][1] == matrice[2][1] and matrice[1][1] == 0:
                if 2 == matrice[0][0]:
                    bouge_pion_bleu(0, 0, 1, 1)
                elif 2 == matrice[1][0]:
                    bouge_pion_bleu(1, 0, 1, 1)
                elif 2 == matrice[0][2]:
                    bouge_pion_bleu(0, 2, 1, 1)
                elif 2 == matrice[2][0]:
                    bouge_pion_bleu(2, 0, 1, 1)
                elif 2 == matrice[1][2]:
                    bouge_pion_bleu(1, 2, 1, 1)
                elif 2 == matrice[2][2]:
                    bouge_pion_bleu(2, 2, 1, 1)
            if krokmou == 0 and tour > 5:
                depl_rd_b()
        # coup random
        elif nb_ia == 2:
            placement_IA()  


    def Coup_rd():
        print("Coup_rd()")
        posx = rd.randint(0,2)
        posy = rd.randint(0,2)
        #print (posx, posy)
        #print(matrice)
        while matrice[posy][posx] != 0:
            posx = rd.randint(0,2)
            posy = rd.randint(0,2)
        print("nsm",pommeau_pathétiquement_croustillant[posy][posx])
        Place_Pion(pommeau_pathétiquement_croustillant[posy][posx][0],pommeau_pathétiquement_croustillant[posy][posx][1])


    def click(event):
        x, y = event.x, event.y
        Place_Pion (x, y)


    def Place_Pion(x, y):
        '''place ou déplace un pion sur le cercle gris cliqué'''
        global tour, nb_pions_b, nb_pions_r
        for i in range (3):
            for j in range (3):
                x1,y1,x2,y2 = canvas.coords(liCe[i][j]) 

                if nb_pions_b > 0 or nb_pions_r > 0: # permet de placer un pion si il en reste en stock
                #si: coord cliquées sont dans coord du cercle     & tour de bleu    & si case vide         & si la nouvelle position du pion est dans un rayon de 1 de la précédente position
                    if x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 == 0 and matrice[i][j] == 0 and i - position_prece[0] <= 1 and i - position_prece[0] >= -1 and j - position_prece[1] <= 1 and j - position_prece[1] >= -1 and nb_ia < 2:
                        canvas.itemconfig(liCe[i][j], fill = 'blue', outline = "blue")
                        tour += 1 
                        nb_pions_b -= 1
                        pions_cote()
                        matrice[i][j] = 2
                        affiche_tour()
                        mapla()
                        matcheur_nul()
                        position_prece[0], position_prece[1] = 1,1
                        if nb_ia >= 1: # ajoute un delay avant d'executer l'ia si partie à 1 joueur
                            canvas.after(1100, IA_rouge)#affiche un msg d'erreur mais fonctionne?

                    elif x <= x2 and y <= y2 and x >= x1 and y >= y1 and tour % 2 != 0 and matrice[i][j] == 0 and i - position_prece[0] <= 1 and i - position_prece[0] >= -1 and j - position_prece[1] <= 1 and j - position_prece[1] >= -1 :
                        canvas.itemconfig(liCe[i][j], fill = 'red', outline = "red")
                        tour += 1
                        nb_pions_r -= 1
                        pions_cote()
                        matrice[i][j] = 1
                        affiche_tour()
                        mapla()
                        matcheur_nul()
                        position_prece[0], position_prece[1] = 1,1  
                        if nb_ia == 2: # ajoute un delay avant d'executer l'ia si partie à 1 joueur
                        #print ("c'est la wati sauce")
                            canvas.after(1100, IA_bleu)
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
                    
        win_ckeck(matrice)
        

    def win_ckeck(matrice):
        '''évalue après chaque tour si qqn a gagné. s'il y a un gagnant, un msg 
        s'affiche dans une nouvelle fenêtre. Fermer le message lance une nouvelle partie'''
        global r, b, player
        player = ''
        for i in range(3):
            #vérifie l'alignement horizontal puis vertical des pions rouges
            if matrice[i][0] == matrice[i][1] == matrice[i][2] == 1 or matrice[0][i] == matrice[1][i] == matrice[2][i] == 1:
                player = '1'
                r += 1
                score.configure(text='SCORE : ' + str(r) + ' - ' + str(b))
                fin_de_partie()
            #vérifie l'alignement  horizontal puis vertical des pions bleus
            elif matrice[i][0] == matrice[i][1] == matrice[i][2] == 2 or matrice[0][i] == matrice[1][i] == matrice[2][i] ==2:
                player = '2'
                b += 1
                score.configure(text='SCORE : ' + str(r) + ' - ' + str(b))
                fin_de_partie()
        #vérfie l'alignement des deux diagonales pour les pions rouges   
        if matrice[0][0] ==  matrice[1][1] == matrice[2][2] == 1 or matrice[2][0] ==  matrice[1][1] == matrice[0][2] == 1:
            player = '1'
            r += 1
            score.configure(text='SCORE : ' + str(r) + ' - ' + str(b))
            fin_de_partie()
        #vérifie l'lignement des deux diagonales pour les pions bleus
        if matrice[2][0] ==  matrice[1][1] == matrice[0][2] == 2 or matrice[0][0] ==  matrice[1][1] == matrice[2][2] == 2:
            player = '2'
            b += 1
            score.configure(text='SCORE : ' + str(r) + ' - ' + str(b))
            fin_de_partie()

    def msg_gagne():
        """"fenetre auxiliaire qui affiche message 'Gagné' par dessus le plateau"""
        global player, r, b
        msg = tk.Toplevel()
        msg.lift()
        def fermer_msg():
            msg.destroy()
            canvas.after(1000, rezero())
        msg.title("Fin de manche")
        gagné = tk.Label(msg, text='Joueur '+player+' a gagné!',font=('helvetica', '16'), padx=20, pady=30,  bg='dark khaki')
        button_next_round = tk.Button(msg, text = "next", command = fermer_msg)
        gagné.grid(row = 0)
        button_next_round.grid(row = 1)
        

    def msg_vainqueur():
        '''fenêtre qui souvre quand il ya un vainqueur'''
        global r, b
        win = tk.Toplevel()
        def rejouer():
            rezero()
            plateau.destroy()
            win.destroy()
            menu.deiconify()
        win.title("Fin de partie")
        gagné = tk.Label(win, text='JOUEUR '+player+' A  GAGNE !!!', font=('helvetica', '16'), bg='dark khaki', pady=30, padx=10)
        button_quit = tk.Button(win, text='Quitter', command =menu.destroy )
        button_replay = tk.Button(win, text='Recommencer une partie', command = rejouer)
        gagné.grid(row = 0)
        button_quit.grid(row=1)
        button_replay.grid(row=2)
        r = 0
        b = 0


    def fin_de_partie():
        """relance une partie tant qu'il n'y a pas de vainqueur"""
        global r, b
        if r == 3 or b == 3:
            msg_vainqueur()
        elif r < 3 or b < 3:
            msg_gagne()
        
        
    def rezero():
        '''remet le plateau à 0'''
        global nb_pions_r, nb_pions_b, tour, fantome_de_tes_matrices_passées, r, b
        nb_pions_b = 3
        nb_pions_r = 3
        tour = 0
        fantome_de_tes_matrices_passées = []
        for i in range(3):
            for j in range(3):
                matrice[i][j] = 0
        mapla()        
        pions_cote()


    def pions_cote():
        '''gère les pions à coté'''
        global nb_pions_r, nb_pions_b
        if nb_pions_b == 2:
            canvas.itemconfigure(bleu1, fill = "grey", outline="grey")
        elif nb_pions_b == 1:
            canvas.itemconfigure(bleu2, fill = "grey", outline="grey")
        elif nb_pions_b == 0:
            canvas.itemconfigure(bleu3, fill = "grey", outline="grey")
        if nb_pions_r == 2:
            canvas.itemconfigure(rouge1, fill = "grey", outline="grey")
        elif nb_pions_r == 1:
            canvas.itemconfigure(rouge2, fill = "grey", outline="grey")
        elif nb_pions_r == 0:
            canvas.itemconfigure(rouge3, fill = "grey", outline="grey")
        if nb_pions_b == 3:
            canvas.itemconfigure(bleu1, fill = "blue", outline="blue")
            canvas.itemconfigure(bleu2, fill = "blue", outline="blue")
            canvas.itemconfigure(bleu3, fill = "blue", outline="blue")
        if nb_pions_r == 3:
            canvas.itemconfigure(rouge1, fill = "red", outline="red")
            canvas.itemconfigure(rouge2, fill = "red", outline="red")
            canvas.itemconfigure(rouge3, fill = "red", outline="red")


    canvas.bind("<Button-1>", click)

menu.mainloop()
########################
