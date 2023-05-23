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
        self.journee1 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(1))
        self.journee2 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(2))
        self.journee3 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(3))
        self.journee4 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(4))
        self.journee5 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(5))
        self.journee6 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(6))
        self.journee7 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(7))
        self.journee8 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(8))
        self.journee9 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(9))
        self.journee10 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(10))
        self.journee11 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(11))
        self.journee12 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(12))
        self.journee13 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(13))
        self.journee14 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(14))
        self.journee15 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(15))
        self.journee16 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(16))
        self.journee17 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(17))
        self.journee18 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(18))
        self.journee19 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(19))
        self.journee20 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(20))
        self.journee21 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(21))
        self.journee22 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(22))
        self.journee23 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(23))
        self.journee24 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(24))
        self.journee25 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(25))
        self.journee26 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(26))
        self.journee27 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(27))
        self.journee28 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(28))
        self.journee29 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(29))
        self.journee30 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(30))
        self.journee31 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(31))
        self.journee32 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(32))
        self.journee33 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(33))
        self.journee34 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(34))
        self.journee35 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(35))
        self.journee36 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(36))
        self.journee37 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(37))
        self.journee38 = Journee.Journee(noms_clubs, noms_joueurs, niveaux).classement_journee().to_csv("jour{0}.csv".format(38))

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


if __name__ == "__main__":
    saison = Saison()
    # for i in range(38):
    #     res = saison.classement_journee()
    #     res.to_csv("jour{0}.csv".format(i+1))
    print(saison.classement_final())


## Nombre de points = nombre de buts (on veut pas)
## Stockage / appel à la fonction classement_journee
## Le nombre de points final de chaque club ne s'actualise pas correctement