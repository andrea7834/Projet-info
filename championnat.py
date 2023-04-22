# -*- coding: utf-8 -*-

from equipes import  Club, Joueur
import random
import numpy as np
from math import exp
from math import factorial

"""
Ce module contient la définition de la classe principale servant à créer le championnat
"""

class Match:
    def __init__(self, equipe_dom, equipe_ext):
        """On définit la classe Match récapitulant le match joué par deux équipes

        Input : équipe jouant à domicile (str)
                  équipe jouant à l'extérieur (str)
        Output : None
        """
        self.equipe_dom = equipe_dom
        self.equipe_ext = equipe_ext
        self.buts_dom = 0
        self.buts_ext = 0
        self.proba_dom = 1.0
        self.proba_ext = 1.0

    def jouer(self):
        """On définit la méthode jouer permettant de simuler un match joué

        Input : None
        Output : None
        """

        #Simule un match entre le club et son adversaire
        niveau_dom = self.equipe_dom.niveau
        niveau_ext = self.equipe_ext.niveau

        # Calcule la probabilité de marquer des buts pour chaque club en utilisant leur niveau
        proba_dom = self.proba_dom * self.proba_ext * niveau_dom
        proba_ext = self.proba_dom * self.proba_ext * niveau_ext

        #génération aléatoires des buts en suivant une loi de poisson
        buts_dom = int(np.random.poisson(proba_dom))
        buts_ext = int(np.random.poisson(proba_ext))


        # Mise à jour des statistiques des joueurs et des clubs
        for joueur in self.equipe_dom.joueurs:
            joueur.marquer_but()
        for joueur in self.equipe_ext.joueurs:
            joueur.marquer_but()
        self.equipe_dom.jouer_match(self.equipe_ext, self.buts_dom, self.buts_ext)
        self.equipe_ext.jouer_match(self.equipe_dom, self.buts_ext, self.buts_dom)

    def __str__(self):
        """On définit __str__ la méthode retournant une chaine de caractères avec le nom des deux équipes qui
        se sont affrontées lors du match ainsi que leur score final respectif.

        Input : None
        Output : None
            """
        print(f"{self.equipe_dom.nom} : {self.buts_dom}  VS {self.buts_ext} {self.equipe_ext.nom} ")

class Championnat:
    def __init__(self, clubs):
        """On définit la classe Championnat regroupant les matchs d'une journée et le récapitulatif de la saison

        Input : le nom de tous les clubs (list)
        Output : None
        """
        super().__init__()
        self.nom = "Ligue 1"
        self.clubs = clubs
        self.matchs = []
        self.nb_matchs = 0
        self.nb_journees = 0

    def jouer_journee(self):
        """ On définit la méthode jouer_journee le récapitulatif des matchs joués en une journée

        Input : None
        Output : None
        """
        self.nb_journees += 1

        # Générer les matchs de la journée
        random.shuffle(self.clubs)
        self.nb_matchs += len(self.clubs) // 2
        matchs = [Match(self.clubs[i], self.clubs[i + 1]) for i in range(0, len(self.clubs), 2)]

        # Jouer les matchs et mettre à jour le classement
        for match in matchs:
            match.jouer()
        self.clubs.sort(key=lambda x: (x.points, x.buts_marques), reverse=True)

    def jouer_saison(self):
        """ On définit la méthode jouer_saison le récapitulatif des matchs joués sur la saison

            Input : None
            Output : None
            """
        for i in range(self.nb_journees):
            self.jouer_journee()


if __name__ == "__main__":

    noms_clubs = ["Ajaccio", "Angers", "Auxerre", "Brest", "Clermont", "Lens", "Lille", "Lorient",
                  "OL", "OM", "AS Monaco", "Montpellier", "Nantes", "Nice", "PSG", "Reims",
                  "Rennes", "Strasbourg", "Toulouse", "Troyes"]
    scores = [0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
              3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
              3.75, 1, 2.25, 0.75]
    clubs = []
    lieux = ["Ajaccio", "Angers", "Auxerre", "Brest", "Clermont", "Lens", "Lille", "Lorient",
                  "Lyon", "Marseilles", "Monaco", "Montpellier", "Nantes", "Nice", "Paris", "Reims",
                  "Rennes", "Strasbourg", "Toulouse", "Troyes"]

    for i in range (len(noms_clubs)):
        clubs.append(Club(noms_clubs[i], scores[i], lieux[i]))

    fichier = open("C:\Projet-info\\noms_joueurs.txt", "r")
    equipe = []
    ligne = fichier.readline()
    while ligne != "":
        noms = ligne.split('"')
        noms = ligne.strip(',')
        noms = ligne.strip('\n')
        equipe.append([noms])
        ligne = fichier.readline()
    print(equipe)
    fichier.close()

    i = 0
    for team in equipe:
        for nom_joueur in team :
            joueur = Joueur(nom_joueur)
            clubs[i].ajouter_joueur(nom_joueur)
        i += 1