# -*- coding: utf-8 -*-

import random
from abc import ABCMeta
import numpy as np

""" Ce module contient la définition de la classe Joueur permettant la création d'un joueur """

class Joueur(metaclass=ABCMeta):
    def __init__(self):
        """On définit la classe Joueur définissant les caractéristiques du joueur"""
        self.noms_joueurs = self.noms_des_joueurs()
        self.note = np.zeros((220, 1))
        self.buts_marques = np.zeros((220, 1))
        self.tab = np.array(self.noms_joueurs, self.note, self.buts_marques)

    def noms_des_joueurs(self):
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
        return  noms_joueurs

    def marquer_but(self):
        """On définit la méthode marquer_but mettant à jour la note et le nombre de buts marqués
        par le joueur lorsqu'il marque un but."""
        # La note ne peut pas dépasser 20 et on l'augmente à chaque but
        self.note = np.maximum(20.0, self.note + 20 * random.random())
        self.buts_marques += 1

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec les noms des joueurs,
        ses notes et leur nombre de buts qu'ils ont marqué"""
        for i in range(len(self.noms_joueurs[:][0]) + 1):
            return f"Nom du joueur : {self.noms_joueurs[i]}, Note : {self.note[i]}, Buts marqués :{self.buts_marques[i]}"

if __name__ == "__main__":