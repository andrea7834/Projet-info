# -*- coding: utf-8 -*-

from equipes import Club, Joueur
import numpy as np

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
        self.nb_rencontres = 10  # Comme il y a 20 équipes alors il y a 10 matchs par jour puisque toutes les équipes jouent une fois
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
                        if equipe[j] not in self.adversaires_a_domicile[i] and equipe[i] not in self.adversaires_a_l_ext[j]:
                            self.domicile.append(equipe[i])
                            self.exterieur.append(equipe[j])
                            self.adversaires_a_domicile[i].append(equipe[j])
                            self.adversaires_a_l_ext[j].append(equipe[i])
                            self.nb_rencontres -= 1

    def simuler_journee(self):
        """On définit la méthode simuler_journee simulant les résultats de la journée à l'aide
        de la fonction jouer_match de la classe Club
        Inputs : None
        Output : None
        """
        self.rencontres_journee()
        for i in range(11): # Il y a 10 matchs par jour puisqu'il y a 20 équipes différentes
            equipeA = self.domicile[i]
            equipeB = self.exterieur[i]
            butsA, butsB = self.jouer_match(equipeA, equipeB)
            self.buts_dom.append(butsA)
            self.buts_ext.append(butsB)
        domicile = np.array(self.domicile).reshape(10,)
        exterieur = np.array(self.exterieur).reshape(10,)
        score_dom = np.array(self.buts_dom).reshape(10,)
        score_ext = np.array(self.buts_ext).reshape(10,)
        return np.array(domicile, score_dom, score_ext, exterieur)


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

    def classement_recursive(self, clubs):
        '''fonction qui classe les clubs par ordre décroissants de points'''

        # Cas de base : une liste d'un seul élément est déjà triée
        if len(clubs) == 1:
            return clubs
        else:
            # Divisez la liste de clubs en deux parties égales
            milieu = len(clubs) // 2
            gauche = clubs[:milieu]
            droite = clubs[milieu:]

            # Trier chaque partie en appelant la fonction récursive
            gauche_triee = self.classement_recursive(gauche)
            droite_triee = self.classement_recursive(droite)

            # Fusionnez les deux listes classées obtenues à partir des appels récursifs en une seule liste triée
            clubs_tries = []
            while gauche_triee and droite_triee:
                if gauche_triee[0].points <= droite_triee[0].points:
                    clubs_tries.append(gauche_triee.pop(0))
                else:
                    clubs_tries.append(droite_triee.pop(0))

            clubs_tries.extend(gauche_triee)
            clubs_tries.extend(droite_triee)

    def jouer_journee(self):
        """ On définit la méthode jouer_journee qui donne le récapitulatif des matchs joués en une journée

        Input : None
        Output : None
        """
        self.nb_journees += 1
        resultats_journee = self.simuler_journee()

        #self.clubs.sort(key=lambda x: (x.points, x.buts_marques), reverse=True)
        self.classement_recursive(self.clubs)

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

    for i in range (len(noms_clubs)):
        Club.creer_club(noms_clubs[i],  scores[i], lieux[i], equipe[i])

    i = 0
    for team in equipe:
        for nom_joueur in team :
            joueur = Joueur(nom_joueur)
            clubs[i].ajouter_joueur(nom_joueur)
        i += 1