# -*- coding: utf-8 -*-

import random
import numpy as np
import pandas as pd

""" Ce module contient la définition de la classe Joueur permettant la création des joueurs """

class Joueur(list):
    def __init__(self):
        """On définit la classe Joueur définissant les caractéristiques des joueurs
        On initialise tout par des listes vides
        Input et Output : None
        """
        super().__init__()
        self.noms_joueurs, self.notes, self.buts_marques = [], [], []

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
        Input et Output : None
        """
        i = self.noms_joueurs.index(nom_joueur)  # On cherche l'indice du joueur dans la liste de l'équipe
        self.buts_marques[i] += 1      # On augmente de 1 but le nombre de buts marqués par le joueur

    def actualiser_note(self, nom_joueur):
        """On définit la méthode actualiser_note mettant à jour la note du joueur lorsqu'il marque un but
        Input et Output : None
        """
        i = self.noms_joueurs.index(nom_joueur)
        self.notes[i] = np.max(20.0, self.notes[i] + 20 * random.random())
        # Lorsque le joueur a atteint la note de 20, il ne peut pas avoir plus

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec les noms des joueurs
            Input et Output : None
        """
        return pd.DataFrame({"Noms des joueurs" : self.noms_joueurs, 'Notes' : self.notes, "Buts marqués" : self.buts_marques})