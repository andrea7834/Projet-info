# -*- coding: utf-8 -*-

import Club
import numpy as np

""" Ce module contient la définition de la classe Journée simulant une journée de championnat """


class Journee(Club):

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée

        Input : None
        Output : None
        """
        super().__init__()
        self.nb_rencontres_par_jour = 10
        # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
        self.domicile = []  # On définit les équipes jouant à domicile ou à l'extérieur
        self.exterieur = []
        self.buts_dom = []  # Il y a 10 matchs par jours
        self.buts_ext = []
        self.nb_jours_restants = 38  # il y a 19 rencontres aller et 19 rencontres retour

    def numero_journee(self):
        """On définit la méthode numero_journee déterminant le numéro de la journée de match
        Inputs : None
        Output : None
        """
        return 39 - self.nb_jours_restants

    def rencontres_journee(self):
        """On définit la méthode rencontres_journee décidant des rencontres de la journée
        Inputs : None
        Output : None
        """
        self.nb_jours_restants -= 1
        self.nb_rencontres_par_jour = 10
        if self.nb_jours_restants > 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

            while self.nb_rencontres_par_jour > 0:
                for i in range(len(equipes) + 1):
                    for j in range(len(equipes) + 1):
                        # On vérifie que ces deux équipes ne se sont pas affrontées au domicile de l'équipe i
                        if self.rencontre_possible(equipes[j], equipes[i]):
                            self.domicile.append(equipes[i])
                            self.exterieur.append(equipes[j])
                            buts_equipe_i, buts_equipe_j = self.jouer_match(equipes[i], equipes[j])
                            self.nb_rencontres_par_jour -= 1

    def simuler_journee(self):
        """On définit la méthode simuler_journee simulant les résultats de la journée à l'aide
        de la fonction jouer_match de la classe Club
        Inputs : None
        Output : None
        """
        self.rencontres_journee()
        for i in range(10):  # Il y a 10 matchs par jour puisqu'il y a 20 équipes différentes
            equipe_a = self.domicile[i]
            equipe_b = self.exterieur[i]
            buts_a, buts_b = self.jouer_match(equipe_a, equipe_b)
            self.buts_dom.append(buts_a)
            self.buts_ext.append(buts_b)

        domicile = np.array(self.domicile).reshape(10,)
        exterieur = np.array(self.exterieur).reshape(10,)
        score_dom = np.array(self.buts_dom).reshape(10,)
        score_ext = np.array(self.buts_ext).reshape(10,)

        return np.array(domicile, score_dom), np.array(exterieur, score_ext)