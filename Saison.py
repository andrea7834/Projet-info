# -*- coding: utf-8 -*-

import Journee
import numpy as np
import pandas as pd

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """


class Saison(Journee.Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison """
        noms_clubs = self.extraire_clubs()
        noms_joueurs = self.extraire_joueurs()
        niveaux = self.niveaux()
        super().__init__(noms_clubs, noms_joueurs, niveaux)
        self.nom = "Ligue 1"
        self.nb_jours_total = 38

    def classement_final(self):
        return self.classement_date(self.nb_jours_total)

    def extraire_joueurs(self):
        """Extraction de la liste des joueurs"""
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
        return noms_joueurs

    def extraire_clubs(self):
        """Extraction de la liste des clubs"""
        fichier = open("noms_clubs.txt", 'r')
        noms_clubs = []
        fichier.seek(0)  # Mettre le curseur au début du fichier
        i = 0
        for nom_club in fichier:  # Il y a un club par ligne
            nom_club = nom_club.strip(" \n")
            noms_clubs.append(nom_club)
            i += 1
        fichier.close()  # Fermeture du fichier après lecture
        return noms_clubs

    def niveaux(self):
        niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                       3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                       3.75, 1, 2.25, 0.75]).reshape((20, 1))
        return niveaux


if __name__ == "__main__":
    saison = Saison()
    noms_clubs = saison.extraire_clubs()
    noms_joueurs = saison.extraire_joueurs()
    niveaux = saison.niveaux
    journee = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee()
    print(journee)