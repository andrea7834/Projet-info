import unittest
import numpy as np
from Joueur import Joueur
from Club import Club
from Journee import Journee
from Saison import Saison

niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                            3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                            3.75, 1, 2.25, 0.75]).reshape((20, 1))

#Extraction de la liste des joueurs
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

# Extraction de la liste des clubs
fichier = open("noms_clubs.txt", 'r')
noms_clubs = []
fichier.seek(0)  # Mettre le curseur au début du fichier
i = 0
for nom_club in fichier:  # Il y a un club par ligne
    nom_club = nom_club.strip(" \n")
    noms_clubs.append(nom_club)
    i += 1
fichier.close()  # Fermeture du fichier après lecture

class TestJoueur(unittest.TestCase):
    def test_creer_joueur(self):
        joueur = Joueur('Mbappé')
        self.assertEqual('Mbappé', joueur.nom_joueur)
        self.assertEqual(0, joueur.note)
        self.assertEqual(0, joueur.buts_marques)

    def test_marquer_but(self):
        joueur = Joueur("MBappé")
        joueur.marquer_but()
        self.assertEqual(joueur.buts_marques, 1)
        joueur.marquer_but()
        self.assertEqual(joueur.buts_marques, 2)


class TestClub(unittest.TestCase):
    def test_creer_club(self):
        club = Club('PSG', 5, ['j1', 'j2'])
        self.assertEqual('PSG', club.nom_club)
        self.assertEqual(5, club.niveau)
        self.assertEqual(['j1', 'j2'], club.noms_joueurs)


class TestJournee(unittest.TestCase):
    def test_noms_clubs(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertIs(journee.noms_clubs, noms_clubs)

    def test_noms_joueurs(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertIs(journee.noms_joueurs, noms_joueurs)

    def test_niveaux(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertIs(journee.niveaux, niveaux)

    def test_points(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertIs(journee.points.all(), np.zeros((20,)).all())

    def test_buts(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(journee.buts_marques.all(), np.zeros((20,)).all())

    def test_buts_dom(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(journee.dom_ext.all(), np.eye(20).all())

    def test_nb_rencontres_par_jour(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(journee.nb_rencontres_par_jour, 10)

    def test_numero_journee(self):
        journee = Journee(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(journee.nb_jours_restants, 38)
        journee.classement_journee()
        self.assertEqual(journee.nb_jours_restants, 37)


class TestSaison(unittest.TestCase):
    def test_nom_tournoi(self):
        saison = Saison(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(saison.nom, "Ligue 1")

    def test_nb_jours_total(self):
        saison = Saison(noms_clubs, noms_joueurs, niveaux)
        self.assertEqual(saison.nb_jours_total, 38)


if __name__ == '__main__':
    unittest.main()