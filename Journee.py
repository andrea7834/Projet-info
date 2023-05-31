# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from Club import Club
from Joueur import Joueur

class Journee:

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée """
        self.noms_clubs = self.extraire_clubs()
        self.noms_joueurs = self.extraire_joueurs()
        self.niveaux = self.niveaux()
        # super().__init__()
        self.Clubs = []
        for i in range(20):
            self.Clubs.append(Club(self.noms_clubs[i], self.niveaux[i], self.noms_joueurs[i]))

        # self.points = np.zeros((20, ))
        # self.buts_marques = np.zeros((20, ))
        self.dom_ext = np.eye(20)  # On définit une matrice pour les matchs joués à domicile ou à l'extérieur
        # Les lignes correspondent aux équipes jouant à domicile et les colonnes à celles jouant à l'extérieur
        self.nb_rencontres_par_jour = 10 # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour

    # def points(self):
    #     return self.points

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
        # noms_joueurs = np.array(noms_joueurs)
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
        # noms_clubs = np.array(noms_clubs)
        return noms_clubs

    def niveaux(self):
        niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                       3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                       3.75, 1, 2.25, 0.75])
        return niveaux

    def jouer_un_match(self, equipe_a, equipe_b):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs
        Inputs : equipe_a (str) jouant à domicile
                    equipe_b (str) jouant à l'extérieur """

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
            else: # Il y a égalité
                points_a, points_b = 1, 1
            self.Clubs[i].points += points_a
            self.Clubs[j].points += points_b
            self.Clubs[i].buts_marques += buts_marques_a
            self.Clubs[i].buts_marques += buts_marques_b

            if buts_marques_a > 0:
                for nb_butsA in range(1, buts_marques_a + 1):
                    indice_buteur = np.random.randint(1, 11)
                    # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
                    buteur = self.noms_joueurs[i][indice_buteur]
                    buteurs_a.append(buteur)
                    joueur = self.Clubs[i].Joueurs[indice_buteur]
                    joueur.marquer_but()
            if buts_marques_b > 0:
                for nb_butsB in range(1, buts_marques_b + 1):
                    indice_buteur = np.random.randint(1, 11)
                    buteur = self.noms_joueurs[j][indice_buteur]
                    buteurs_b.append(buteur)
                    joueur = self.Clubs[j].Joueurs[indice_buteur]
                    joueur.marquer_but()

            return [buts_marques_a, buts_marques_b, points_a, points_b, buteurs_a, buteurs_b]

    def classement_journee(self):
        """On définit la méthode jouer_journee récapitulant les résultats des rencontres de la journée """
        self.nb_jours_restants -= 1
        nb_rencontres = self.nb_rencontres_par_jour
        equipes_dom, equipes_ext, buts_dom, buts_ext, pts_dom, pts_ext, buteurs_dom, buteurs_ext, indices = [], [], [], [], [], [], [], [], []

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

            equipes_dom = np.array([equipes_dom]).reshape(10, )
            equipes_ext = np.array([equipes_ext]).reshape(10, )
            buts_dom = np.array([buts_dom]).reshape(10, )
            buts_ext = np.array([buts_ext]).reshape(10, )
            pts_dom = np.array([buts_dom]).reshape(10, )
            pts_ext = np.array([buts_ext]).reshape(10, )
            buteurs_dom = np.array([buteurs_dom]).reshape(10, )
            buteurs_ext = np.array([buteurs_ext]).reshape(10, )

            dico = {"Points dom" : pts_dom, "Buteurs dom" : buteurs_dom, "Clubs à domicile" : equipes_dom, "Buts dom" : buts_dom,
                   "Buts exté": buts_ext, "Clubs à l'extérieur": equipes_ext, "Buteurs exté": buteurs_ext, "Points exté": pts_ext}

            res = pd.DataFrame(data=dico)
            res = res.sort_values(by=["Points dom", "Buts dom"], ascending=False)

            return res

if __name__ == "__main__":
    journee = Journee()
    score = journee.jouer_un_match("PSG", "OM")
    print(score)
    # joueurs = journee.extraire_joueurs()
    # clubs = journee.extraire_clubs()
    # niveaux = journee.niveaux()
    # print(joueurs)
    # print(clubs)
    # print(niveaux)