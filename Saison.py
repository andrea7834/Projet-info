# -*- coding: utf-8 -*-

import Club, Journee
import numpy as np

""" Ce module contient la définition de la classe principale Saison servant à créer le championnat """

class Saison(Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison
        Input et Output : None
        """
        super().__init__()
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

    clubs = Club.Club()
    saison = Saison()
    print(saison.classement_final())