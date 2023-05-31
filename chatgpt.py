import numpy as np
import random
import pandas as pd

class Joueur:
    def __init__(self, nom_joueur):
        """On définit la classe Joueur définissant les caractéristiques du joueur"""
        self.nom_joueur = nom_joueur
        self.note = 0
        self.buts_marques_j = 0

    def marquer_but(self):
        """On définit la méthode marquer_but mettant à jour la note et le nombre de buts marqués
        par le joueur lorsqu'il marque un but."""
        # La note ne peut pas dépasser 20 et on l'augmente à chaque but
        self.note = np.maximum(self.note + random.random(), 20.0)
        self.buts_marques_j += 1

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom du joueur,
        sa note et son nombre de buts qu'il a marqué"""
        return f"Nom du joueur : {self.nom_joueur}, Note : {self.note}, Buts marqués : {self.buts_marques_j}"

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
        # On attribue un niveau à chaque club (en fonction des résultats de cette année