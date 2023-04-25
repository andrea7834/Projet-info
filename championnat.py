# -*- coding: utf-8 -*-

from equipes import Club, Joueur
import numpy as np
import sys

"""
Ce module contient la définition de la classe principale servant à créer le championnat
"""


class Journee(Club):

    def __init__(self):
        """On définit la classe Journee comprenant les rencontres de la journée

        Input : None
        Output : None
        """
        super().__init__()
        self.nb_rencontres = 10
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
        """On définit la méthode rencontres_journee décidant des rencontres de la journee
        Inputs : None
        Output : None
        """
        self.nb_jours_restants -= 1
        if self.nb_jours_restants > 0:  # On vérifie bien que ce n'est pas la fin de la saison
            equipes = self.noms_clubs

            while self.nb_rencontres > 0:
                for i in range(len(equipes) + 1):
                    for j in range(len(equipes) + 1):
                        # On vérifie que ces deux équipes ne se sont pas affrontées au domicile de l'équipe i
                        if equipes[j] not in self.adversaires_a_domicile[i] \
                                and equipes[i] not in self.adversaires_a_l_ext[j]:
                            self.domicile.append(equipes[i])
                            self.exterieur.append(equipes[j])
                            self.adversaires_a_domicile[i].append(equipes[j])
                            self.adversaires_a_l_ext[j].append(equipes[i])
                            self.nb_rencontres -= 1

    def simuler_journee(self):
        """On définit la méthode simuler_journee simulant les résultats de la journée à l'aide
        de la fonction jouer_match de la classe Club
        Inputs : None
        Output : None
        """
        self.rencontres_journee()
        for i in range(11):  # Il y a 10 matchs par jour puisqu'il y a 20 équipes différentes
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


class Saison(Journee):
    def __init__(self):
        """On définit la classe Saison regroupant les matchs d'une journée et le récapitulatif de la saison

        Input : None
        Output : None
        """
        super().__init__()
        self.nom = "Ligue 1"
        self.classement = []
        self.matchs = []
        self.nb_journees = 0

    def tri(self, tab):
        """ On définit la méthode tri permet de trier un tableau en fonction du nombre de points des équipes

        Input : tab (array)
        Output : None
        """
        tab1 = tab.copy()
        tab_trie = []
        while tab1:
            arg_min = np.argmin(tab[:, 1])
            tab_trie.append(tab1[arg_min])
            tab1.pop(arg_min)
        return tab_trie

    def jouer_journee(self):
        """ On définit la méthode jouer_journee qui donne le récapitulatif des matchs joués en une journée

        Input : None
        Output : None
        """
        tab_dom, tab_ext = self.simuler_journee()
        scores_totaux = np.array(tab_dom, tab_ext).reshape((20, 2))
        classement_journee = self.tri(scores_totaux)
        return classement_journee

    def jouer_saison(self):
        """ On définit la méthode jouer_saison le récapitulatif des matchs joués sur la saison

            Input : None
            Output : None
            """
        classement_saison = np.zeros((20, 3))  # Tableau récapitulatif de la saison
        classement_saison[:, 0] = self.noms_clubs  # La 1ʳᵉ colonne correspond au nom des clubs
        classement_saison[:, 1] = self.points  # La 2ᵉ colonne correspond à leur nombre de points
        for i in range(self.nb_journees + 1):
            classement_journee = self.jouer_journee()
            j = 0
            for club in self.noms_clubs:
                indice = classement_journee[:, 0].index(club)
                classement_saison[j, 2] += [indice, 2]  # La 3ᵉ colonne correspond à leur nombre de buts
                j += 1
        return classement_saison


if __name__ == "__main__":
    scores = [0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
              3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
              3.75, 1, 2.25, 0.75]

    clubs = []
    lieux = ["Ajaccio", "Angers", "Auxerre", "Brest", "Clermont", "Lens", "Lille", "Lorient",
                "Lyon", "Marseilles", "Monaco", "Montpellier", "Nantes", "Nice", "Paris", "Reims",
                "Rennes", "Strasbourg", "Toulouse", "Troyes"]
    equipes = []

    joueurs = Joueur()
    clubs = Club()
    for i in range(len(noms_clubs)):
        for j in range(11):
            joueurs.creer_joueur(equipes[i][j])
        clubs.creer_club(noms_clubs[i], scores[i], lieux[i], equipes[i])
    saison = Saison()
    print(saison.jouer_saison())