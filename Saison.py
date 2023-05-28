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
        self.journee1 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(1))
        self.journee2 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(2))
        self.journee3 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(3))
        self.journee4 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(4))
        self.journee5 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(5))
        self.journee6 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(6))
        self.journee7 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(7))
        self.journee8 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(8))
        self.journee9 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(9))
        self.journee10 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(10))
        self.journee11 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(11))
        self.journee12 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(12))
        self.journee13 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(13))
        self.journee14 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(14))
        self.journee15 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(15))
        self.journee16 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(16))
        self.journee17 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(17))
        self.journee18 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(18))
        self.journee19 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(19))
        self.journee20 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(20))
        self.journee21 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(21))
        self.journee22 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(22))
        self.journee23 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(23))
        self.journee24 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(24))
        self.journee25 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(25))
        self.journee26 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(26))
        self.journee27 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(27))
        self.journee28 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(28))
        self.journee29 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(29))
        self.journee30 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(30))
        self.journee31 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(31))
        self.journee32 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(32))
        self.journee33 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(33))
        self.journee34 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(34))
        self.journee35 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(35))
        self.journee36 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(36))
        self.journee37 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(37))
        self.journee38 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_excel("jour{0}.xlsx".format(38))

    def classement_final(self):
        dico = {"Clubs": self.noms_clubs, "Points": self.points}
        res = pd.DataFrame(data=dico)
        res.sort_values(by="Points", ascending=False)
        return res

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