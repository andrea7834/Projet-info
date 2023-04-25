# -*- coding: utf-8 -*-

import random
import numpy as np
import pandas as pd
import Joueur

""" Ce module contient la définition de la classe Club permettant la création des équipes """

class Club(Joueur):
    def __init__(self):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison
        Input et Output : None
        """
        super().__init__()
        self.noms_clubs = []
        self.niveau = []
        self.joueurs = []
        self.points = np.zeros(20)
        self.buts_marques = np.zeros(20)
        self.dom_ext = np.eye(20)  # On définit une matrice pour les matchs joués à domicile ou à l'extérieur
        # Les lignes correspondent aux équipes jouant à domcile et les colonnes à celles jouant à l'extérieur

    def creer_club(self, nom_club, niveau, noms_joueurs):
        """On définit la méthode creer_club permettant d'ajouter un club
        Input : nom_club (str), le nom du club
                  niveau (float)
                  noms_joueurs (list)
        Output : None
        """
        self.noms_clubs.append(nom_club)
        self.niveau.append(niveau)
        self.joueurs.append(noms_joueurs)

    def gagner_match(self, nom_club):
        """On définit la méthode gagner_match augmentant le nombre de points de 3 de l'équipe gagnante
        Input : nom_club (str), le nom du club gagnant
        Output : None
        """
        i = self.noms_clubs.index(nom_club)
        self.points[i] += 3  # Lorsque le club gagne le match, son nombre de points augmente de 3 points

    def perdre_match(self, nom_club):
        """On définit la méthode perdre_match augmentant le nombre de points de 0 de l'équipe perdante
        Input : nom_club (str), le nom du club perdant
        Output : None
        """
        i = self.noms_clubs.index(nom_club)
        self.points[i] += 0  # Lorsque le club perd le match, son nombre de points n'augmente pas

    def match_nul(self, nom_club_a, nom_club_b):
        """On définit la méthode match_nul augmentant le nombre de points de 1 des deux équipes
        Input : nom_club_a (str)
                  nom_club_b (str)
        Output : None
        """
        i = self.noms_clubs.index(nom_club_a)
        j = self.noms_clubs.index(nom_club_b)
        self.points[i] += 1  # Lorsque le match est nul, le nombre de points de chacun des clubs augmente de 1.
        self.points[j] += 1

    def rencontre_possible(self, equipe_a, equipe_b):
        i = self.noms_clubs.index(equipe_a)
        j = self.noms_clubs.index(equipe_b)
        if self.dom_ext[i][j] == 1:
            return False
        else:
            return True

    def jouer_un_match(self, equipe_a, equipe_b):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs
        Inputs : equipe_a (str)
                    equipe_b (str)
        Output : None
        """
        i = self.noms_clubs.index(equipe_a)
        j = self.noms_clubs.index(equipe_b)

        if not self.rencontre_possible(equipe_a, equipe_b):
            return "Cette rencontre a déjà eu lieu"
        else:
            self.dom_ext[i][j] = 1

            # On définit le nombre de buts marqués et encaissés en fonction du niveau de l'équipe
            buts_marques_a = int(self.niveau * np.random.randint(0, 5))
            buts_marques_b = int(self.niveau * np.random.randint(0, 5))

            # On actualise le nombre de points et de buts marqués de chaque équipe
            if buts_marques_a > buts_marques_b:
                self.gagner_match(equipe_a)
                self.perdre_match(equipe_b)
            elif buts_marques_a < buts_marques_b:
                self.gagner_match(equipe_b)
                self.perdre_match(equipe_a)
            elif buts_marques_a < buts_marques_b:
                self.match_nul(equipe_a, equipe_b)
            self.buts_marques[i] += buts_marques_a
            self.buts_marques[j] += buts_marques_b

            for nb_butsA in range(buts_marques_a + 1):
                indice_buteur = np.random.randint(1, 12)
                # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
                buteur = self.noms_joueurs[i + indice_buteur]
                self.marquer_but(buteur)
                self.actualiser_note(buteur)

            for nb_butsB in range(buts_marques_b + 1):
                indice_buteur = np.random.randint(1, 12)
                # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
                buteur = self.noms_joueurs[j + indice_buteur]
                self.marquer_but(buteur)
                self.actualiser_note(buteur)

            return buts_marques_a, buts_marques_b

    def __str__(self):
        """On définit __str__ la méthode retournant le nom de clubs, leur nombre de poinst et le nombre de buts marqués sous forme de dataframe
        Input et Output : None
        """
        return pd.DataFrame({"Noms des clubs" : self.noms_clubs, 'Nombre de points' : self.points, "Buts marqués" : self.buts_marques})