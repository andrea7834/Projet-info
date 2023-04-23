# -*- coding: utf-8 -*-

import random
import numpy as np
from math import exp
from math import factorial

"""
Ce module contient la définition des classe Joueurs et Clubs permettant la création des équipes
"""

class Joueur(list):
    def __init__(self):
        """On définit la classe Joueur définissant les caractéristiques des joueurs
        On initialise tout par des listes vides

        Input : None
        Output : None
        """
        super().__init__()
        self.noms_joueurs = []
        self.notes = []
        self.buts_marques = []

    @property
    def noms_joueurs(self):
        return self.noms_joueurs

    @noms_joueurs.setter
    def noms_joueurs(self, value):
        self.noms_joueurs.append(value)

    def creer_joueur(self, nom_joueur):
        """On crée un nouveau joueur dans la liste.
        Au départ, sa note est de 0 et son nombre de buts marqués aussi.

        Input : nom_joueur (str)
        Output : None
        """
        self.noms_joueurs.append(nom_joueur)
        self.notes.append(0)
        self.buts_marques.append(0)

    def marquer_but(self, nom_joueur):
        """On définit la méthode marquer_but mettant à jour le nombre de buts marqués
        par le joueur lorsqu'il marque un but.

        Input : None
        Output : None
        """
        i = self.noms_joueurs().index(nom_joueur)
        self.buts_marques[i] += 1      # On augmente de 1 but le nombre de buts marqués par le joueur

    def actualiser_note(self, nom_joueur):
        """On définit la méthode actualiser_note mettant à jour la note du joueur
            lorsqu'il marque un but

            Input : None
            Output : None
            """
        i = self.noms_joueurs().index(nom_joueur)
        self.notes[i] = np.max(20.0, self.notes[i] + 20 * random.random())
        # Lorsque le joueur a atteint la note de 20, il ne peut pas avoir plus


    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec les noms des joueurs
            Input : None
            Output : None
            """
        return self.noms_joueurs()


class Club(Joueur):
    def __init__(self):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison

        Input : None
        Output : None
        """
        super().__init__()
        self.noms_clubs = []
        self.niveau = []
        self.lieux = []
        self.joueurs = []
        self.points = []
        self.buts_marques = []
        self.adversaires_a_domicile = []
        self.adversaires_a_l_ext = []

    def creer_club(self, nom_club, niveau, lieu, noms_joueurs):
        """On définit la méthode gagner_match augmentant le nombre de points de 3 de l'équipe gagnante

            Input : nom_club (str), le nom du club
                      niveau (float)
                      lieu (str)
                      noms_joueurs (list)
            Output : None
        """
        self.noms_clubs.append(nom_club)
        self.niveau.append(niveau)
        self.lieux.append(lieu)
        self.joueurs.append(noms_joueurs)

    def gagner_match(self, nom_club):
        """On définit la méthode gagner_match augmentant le nombre de points de 3 de l'équipe gagnante

            Input : nom_club (str), le nom du club gagnant
            Output : None
        """
        i = self.noms_clubs.index(nom_club)
        self.points[i] += 3  # Lorsque le club gagne le match, son nombre de points augmente de 3 points

    def perdre_match(self, nom_club):
        """On définit la méthode perdre_match augmentant le nombre de points de 0 de l'équipe perdante

            Input : nom_club (str), le nom du club perdant
            Output : None
        """
        i = self.noms_clubs.index(nom_club)
        self.points[i] += 0  # Lorsque le club perd le match, son nombre de points n'augmente pas

    def match_nul(self, nom_clubA, nom_clubB):
        """On définit la méthode match_nul augmentant le nombre de points de 1 des deux équipes

            Input : nom_clubA (str)
                      nom_clubB (str)
            Output : None
        """
        i = self.noms_clubs.index(nom_clubA)
        j = self.noms_clubs.index(nom_clubB)
        self.points[i] += 1  # Lorsque le match est nul, le nombre de points de chacun des clubs augmente de 1
        self.points[j] += 1


    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom des clubs
        Input : None
        Output : None
        """
        return self.noms_clubs