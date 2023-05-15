import unittest
import random
import numpy as np
from Joueur import Joueur
from Club import Club
from Journee import Journee
from Saison import Saison

class TestJoueur(unittest.TestCase):
    def test_creer_joueur(self):
        joueur = Joueur('Mbappé')
        self.assertIs('Mbappé', joueur.nom_joueur)
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
        self.assertIn('PSG', club.nom_club)
        self.assertIn(5, club.niveau)
        self.assertIn(['j1', 'j2'], club.noms_joueurs)

class TestJournee(unittest.TestCase):
    def test_numero_journee(self):
        self.journee = Journee()
        self.assertEqual(self.journee.numero_journee(), 1)
        self.journee.nb_jours_restants = 37
        self.assertEqual(self.journee.numero_journee(), 2)
'
# class TestObligatoires(unittest.TestCase):
#     def test_victoire_implique_plus_de_buts(self):
#         self.club = Club()
#         equipeA = self.club.creer_club('PSG', 5, 'Paris', ['j1', 'j2'])
#         equipeB = self.club.creer_club('OM', 4.75, 'Marseille', ['j4', 'j5'])
#         equipeA.buts_marques = 2
#         equipeB.buts_marques = 1
#         assert equipeA.buts_marques > equipeB.buts_encaisses
#     def test_nombre_de_points(self):
#         journee = Journee()
#         assert 2 * len(journee.noms_clubs)<= journee.nb_rencontres
#         assert journee.nb_rencontres <= 3 * len(journee.noms_clubs)
#     def test_nombre_de_matchs(self):
#         journee = Journee()
#         assert journee.nb_rencontres == len(journee.noms_clubs) // 2'''

if __name__ == '__main__':
    unittest.main()