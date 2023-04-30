# -*- coding: utf-8 -*-

import Joueur, Club, Journee
import numpy as np

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """

class Saison(Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison
        Input et Output : None
        """
        super().__init__()
        self.nom = "Ligue 1"
        self.classement_final = np.array(self.noms_clubs, self.points, self.buts_marques)
        self.nb_jours_total = 38
        self.nb_journees = 0

    def calendrier(self):
        nb_jours = self.nb_jours_restants
        nb_col = 7 # Du lundi au dimanche
        nb_lignes = int(nb_jours / nb_col) + 1
        calend = np.empty((nb_lignes, nb_col))
        for i in range(0, nb_lignes):
            for j in range(0, nb_col):
                calend[i][j] = int(i * nb_col + j + 1)
        calend[-1][4:] = 0
        return calend



    def matchs_saison(self):
        """ On définit la méthode jouer_saison le récapitulatif des matchs joués sur la saison"""
        matchs = []
        for i in range(self.nb_jours_total + 1):
            matchs_journee = self.jouer_journee()
            matchs.append(matchs_journee)
        return matchs

    def classement_journee(self, date):
        """ On définit la méthode classement_journee qui donne le récapitulatif des matchs joués en une journée"""
        tab_dom, tab_ext = self.simuler_journee()
        scores_totaux = np.array(tab_dom, tab_ext).reshape((20, 2))  # On ajoute les résultats de la journée dans le récap final
        classement_journee = self.tri(scores_totaux)
        return classement_journee


if __name__ == "__main__":

    # Extraction de la liste des clubs
    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    for club in fichier:  # Il y a un club par ligne
        club = club.strip(" \n")
        noms_clubs.append(club)
    fichier.close()  # Fermeture du fichier après lecture

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

    # On attribue un niveau à chaque club (en fonction des résultats de cette année)
    niveau_clubs = [0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
              3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
              3.75, 1, 2.25, 0.75]

    clubs = Club.Club(noms_clubs, niveau_clubs, noms_joueurs)

    saison = Saison()
    print(saison.jouer_saison())