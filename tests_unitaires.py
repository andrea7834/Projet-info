import unittest
import random
import numpy as np
from equipes import Club, Joueur
from championnat import Journee, Saison

class TestJoueur(unittest.TestCase):

    def test_creer_joueur(self):
        self.joueur = Joueur()
        self.joueur.creer_joueur('Mbappé')
        self.assertIn('Mbappé', self.joueur.noms_joueurs)
        self.assertIn(0, self.joueur.notes)
        self.assertIn(0, self.joueur.buts_marques)

    def test_marquer_but(self):
        self.joueur = Joueur()
        self.joueur.creer_joueur('j1')
        self.joueur.marquer_but('j1')
        self.assertEqual(self.joueur.buts_marques[self.joueur.noms_joueurs.index('j1')], 1)
        self.joueur.marquer_but('j1')
        self.assertEqual(self.joueur.buts_marques[self.joueur.noms_joueurs.index('j1')], 2)


class TestClub(unittest.TestCase):

    def test_creer_club(self):
        self.club = Club()
        self.club.creer_club('PSG', 5, 'Paris', ['j1', 'j2'])
        self.assertIn('PSG', self.club.noms_clubs)
        self.assertIn(5, self.club.niveau)
        self.assertIn('Paris', self.club.lieux)
        self.assertIn(['j1', 'j2'], self.club.joueurs)

class TestJournee(unittest.TestCase):

    def test_numero_journee(self):
        self.journee = Journee()
        self.assertEqual(self.journee.numero_journee(), 1)
        self.journee.nb_jours_restants = 37
        self.assertEqual(self.journee.numero_journee(), 2)

class TestObligatoires(unittest.TestCase):
    '''def test_victoire_implique_plus_de_buts(self):
        self.club = Club()
        equipeA = self.club.creer_club('PSG', 5, 'Paris', ['j1', 'j2'])
        equipeB = self.club.creer_club('OM', 4.75, 'Marseille', ['j4', 'j5'])
        equipeA.buts_marques = 2
        equipeB.buts_marques = 1
        assert equipeA.buts_marques > equipeB.buts_encaisses
    def test_nombre_de_points(self):
        journee = Journee()
        assert 2 * len(journee.noms_clubs)<= journee.nb_rencontres
        assert journee.nb_rencontres <= 3 * len(journee.noms_clubs)
    def test_nombre_de_matchs(self):
        journee = Journee()
        assert journee.nb_rencontres == len(journee.noms_clubs) // 2'''

if __name__ == '__main__':
    unittest.main()

