# -*- coding: utf-8 -*-

import numpy as np
import Joueur

""" Ce module contient la définition de la classe Club permettant la création des équipes """

class Club(Joueur):
    def __init__(self, noms_clubs, niveau, noms_joueurs):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison (initialisés à 0)
        Inputs : noms_clubs (liste de str)
                    niveau (liste de float)
                    noms_joueurs (liste de listes de str)
        """
        super().__init__()
        self.noms_clubs, self.niveau, self.joueurs = noms_clubs, niveau, noms_joueurs
        self.points = np.zeros(20)
        self.buts_marques = np.zeros(20)
        self.dom_ext = np.eye(20)  # On définit une matrice pour les matchs joués à domicile ou à l'extérieur
        # Les lignes correspondent aux équipes jouant à domicile et les colonnes à celles jouant à l'extérieur

    def jouer_un_match(self, equipe_a, equipe_b):
        """On définit la méthode jouer_match ajoutant un match dans le tableau des matchs
        Inputs : equipe_a (str) jouant à domicile
                    equipe_b (str) jouant à l'extérieur
        Output : None
        """

        # On cherche l'indice de chaque club dans la liste des clubs pour accéder à ses caractéristiques
        i = self.noms_clubs.index(equipe_a)
        j = self.noms_clubs.index(equipe_b)

        if self.dom_ext[i][j] == 1:
            return "Cette rencontre a déjà eu lieu"
        else:
            self.dom_ext[i][j] = 1

            # On définit le nombre de buts marqués et encaissés en fonction du niveau de l'équipe
            buts_marques_a = int(self.niveau * np.random.randint(0, 5))
            buts_marques_b = int(self.niveau * np.random.randint(0, 5))

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

            for nb_butsA in range(buts_marques_a + 1):
                indice_buteur = np.random.randint(1, 12)
                # On prend un buteur au hasard dans l'équipe (sauf le gardien d'indice 0)
                buteur = self.noms_joueurs[i][indice_buteur]
                buteur.marquer_but()

            for nb_butsB in range(buts_marques_b + 1):
                indice_buteur = np.random.randint(1, 12)
                buteur = self.noms_joueurs[j][indice_buteur]
                buteur.marquer_but()

            return [buts_marques_a, buts_marques_b], [points_a,points_b]

    def __str__(self):
        """On définit __str__ la méthode retournant le nom de clubs, leur nombre de poinst et le nombre de buts marqués sous forme de dataframe
        """
        return f"Noms des clubs : {self.noms_clubs}, Nombre de points : {self.points}, Buts marqués :{self.buts_marques}"