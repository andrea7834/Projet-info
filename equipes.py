# -*- coding: utf-8 -*-

import random
import numpy as np
from math import exp
from math import factorial

"""
Ce module contient la définition des classe Joueurs et Clubs permettant la création des équipes
"""

class Joueur:
    def __init__(self):
        """On définit la classe Joueur définissant les caractéristiques des joueurs
        On initialise tout par des listes vides

        Input : None
        Output : None
        """
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
    def __init__(self, noms_clubs, lieux, niveau):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison

        Input : nom du club (list)
                  lieux (list)
                  niveau (list)
        Output : None
        """
        super().__init__()
        self.noms_clubs = noms_clubs
        self.niveau = niveau
        self.lieux = lieux
        self.joueurs = []
        self.points = []
        self.buts_marques = []

    def ajouter_joueur(self):
        """On définit la méthode ajouter_joueur permettant d'ajouter un joueur dans l'équipe du club

        Input : None
        Output : None
        """
        for i in range(len(self.noms_clubs)):
            self.joueurs.append([self.noms_joueurs()[i : i+11]]) # chaque club possède 11 joueurs

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


    def jouer_match(self, equipeA, equipeB):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs

        Inputs : equipeA (str)
                    equipeB (str)
        Output : None
        """

        # On définit le nombre de buts marqués et encaissés en fonction du niveau de l'équipe
        buts_marquesA = int(self.niveau*np.random.randint(0, 5))
        buts_marquesB= int(self.niveau*np.random.randint(0, 5))

        # On actualise le nombre de points et de buts marqués de chaque équipe
        if buts_marquesA > buts_marquesB:
            self.gagner_match(equipeA)
            self.perdre_match(equipeB)
        elif buts_marquesA < buts_marquesB:
            self.gagner_match(equipeB)
            self.perdre_match(equipeA)
        elif buts_marquesA < buts_marquesB:
            self.match_nul(equipeA, equipeB)
        i = self.noms_clubs.index(equipeA)
        j = self.noms_clubs.index(equipeB)
        self.buts_marques[i] += buts_marquesA
        self.buts_marques[j] += buts_marquesB

        for nb_butsA in range(buts_marquesA + 1):
            indice_buteur = np.random.randint(1, 12)  # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
            buteur = self.noms_joueurs()[i+indice_buteur]
            self.marquer_but(buteur)
            self.actualiser_note(buteur)

        for nb_butsB in range(buts_marquesB + 1):
            indice_buteur = np.random.randint(1, 12)  # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
            buteur = self.noms_joueurs()[j+indice_buteur]
            self.marquer_but(buteur)
            self.actualiser_note(buteur)



    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom des clubs
        Input : None
        Output : None
        """
        return self.noms_clubs