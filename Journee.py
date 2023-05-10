# -*- coding: utf-8 -*-

import Club, Joueur
import numpy as np
import pandas as pd

""" Ce module contient la définition de la classe Journée simulant une journée de championnat """


class Journee(Joueur.Joueur):

    def __init__(self, noms_clubs, noms_joueurs, niveaux):
        """On définit la classe Journee comprenant les rencontres de la journée """
        # for club in noms_clubs:
        #     super().__init__(club)
        # super().__init__(noms_clubs, noms_joueurs)
        for nom in noms_joueurs:
            super().__init__(nom)
        self.noms_clubs = noms_clubs
        self.noms_joueurs = noms_joueurs
        self.niveaux = niveaux
        self.points = np.zeros((20, 1))
        self.buts_marques = np.zeros((20, 1))
        self.dom_ext = np.eye(20)  # On définit une matrice pour les matchs joués à domicile ou à l'extérieur
        # Les lignes correspondent aux équipes jouant à domicile et les colonnes à celles jouant à l'extérieur
        self.nb_rencontres_par_jour = 10 # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour

    def jouer_un_match(self, equipe_a, equipe_b):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs
        Inputs : equipe_a (str) jouant à domicile
                    equipe_b (str) jouant à l'extérieur
        Output : None
        """

        buteurs_a, buteurs_b = [], []

        # On cherche l'indice de chaque club dans la liste des clubs pour accéder à ses caractéristiques
        i = self.noms_clubs.index(equipe_a)
        j = self.noms_clubs.index(equipe_b)

        if self.dom_ext[i][j] == 0:
            self.dom_ext[i][j] = 1

            # On définit le nombre de buts marqués et encaissés en fonction du niveau de l'équipe
            buts_marques_a = int(np.random.normal(self.niveaux, 1, 1) + 2)
            buts_marques_b = int(np.random.normal(self.niveaux, 1, 1) + 2)
            if buts_marques_a < 0:
                buts_marques_a = 0
            if buts_marques_b < 0:
                buts_marques_b = 0

            # On actualise le nombre de points et de buts marqués de chaque équipe
            # Lorsqu'un club gagne, il remporte 3 points, le perdant ne gagne aucun point.
            # S'il y a égalité, chaque équipe remporte 1 point
            points_a, points_b = 0, 0
            if buts_marques_a > buts_marques_b: # Le club A gagne et le club B perd
                points_a = 3
            elif buts_marques_a < buts_marques_b: # Le club B gagne et le club A perd
                points_b = 3
            elif buts_marques_a == buts_marques_b: # Il y a égalité
                points_a, points_b = 1, 1
            self.points[i] += points_a
            self.points[j] += points_b
            self.buts_marques[i] += buts_marques_a
            self.buts_marques[j] += buts_marques_b

            if buts_marques_a > 0:
                for nb_butsA in range(1, buts_marques_a + 1):
                    indice_buteur = np.random.randint(1, 11)
                    # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
                    buteur = self.noms_joueurs[i][indice_buteur]
                    buteurs_a.append(buteur)
                    joueur = Joueur.Joueur(buteur)
                    joueur.marquer_but()
            if buts_marques_b > 0:
                for nb_butsB in range(1, buts_marques_b + 1):
                    indice_buteur = np.random.randint(1, 11)
                    buteur = self.noms_joueurs[j][indice_buteur]
                    buteurs_b.append(buteur)
                    joueur = Joueur.Joueur(buteur)
                    joueur.marquer_but()

            return [buts_marques_a, buts_marques_b, points_a, points_b, buteurs_a, buteurs_b]

    def jouer_journee(self):
        """On définit la méthode jouer_journee récapitulant les résultats des rencontres de la journée """
        self.nb_jours_restants -= 1
        nb_rencontres = self.nb_rencontres_par_jour
        equipes_dom, equipes_ext, buts_dom, buts_ext, pts_dom, pts_ext, buteurs_dom, buteurs_ext, indices = [], [], [], [], [], [], [], [], [],

        if self.nb_jours_restants > 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

        # On choisit les rencontres de la journée
            while nb_rencontres > 0:
                i = np.random.randint(0, 20)
                j = np.random.randint(0, 20)

                if (i not in indices) and (j not in indices) and (i != j) and (self.dom_ext[i][j] == 0):
                    indices.append(i)
                    indices.append(j)
                    [buts_marques_a, buts_marques_b, points_a, points_b, buteurs_a, buteurs_b] = self.jouer_un_match(equipes[i], equipes[j])
                    equipes_dom.append(equipes[i])
                    equipes_ext.append(equipes[j])
                    buts_dom.append(buts_marques_a)
                    buts_ext.append(buts_marques_b)
                    pts_dom.append(points_a)
                    pts_ext.append(points_b)
                    buteurs_dom.append(buteurs_a)
                    buteurs_ext.append(buteurs_b)
                    nb_rencontres -= 1

            equipes_dom = np.array([equipes_dom]).reshape(10, 1)
            equipes_ext = np.array([equipes_ext]).reshape(10, 1)
            buts_dom = np.array([buts_dom]).reshape(10, 1)
            buts_ext = np.array([buts_ext]).reshape(10, 1)
            pts_dom = np.array([buts_dom]).reshape(10, 1)
            pts_ext = np.array([buts_ext]).reshape(10, 1)
            buteurs_dom = np.array([buteurs_dom]).reshape(10, 1)
            buteurs_ext = np.array([buteurs_ext]).reshape(10, 1)

            res_dom = np.array([equipes_dom.T, buts_dom.T, pts_dom.T, buteurs_dom.T])
            res_ext = np.array([equipes_ext, buts_ext, pts_ext, buteurs_ext])

            data_dom = {"Nom des clubs" : equipes_dom, "Buts" : buts_dom, "Points" : pts_dom, "Buteurs" : buteurs_dom}
            res = pd.DataFrame(data=data_dom)
            # res = pd.DataFrame(res_dom, index=["match1", "match2", "match3",
            #                                    "match4", "match5", "match6", "match7",
            #                                    "match8", "match9", "match10"],
            #                    columns=["Nom des clubs", "Buts", "Points", "Buteurs"])

            return res

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
                # classement_jour_liste = list(classement_jour[0][:])
                # classement_date_liste = list(classement_date[0][:])
                classement_jour_liste = []
                classement_date_liste = []
                for a in range(20):
                    classement_jour_liste.append(classement_jour[0][a])
                    classement_date_liste.append(classement_date[0][a])
                j = classement_jour_liste.index(nom)  # Indice du club dans le classement du jour
                k = classement_date_liste.index(nom)  # Indice du club dans le classement à la date t
                classement_date[1][k] += classement_jour[1][j]  # On actualise le nb_buts
                classement_date[2][k] += classement_jour[2][j]  # On actualise le nb_points
        tab = np.array(classement_date)
        classement_date = tab[np.argsort(tab[:, 2]), :] # On trie selon le nombre de points gagnés
        return classement_date