# -*- coding: utf-8 -*-

import random
import numpy as np
from math import exp
from math import factorial

"""
Ce module contient la définition des classe Joueurs et Clubs permettant la création des équipes
"""

class Club(list):
    def __init__(self, nom, niveau, lieu):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison

        Input : nom du club (str)
                  niveau (float)
                  lieu (str)
        Output : None
        """
        super().__init__()
        self.nom = nom
        self.niveau = niveau
        self.lieu = lieu
        self.joueurs = []
        self.points = 0
        self.buts_marques = 0

    def ajouter_joueur(self, joueur):
        """On définit la méthode ajouter_joueur permettant d'ajouter un joueur dans l'équipe du club

        Input : nom du joueur appartennat au club (str)
        Output : None
        """
        self.joueurs.append(joueur)

    def jouer_match(self, adversaire, buts_marques, buts_encaisses):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs

        Inputs : adversaire (str)
                    buts_marques (int)
                    buts_encaisses (int)
        Output : None
        """
        if buts_marques > buts_encaisses:
            self.points += 3
        elif buts_marques < buts_encaisses:
            adversaire.points += 3
        elif buts_marques == buts_encaisses:
            self.points += 1
            adversaire.points += 1

        self.buts_marques += buts_marques
        adversaire.buts_marques += buts_encaisses



    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom du club
        Input : None
        Output : None
        """
        return self.nom


class Joueur:
    def __init__(self, nom):
        """On définit la classe Joueur définissant les caractéristiques d'un joueur

        Input  :  nom du joueur (str)
                    note du joueur (float)
        Output : None
        """
        self.nom = nom
        self.note = 0
        self.buts_marques = 0

    def marquer_but(self):
        """On définit la méthode marquer_but mettant à jour le nombre de buts marqués
        par le joueur lorsqu'il marque un but

        Input : None
        Output : None
        """
        self.buts_marques += 1

    def actualiser_note(self):
        """On définit la méthode actualiser_note mettant à jour la note du joueur
            lorsqu'il marque un but

            Input : None
            Output : None
            """
        self.note = np.max(20.0, self.note + 20*random.random())
        # Lorsque le joueur a atteint la note de 20, il ne peut pas avoir plus

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom du joueur
            Input : None
            Output : None
            """
        return self.nom