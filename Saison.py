# -*- coding: utf-8 -*-

import Club, Journee, Joueur
import numpy as np

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """

class Saison(Journee):
    def __init__(self, noms_clubs, noms_joueurs):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison """
        super().__init__(noms_clubs, noms_clubs)
        self.nom = "Ligue 1"
        self.nb_jours_total = 38

    def matchs_saison(self):
        """ On définit la méthode matchs_saison le récapitulatif des matchs joués sur la saison"""
        matchs = []
        for i in range(self.nb_jours_total + 1):
            matchs_journee = self.jouer_journee()
            matchs.append(matchs_journee)
        return matchs

    def classement_final(self):
        return self.classement_date(self.nb_jours_total)


if __name__ == "__main__":

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

    # Extraction de la liste des clubs
    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    for club in fichier:  # Il y a un club par ligne
        club = club.strip(" \n")
        noms_clubs.append(club)
    fichier.close()  # Fermeture du fichier après lecture

    # joueurs = Joueur.Joueur
    # print(joueurs)
    # clubs = Club.Club()
    # print(clubs)
    # saison = Saison()
    # print(saison.classement_final())