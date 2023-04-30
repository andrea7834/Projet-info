# -*- coding: utf-8 -*-

import random
import numpy as np

""" Ce module contient la définition de la classe Joueur permettant la création d'un joueur """

class Joueur():
    def __init__(self, nom_joueur, note=0, buts_marques=0):
        """On définit la classe Joueur définissant les caractéristiques du joueur"""
        self.nom_joueur, self.note, self.buts_marques = nom_joueur, note, buts_marques

    def marquer_but(self):
        """On définit la méthode marquer_but mettant à jour la note et le nombre de buts marqués
        par le joueur lorsqu'il marque un but."""
        # La note ne peut pas dépasser 20 et on l'augmente à chaque but
        self.note = np.maximum(20.0, self.note + 20 * random.random())
        self.buts_marques += 1

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom du joueur,
        sa note et le nombre de buts qu'il a marqué"""
        return f"Nom du joueur : {self.nom_joueur}, Note : {self.note}, Buts marqués :{self.buts_marques}"