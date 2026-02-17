# --------------------------------------------------------------------
# Créé par : MIRALLES Nicola
# Classe : TF
# Date de création : 04/10/2024
# Version = '3.0'
# --------------------------------------------------------------------


from turtle import *
from random import *

class Carre:
    """Classe qui modélise un carré"""
    
    # Constructeur de la classe Carre
    def __init__(self, cote, abscisse, ordonnee):
        self.__cote = cote
        self.__abscisse = abscisse
        self.__ordonnee = ordonnee
    
    def get_cote(self):
        return self.__cote
    def get_abscisse(self):
        return self.__abscisse
    def get_ordonne(self):
        return self.__ordonnee
    
    
    # Méthode pour afficher le carré au coin inférieur gauche (abscisse ; ordonnee)
    def afficher(self):
        """Affiche le carré avec une couleur spécifique."""
        up()
        goto(self.__abscisse, self.__ordonnee)
        down()
        fillcolor(self.couleur)
        begin_fill() 
        for i in range(4):
            forward(self.__cote)
            left(90)
        end_fill()

#Fin de la classe Carre  
# --------------------------------------------------------------------


def tapis(n, longueur, a, o):
    """ Fonction récursive qui trace le tapis de Sierpinsky """
    if n == 0:
        carre = Carre(longueur // 3, a + longueur // 3, o + longueur // 3)
        carre.couleur = liste_couleur[n] 
        carre.afficher() 
    else:
        c = longueur // 3
        grand_carre = Carre(c, a + c, o + c)
        grand_carre.couleur = liste_couleur[n] 
        grand_carre.afficher() 
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    tapis(n - 1, c, a + i * c, o + j * c) 

#Fin de la fonction tapis 
# --------------------------------------------------------------------


liste_couleur = [(randint(0, 255), randint(0, 255), randint(0, 255))]
nb_couleur = 5
for i in range(nb_couleur):
    liste_couleur.append((randint(0, 255), randint(0, 255), randint(0, 255)))
speed('fastest')  # Vitesse la plus rapide
colormode(255) 
color(liste_couleur[0])
carre1 = Carre(300, -200, -200)
carre1.couleur = liste_couleur[0] 
carre1.afficher() 
tapis(3, 300, -200, -200)  
ht()  # Pour cacher la tortue
