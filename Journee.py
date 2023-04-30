# -*- coding: utf-8 -*-

import Club
import numpy as np

""" Ce module contient la définition de la classe Journée simulant une journée de championnat """


class Journee(Club):

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée """
        super().__init__()
        self.nb_rencontres_par_jour = 10
        # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        Journee.nb_journee += 1
        self.nb_jours_total = 38  # il y a 19 rencontres aller et 19 rencontres retour

    def jouer_journee(self):
        """On définit la méthode rencontres_journee décidant des rencontres de la journée """
        self.nb_jours_total -= 1
        nb_rencontres = self.nb_rencontres_par_jour
        equipes_dom, equipes_ext, buts_dom, buts_ext, pts_dom, pts_ext = [], [], [], [], [], []

        if self.nb_jours_restants > 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

        # On choisit les rencontres de la journée
            while nb_rencontres > 0:
                for i in range((len(equipes) + 1) // 2): # Equipes à domiciles (lignes)
                    for j in range((len(equipes) + 1) // 2, len(equipes) +1): # Equipes à l'extérieur (colonnes)
                        # On vérifie que ces deux équipes ne se sont pas affrontées au domicile de l'équipe i
                        if self.dom_ext[i][j] == 1:
                            equipes_dom.append(equipes[i])
                            equipes_ext.append(equipes[j])
                            buts_dom.append(self.jouer_un_match(equipes[i], equipes[j])[0][0])
                            buts_ext.append(self.jouer_un_match(equipes[i], equipes[j])[0][1])
                            pts_dom.append(self.jouer_un_match(equipes[i], equipes[j])[1][0])
                            pts_ext.append(self.jouer_un_match(equipes[i], equipes[j])[1][1])
                            nb_rencontres -= 1
            equipes_dom = np.array(equipes_dom).reshape(10, 1)
            equipes_ext = np.array(equipes_ext).reshape(10, 1)
            buts_dom = np.array(buts_dom).reshape(10, 1)
            buts_ext = np.array(buts_ext).reshape(10, 1)
            pts_dom = np.array(buts_dom).reshape(10, 1)
            pts_ext = np.array(buts_ext).reshape(10, 1)

            return np.array(equipes_dom, buts_dom, pts_dom), np.array(equipes_ext, buts_ext, pts_ext)

    def tri(self, tab):
        """ On définit la méthode tri permet de trier un tableau en fonction du nombre de points des équipes
        Input : tab (array)
        Output : tab_triee
        """
        tab1 = tab.copy()
        tab_trie = []

        while tab1:
            arg_min = np.argmin(tab[:, 1])  # On cherche l'indice du plus petit élément du tableau des scores
            tab_trie.append(tab1[arg_min])
            tab1.pop(arg_min)
        return tab_trie