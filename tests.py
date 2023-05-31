import unittest
import numpy as np
from Joueur import Joueur
from Club import Club
from Journee import Journee
from Saison import Saison

class TestJoueur(unittest.TestCase):
    def test_creer_joueur(self):
        joueur = Joueur('Mbappé')
        self.assertEqual('Mbappé', joueur.nom_joueur)
        self.assertEqual(0, joueur.note)
        self.assertEqual(0, joueur.buts_marques_j)

    def test_marquer_but(self):
        joueur = Joueur("MBappé")
        joueur.marquer_but()
        self.assertEqual(joueur.buts_marques_j, 1)
        joueur.marquer_but()
        self.assertEqual(joueur.buts_marques_j, 2)

class TestClub(unittest.TestCase):
    def test_creer_club(self):
        club = Club('PSG', 5, ['j1', 'j2'])
        self.assertEqual('PSG', club.nom_club)
        self.assertEqual(5, club.niveau)
        self.assertEqual(['j1', 'j2'], club.noms_joueurs)


class TestJournee(unittest.TestCase):

    def variables(self):
        saison = Saison()
        niveaux = saison.niveaux()
        noms_joueurs = saison.extraire_joueurs()
        noms_clubs = saison.extraire_clubs()


class TestSaison(unittest.TestCase):
    def test_nom_tournoi(self):
        saison = Saison()
        self.assertEqual(saison.nom, "Ligue 1")

    def test_nb_jours_total(self):
        saison = Saison()
        self.assertEqual(saison.nb_jours_total, 38)