# -*- coding: utf-8 -*-

from equipes import  Club, Joueur
import random
import numpy as np

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

        niveau_dom = self.equipe_dom.niveau
        niveau_ext = self.equipe_ext.niveau

        # Calcule le nombre de buts moyen pour chaque club en utilisant leur niveau
        self.proba_dom = int(niveau_dom) + self.proba_dom
        self.proba_ext = self.proba_ext + int(niveau_ext)

        #génération aléatoires des buts en suivant une loi de poisson
        buts_dom = int(np.random.poisson(self.proba_dom))
        buts_ext = int(np.random.poisson(self.proba_ext))


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
        return(f"{self.equipe_dom.nom} : {self.buts_dom} VS {self.buts_ext} : {self.equipe_ext.nom}")

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
        """ On définit la méthode jouer_journee qui donne le récapitulatif des matchs joués en une journée

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
        #self.clubs.sort(key=lambda x: (x.points, x.buts_marques), reverse=True)
        Classement.classement_recursive(self,self.clubs)

    def jouer_saison(self):
        """ On définit la méthode jouer_saison le récapitulatif des matchs joués sur la saison

            Input : None
            Output : None
            """
        for i in range(self.nb_journees):
            self.jouer_journee()

class Classement(Club):

    def __init__(self,clubs,points):
        '''
        On définit la classe Classement pour actualiser le classement général du championnat

        Input : le nom de tous les clubs (list)
                les points des clubs (int)
        Output : None
        '''

        super().__init__(noms_clubs, lieux)
        self.clubs = clubs
        self.points = points

    def classement_recursive(self, clubs):
        '''fonction qui classe les clubs par ordre décroissants de points'''
        # Cas de base : une liste d'un seul élément est déjà triée
        if len(clubs) == 1:
            return clubs

        # Divisez la liste de clubs en deux parties égales
        milieu = len(clubs) // 2
        gauche = clubs[:milieu]
        droite = clubs[milieu:]

        #Trier chaque partie en appelant la fonction: récursivité
        gauche_triee = Classement.classement_recursive(self, gauche)
        droite_triee = Classement.classement_recursive(self, droite)

        # Fusionnez les deux listes classées obtenues à partir des appels récursifs en une seule liste triée
        clubs_tries = []
        while gauche_triee and droite_triee:
            if gauche_triee[0].points <= droite_triee[0].points:
                clubs_tries.append(gauche_triee.pop(0))
            else:
                clubs_tries.append(droite_triee.pop(0))

        clubs_tries.extend(gauche_triee)
        clubs_tries.extend(droite_triee)


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
        clubs.append(Club(noms_clubs[i], lieux[i], scores[i]))

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