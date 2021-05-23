Jeu du Tapatan
Versions pour 2 joueurs, 1 joueur contre une IA, et IA contre IA.

Fonctionnement du jeu :
Chaque joueur possède 3 pions, et le but est d'aligner ses trois pions sur le plateau de façon horizontale, verticale ou diagonale. Il faut d'abord poser ses trois pions sur le plateau en cliquant sur l'emplacement gris où vous voulez poser votre pion, puis on peut déplacer un pion vers un emplacement libre en suivant un des traits noirs formés par le plateau. Pour cela, il suffit de cliquer d'abord sur le pion que l'on veut déplacer, et ensuite sur l'emplacement vide vers lequel on veut déplacer le pion. Attention, on ne peut pas annuler la sélection d'un pion pour le bouger. Si le pion sélectionné ne peut pas être déplacé, il faut cliquer à nouveau sur ce pion et ainsi passer son tour. 
Le gagnant d'une manche est donc le premier joueur à aligner ses trois pions sur le plateau, et le gagnant de la partie est le premier joueur à gagner 3 manches. 
Une manche est déclarée "match nul" lorsque la même configuration du plateau se produit trois fois.
Pour quitter une partie en cours, il faut cliquer sur le bouton "Quitter" et non pas fermer la fenêtre du plateau. 
Les boutons "Sauvegarder la partie" et "Recharger la partie" permettent respectivement d'enregistrer une partie en cours pour la reprendre plus tard, et de continuer une partie déjà commencée qui a été sauvegardée précédemment.
Les boutons "+" et "-" de "Vitesse de l'IA" permettent respectivement d'augmenter et de diminuer la vitesse de l'IA afin d'avoir une IA qui joue plus ou moins rapidement.
Fonctionnement du code : 
Pour créer notre jeu du Tapatan, nous avons utilisé une matrice 3 x 3 déterminant les 9 emplacements possibles du plateau, dans laquelle nous avons indiqué par les chiffres 0, 1 et 2 la couleur de l'emplacement. 0 indique que l'emplacement est gris, donc vide, 1 indique que l'emplacement est rouge, donc occupé par un pion rouge, et 2 indique que l'emplacement est bleu, donc occupé par un pion bleu.
Lorsqu'on lance le programme, un menu s'affiche pour nous demander quel type de partie on veut lancer, ou si l'on veut voir les règles du jeu. Le bouton "0 joueur" lance une partie IA contre IA, le bouton "1 joueur" lance une partie joueur contre IA, et le bouton "2 joueurs" lance une partie joueur contre joueur.
