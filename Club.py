# -*- coding: utf-8 -*-

from Joueur import Joueur

""" Ce module contient la définition de la classe Club permettant la création des équipes """


class Club:
    def __init__(self, nom_club, niveau, noms_joueurs):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison (initialisés à 0)
        """
        self.noms_joueurs = noms_joueurs
        self.nom_club = nom_club
        self.Joueurs = []
        for nom in noms_joueurs:
            self.Joueurs.append(Joueur(nom))
        # On attribue un niveau à chaque club (en fonction des résultats de cette année)
        self.niveau = niveau
        self.points = 0
        self.buts_marques = 0

    def __str__(self):
        """On définit __str__ la méthode retournant le nom de clubs, leur nombre de points et le nombre de buts marqués
        sous forme de dataframe
        """
        return f"Noms des clubs : {self.nom_club}, Nombre de points : {self.points}, Buts marqués : {self.buts_marques}"