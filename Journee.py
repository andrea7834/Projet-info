# -*- coding: utf-8 -*-

import Club
import numpy as np

""" Ce module contient la définition de la classe Journée simulant une journée de championnat """


class Journee(Club):

    def __init__(self, noms_clubs, noms_joueurs):
        """On définit la classe Journee comprenant les rencontres de la journée """
        for club in noms_clubs:
            super().__init__(club)
        super().__init__(noms_clubs, noms_joueurs)
        self.nb_rencontres_par_jour = 10 # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour

    def jouer_journee(self):
        """On définit la méthode jouer_journee récapitulant les résultats des rencontres de la journée """
        self.nb_jours_restants -= 1
        nb_rencontres = self.nb_rencontres_par_jour
        equipes_dom, equipes_ext, buts_dom, buts_ext, pts_dom, pts_ext, buteurs_dom, buteurs_ext = [], [], [], [], [], [], [], []

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
                            buteurs_dom.append(self.jouer_un_match(equipes[i], equipes[j])[2])
                            buteurs_ext.append(self.jouer_un_match(equipes[i], equipes[j])[3])
                            nb_rencontres -= 1
            equipes_dom = np.array(equipes_dom).reshape(10, 1)
            equipes_ext = np.array(equipes_ext).reshape(10, 1)
            buts_dom = np.array(buts_dom).reshape(10, 1)
            buts_ext = np.array(buts_ext).reshape(10, 1)
            pts_dom = np.array(buts_dom).reshape(10, 1)
            pts_ext = np.array(buts_ext).reshape(10, 1)
            buteurs_dom = np.array(buteurs_dom).reshape(10, 1)
            buteurs_ext = np.array(buteurs_ext).reshape(10, 1)

            return np.array(equipes_dom, buts_dom, pts_dom, buteurs_dom), np.array(equipes_ext, buts_ext, pts_ext, buteurs_ext)

    def classement_journee(self):
        """ On définit la méthode classement_journee qui donne le classement d'une journée"""
        tab_dom, tab_ext = self.jouer_journee()
        tab = np.concatenate((tab_dom, tab_ext), axis=0)
        classement_journee = tab[np.argsort(tab[:, 2]), :] # On trie selon le nombre de points gagnés
        return classement_journee

    def classement_date(self, no_jour):
        classement_date = [self.noms_clubs, [0 for i in range(20)], [0 for i in range(20)]]
        for i in range(no_jour):    # Classement au jour n° no_jour
            classement_jour = self.classement_journee()
            for nom in self.noms_clubs:
                j = classement_jour[0].index(nom)  # Indice du club dans le classement du jour
                k = classement_date[0].index(nom)  # Indice du club dans le classement à la date t
                classement_date[1][k] += classement_jour[1][j]  # On actualise le nb_buts
                classement_date[2][k] += classement_jour[2][j]  # On actualise le nb_points
        tab = np.array(classement_date)
        classement_date = tab[np.argsort(tab[:, 2]), :] # On trie selon le nombre de points gagnés
        return classement_date

    def __str__(self, date):
        return str(self.classement_date(date))