# -*- coding: utf-8 -*-

import Club
import numpy as np

""" Ce module contient la définition de la classe Journée simulant une journée de championnat """


class Journee(Club):
    nb_journee = 0

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée

        Input : None
        Output : None
        """
        super().__init__()
        self.nb_rencontres_par_jour = 10
        # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        Journee.nb_journee += 1
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour

    def rencontres_journee(self):
        """On définit la méthode rencontres_journee décidant des rencontres de la journée
        Inputs : None
        Output : None
        """
        self.nb_jours_restants -= 1
        nb_rencontres = self.nb_rencontres_par_jour
        equipes_dom, equipes_ext, buts_dom, buts_ext = [], [], [], []

        if self.nb_jours_restants > 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

        # On choisit les rencontres de la journée
            while nb_rencontres > 0:
                for i in range(len(equipes) + 1):
                    for j in range(len(equipes) + 1):
                        # On vérifie que ces deux équipes ne se sont pas affrontées au domicile de l'équipe i
                        if self.rencontre_possible(equipes[j], equipes[i]):
                            equipes_dom.append(equipes[i])
                            equipes_ext.append(equipes[j])
                            buts_dom.append(self.jouer_match(equipes[i], equipes[j])[0])
                            buts_ext.append(self.jouer_match(equipes[i], equipes[j])[1])
                            nb_rencontres -= 1
            equipes_dom = np.array(equipes_dom).reshape(10, 1)
            equipes_ext = np.array(equipes_ext).reshape(10, 1)
            buts_dom = np.array(buts_dom).reshape(10, 1)
            buts_ext = np.array(buts_ext).reshape(10, 1)

            return np.array(equipes_dom, buts_dom), np.array(equipes_ext, buts_ext)