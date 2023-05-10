# -*- coding: utf-8 -*-

import numpy as np
import Joueur

""" Ce module contient la définition de la classe Club permettant la création des équipes """

class Club(list, Joueur.Joueur):
    def __init__(self, nom_club, niveau, noms_joueurs):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison (initialisés à 0)
        """
        super().__init__()
        self.noms_joueurs = noms_joueurs
        self.nom_club = nom_club
        # On attribue un niveau à chaque club (en fonction des résultats de cette année)
        self.niveau = niveau
        self.points = 0
        self.buts_marques = 0



    def __str__(self):
        """On définit __str__ la méthode retournant le nom de clubs, leur nombre de poinst et le nombre de buts marqués sous forme de dataframe
        """
        return f"Noms des clubs : {self.nom_club}, Nombre de points : {self.points}, Buts marqués : {self.buts_marques}"

if __name__ == "__main__":
    niveau = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                       3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                       3.75, 1, 2.25, 0.75]).reshape((20, 1))

    # Extraction de la liste des joueurs
    fichier = open("noms_joueurs.txt", 'r')
    noms_joueurs = []
    fichier.seek(0)
    for ligne in fichier:  # Il y a une équipe de 11 joueurs par ligne
        equipe = []
        noms = ligne.strip(" \n")
        noms = noms.split()  # Le nom de chaque joueur est séparé par un espace
        for nom in noms:
            equipe.append(nom)
        noms_joueurs.append(equipe)
    fichier.close()  # Fermeture du fichier après lecture
    #noms_joueurs = np.array(noms_joueurs).reshape((20,))

    # Extraction de la liste des clubs
    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    i = 0
    for nom_club in fichier:  # Il y a un club par ligne
        nom_club = nom_club.strip(" \n")
        noms_clubs.append(nom_club)
        club = Club(nom_club, niveau[i], noms_joueurs[i])
        print(club)
        i+=1
    fichier.close()  # Fermeture du fichier après lecture