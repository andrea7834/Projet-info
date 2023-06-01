# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import random
from Club import Club
from Joueur import Joueur


class Journee(list, Joueur, Club):

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée """
        super().__init__()
        noms_clubs = self.extraire_clubs()
        niveaux = self.niveaux()
        noms_joueurs = self.extraire_joueurs()
        self.noms_clubs = noms_clubs
        self.noms_joueurs = noms_joueurs
        self.niveaux = niveaux
        for i in range(len(self.noms_joueurs)):
            Joueur.__init__(self, nom_joueur=self.noms_joueurs[i])
        self.Clubs = []
        for i in range(20):
            Club.__init__(self, self.noms_clubs[i], self.niveaux[i], self.noms_joueurs[i])
            self.Clubs.append(Club(self.noms_clubs[i], self.niveaux[i], self.noms_joueurs[i]))
        self.dom_ext = np.eye(20)  # On définit une matrice pour les matchs joués à domicile ou à l'extérieur
        # Les lignes correspondent aux équipes jouant à domicile et les colonnes à celles jouant à l'extérieur
        self.nb_rencontres_par_jour = 10 # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour


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
        self.Clubs[i].points_dom += points_a
        self.Clubs[i].points += points_a
        self.Clubs[j].points_exte += points_b
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

        return [buts_marques_a, buts_marques_b, points_a, points_b, buteurs_a, buteurs_b, self.Clubs[i].points, self.Clubs[j].points]

    def classement_journee(self):
        """On définit la méthode jouer_journee récapitulant les résultats des rencontres de la journée """
        self.nb_jours_restants -= 1
        indices = [i for i in range(20)]
        dico = {"Score dom": [], "Points dom" : [], "Buteurs dom": [],
                "Clubs à domicile": [], "Buts dom": [],
                "Buts exté": [], "Clubs à l'extérieur": [], "Buteurs exté": [],
                "Points exté" : [], "Score exte": []}

        if self.nb_jours_restants >= 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

            n = 10
        # On choisit les rencontres de la journée
            while n >= 0 and indices != []:
                i = random.choice(indices)
                indices2 = indices.copy()
                indices2.remove(i)
                J = [k for k in indices2 if ((self.dom_ext[i][k] == 0) and (k != i))]
                if J != []:
                    j = random.choice(J)
                    self.dom_ext[i][j] = 1
                    n -= 1
                    indices.remove(i)
                    indices.remove(j)
                    [buts_marques_a, buts_marques_b, points_a, points_b, buteurs_a, buteurs_b, score_a, score_b] = self.jouer_un_match(equipes[i], equipes[j])
                    dico["Clubs à domicile"].append(equipes[i])
                    dico["Clubs à l'extérieur"].append(equipes[j])
                    dico["Buts dom"].append(buts_marques_a)
                    dico["Buts exté"].append(buts_marques_b)
                    dico["Points dom"].append(points_a)
                    dico["Points exté"].append(points_b)
                    dico["Buteurs dom"].append(buteurs_a)
                    dico["Buteurs exté"].append(buteurs_b)
                    dico["Score dom"].append(score_a)
                    dico["Score exte"].append(score_b)
            res = pd.DataFrame(data=dico)
            res = res.sort_values(by=["Buts dom", "Score dom"], ascending=False)
            return res