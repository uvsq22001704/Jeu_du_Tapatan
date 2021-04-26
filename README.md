# Jeu_du_Tapatan

Notations:

    pour la matrice:
    0 gris
    1 rouge
    2 bleu



Jeu du Tapatan pour deux joueurs, soit un joueur réel et une IA, soit deux IA l'une contre l'autre. 

Chacun des deux joueurs dispose de 3 jetons. Le vainqueur est le premier joueur à aligner 3 de ses jetons sur le plateau.

Le jeu se déroule en deux étapes:
- l’étape de placement: au début le plateau est vide, puis les joueurs posent un jeton à tour de rôle sur une intersection libre du plateau;
- l’étape de déplacement: s’il n’y a pas déjà un vainqueur, les joueurs bougent à tour de rôle un jeton sur une intersection voisine (atteignable en empruntant une des droites) libre;
si l’on tombe une troisième fois sur la même disposition des jetons sur le plateau, alors le match est déclaré nul.

Votre interface graphique doit permettre à 2 humains de jouer au jeu. Faire une version ou chaque victoire rapporte un point et le jeu s’arrête dès qu’un des joueurs à 3 points et est alors déclaré vainqueur. A chaque partie, il faut changer le joueur qui débute la partie. Un match nul n’apporte aucun point.

En plus de la programmation du jeu, vous programmerez les fonctionnalités suivantes:
- pouvoir sauvegarder une partie en cours, et la recharger ensuite;
- ajouter une version humain contre IA et IA contre IA; une IA simple consiste à jouer de la manière suivante que ce soit pour l’étape de placement ou de déplacement (mais vous pouvez proposer autre chose):
    - jouer un coup qui fait gagner la partir s’il y en a un
    - sinon jouer pour éviter que l’adversaire ait un coup qui le fasse gagner s’il y en a un
    - sinon jouer un coup au hasard
