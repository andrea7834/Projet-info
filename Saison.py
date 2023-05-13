# -*- coding: utf-8 -*-

import Club, Journee, Joueur
import numpy as np

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """


class Saison(Journee.Journee):
    def __init__(self, noms_clubs, noms_joueurs, niveaux):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison """
        super().__init__(noms_clubs, noms_joueurs, niveaux)
        self.nom = "Ligue 1"
        self.nb_jours_total = 38
        self.recommencer_tournoi()

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

    niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                       3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                       3.75, 1, 2.25, 0.75]).reshape((20, 1))

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
            # joueur = Joueur.Joueur(nom)
            # print(joueur)
        noms_joueurs.append(equipe)
    fichier.close()  # Fermeture du fichier après lecture
    # noms_joueurs = np.array(noms_joueurs).reshape((20,))

    # Extraction de la liste des clubs
    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    i = 0
    for nom_club in fichier:  # Il y a un club par ligne
        nom_club = nom_club.strip(" \n")
        noms_clubs.append(nom_club)
        # club = Club.Club(nom_club, niveau[i], noms_joueurs[i])
        # print(club)
        i += 1
    fichier.close()  # Fermeture du fichier après lecture

    # journee = Journee.Journee(noms_clubs, noms_joueurs, niveaux)
    # test = journee.jouer_un_match("PSG", "OM")
    # print(test)

    journee = Journee.Journee(noms_clubs, noms_joueurs, niveaux).jouer_journee()
    print(journee)

    #saison = Saison.matchs_saison(self)