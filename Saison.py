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
        self.classement_saison = np.array(self.noms_clubs, self.points, self.buts_marques)
        self.nb_journees = 0

    def tri(self, tab):
        """ On définit la méthode tri permet de trier un tableau en fonction du nombre de points des équipes
        Input : tab (array)
        Output : None
        """
        tab1 = tab.copy()
        tab_trie = []
        while tab1:
            arg_min = np.argmin(tab[:, 1])
            tab_trie.append(tab1[arg_min])
            tab1.pop(arg_min)
        return tab_trie

    def jouer_journee(self):
        """ On définit la méthode jouer_journee qui donne le récapitulatif des matchs joués en une journée
        Input et Output : None
        """
        tab_dom, tab_ext = self.simuler_journee()
        scores_totaux = np.array(tab_dom, tab_ext).reshape((20, 2))
        classement_journee = self.tri(scores_totaux)
        return classement_journee

    def jouer_saison(self):
        """ On définit la méthode jouer_saison le récapitulatif des matchs joués sur la saison
        Input et Output : None
        """
        classement_saison = np.zeros((20, 3))  # Tableau récapitulatif de la saison
        classement_saison[:][0] = self.noms_clubs  # La 1ʳᵉ colonne correspond au nom des clubs
        classement_saison[:, 1] = self.points  # La 2ᵉ colonne correspond à leur nombre de points
        for i in range(self.nb_journees + 1):
            classement_journee = self.jouer_journee()
            j = 0
            for club in self.noms_clubs:
                indice = classement_journee[:, 0].index(club)
                classement_saison[j, 2] += [indice, 2]  # La 3ᵉ colonne correspond à leur nombre de buts
                j += 1
        return classement_saison


if __name__ == "__main__":

    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    for club in fichier:  # Il y a un club par ligne
        club = club.strip(" \n")
        noms_clubs.append(club)
    fichier.close()  # Fermeture du fichier après lecture

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

    niveau_clubs = [0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
              3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
              3.75, 1, 2.25, 0.75]

    joueurs = Joueur.Joueur()
    clubs = Club.Club()
    for i in range(len(noms_clubs)):
        for j in range(11):
            joueurs.creer_joueur(str(noms_joueurs[i][j]))
        clubs.creer_club(noms_clubs[i*11 : (i+1)*11], niveau_clubs[i*11 : (i+1)*11], noms_joueurs[i*11 : (i+1)*11])
    saison = Saison()
    print(saison.jouer_saison())