# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

from Journee import Journee

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """


class Saison(Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison """
        self.nom = "Ligue 1"
        self.nb_jours_total = 38
        super().__init__()
        journee = Journee()
        for i in range(self.nb_jours_total):
            classement_journee = journee.classement_journee()
            classement_journee.to_excel("jour{0}.xlsx".format(i+1))
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
        self.journee38 = journee.classement_journee().to_excel("jour{0}.xlsx".format(38))
        equipes = []
        scores = []
        scores_dom = []
        scores_exte = []
        for club in self.Clubs:
            equipes.append(club.nom_club)
            scores.append(club.points)
            scores_dom.append(club.points_dom)
            scores
        dico = {"Clubs":equipes, "Points" : scores}
        # equipes = np.array(equipes)
        # scores = np.array(scores)
        self.fin = pd.DataFrame(data=dico)
        self.fin = self.fin.sort_values(by=['Points'], ascending=False)
        self.fin.to_excel("classement_final")


    def classement_final(self):
        return self.fin


if __name__ == "__main__":
    saison = Saison()
    # results = saison.classement_final()
    # print(results)