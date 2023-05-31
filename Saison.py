# -*- coding: utf-8 -*-
import time

import pandas as pd
import matplotlib.pyplot as plt

from Journee import Journee

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """


class Saison(Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison """
        self.nom = "Ligue 1"
        self.nb_jours_total = 38
        super().__init__()
        journee = Journee()
        self.journee1 = journee.classement_journee().to_excel("jour{0}.xlsx".format(1))
        self.journee2 = journee.classement_journee().to_excel("jour{0}.xlsx".format(2))
        self.journee3 = journee.classement_journee().to_excel("jour{0}.xlsx".format(3))
        self.journee4 = journee.classement_journee().to_excel("jour{0}.xlsx".format(4))
        self.journee5 = journee.classement_journee().to_excel("jour{0}.xlsx".format(5))
        self.journee6 = journee.classement_journee().to_excel("jour{0}.xlsx".format(6))
        self.journee7 = journee.classement_journee().to_excel("jour{0}.xlsx".format(7))
        self.journee8 = journee.classement_journee().to_excel("jour{0}.xlsx".format(8))
        self.journee9 = journee.classement_journee().to_excel("jour{0}.xlsx".format(9))
        self.journee10 = journee.classement_journee().to_excel("jour{0}.xlsx".format(10))
        self.journee11 = journee.classement_journee().to_excel("jour{0}.xlsx".format(11))
        self.journee12 = journee.classement_journee().to_excel("jour{0}.xlsx".format(12))
        self.journee13 = journee.classement_journee().to_excel("jour{0}.xlsx".format(13))
        self.journee14 = journee.classement_journee().to_excel("jour{0}.xlsx".format(14))
        self.journee15 = journee.classement_journee().to_excel("jour{0}.xlsx".format(15))
        self.journee16 = journee.classement_journee().to_excel("jour{0}.xlsx".format(16))
        self.journee17 = journee.classement_journee().to_excel("jour{0}.xlsx".format(17))
        self.journee18 = journee.classement_journee().to_excel("jour{0}.xlsx".format(18))
        self.journee19 = journee.classement_journee().to_excel("jour{0}.xlsx".format(19))
        self.journee20 = journee.classement_journee().to_excel("jour{0}.xlsx".format(20))
        self.journee21 = journee.classement_journee().to_excel("jour{0}.xlsx".format(21))
        self.journee22 = journee.classement_journee().to_excel("jour{0}.xlsx".format(22))
        self.journee23 = journee.classement_journee().to_excel("jour{0}.xlsx".format(23))
        self.journee24 = journee.classement_journee().to_excel("jour{0}.xlsx".format(24))
        self.journee25 = journee.classement_journee().to_excel("jour{0}.xlsx".format(25))
        self.journee26 = journee.classement_journee().to_excel("jour{0}.xlsx".format(26))
        self.journee27 = journee.classement_journee().to_excel("jour{0}.xlsx".format(27))
        self.journee28 = journee.classement_journee().to_excel("jour{0}.xlsx".format(28))
        self.journee29 = journee.classement_journee().to_excel("jour{0}.xlsx".format(29))
        self.journee30 = journee.classement_journee().to_excel("jour{0}.xlsx".format(30))
        self.journee31 = journee.classement_journee().to_excel("jour{0}.xlsx".format(31))
        self.journee32 = journee.classement_journee().to_excel("jour{0}.xlsx".format(32))
        self.journee33 = journee.classement_journee().to_excel("jour{0}.xlsx".format(33))
        self.journee34 = journee.classement_journee().to_excel("jour{0}.xlsx".format(34))
        self.journee35 = journee.classement_journee().to_excel("jour{0}.xlsx".format(35))
        self.journee36 = journee.classement_journee().to_excel("jour{0}.xlsx".format(36))
        self.journee37 = journee.classement_journee().to_excel("jour{0}.xlsx".format(37))
        self.journee38 = journee.classement_journee()
        self.journee38.to_excel("jour{0}.xlsx".format(38))
        print(self.journee38)
        # equipes = []
        # scores = []
        #
        # for club in self.Clubs:
        #     equipes.append(club.nom_club)
        #     scores.append(club.points)
        #     scores_dom.append(club.points_dom)
        #     scores_exte.append(club.points_exte)
        # dico = {"Clubs":equipes, "Points" : scores, "Points à domicile":scores_dom, "Points à l'extérieur":scores_exte}
        # self.fin = pd.DataFrame(data=dico)
        # self.fin = self.fin.sort_values(by=['Points', "Points à domicile", "Points à l'extérieur"], ascending=False)
        # self.fin.to_excel("classement_final.xlsx")


    # def classement_final(self):
    #     return self.fin

class Analyse(Saison):

    '''Cette classe va permettre l'analyse des résultats des clubs'''
    def clubs_avantage_domicile(self):

        """Retourne les clubs pour lesquels jouer à domicile profite le plus"""

        club_avantages = []
        for club in self.Clubs:
            avantage_domicile = club.points_dom() - club.points_exte()
            club_avantages.append((club.nom, avantage_domicile))
        club_avantages = sorted(club_avantages, key=lambda x: x[1], reverse=True)

        return (avantage_domicile,club_avantages)

    def afficher(self):

        valeurs, categories = Analyse().clubs_avantage_domicile()

        plt.bar(categories, valeurs)

        plt.xlabel('Equipes')
        plt.ylabel('Avantages domiciles')
        plt.title('Les équipes avantagées par les matchs à domicile')

        plt.show()



if __name__ == "__main__":
    saison = Saison()
    print(saison.journee38)
    # equipes = []
    # scores = []
    # # scores_dom = []
    # # scores_exte = []
    # for club in saison.Clubs:
    #     equipes.append(club.nom_club)
    #     scores.append(club.points)
    #     scores_dom.append(club.points_dom)
    #     scores_exte.append(club.points_exte)
    # dico = {"Clubs": equipes, "Points": scores, "Points à domicile": scores_dom, "Points à l'extérieur": scores_exte}
    # fin = pd.DataFrame(data=dico)
    # fin = fin.sort_values(by=['Points', "Points à domicile", "Points à l'extérieur"], ascending=False)
    # fin.to_excel("classement_final.xlsx")