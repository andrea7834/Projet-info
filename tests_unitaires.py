import unittest
import numpy as np
from Joueur import Joueur
from Club import Club
from Journee import Journee
from Saison import Saison

saison = Saison()
niveaux = saison.niveaux()
noms_joueurs = saison.extraire_joueurs()
noms_clubs = saison.extraire_clubs()


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
    def test_noms_clubs(self):
        journee = Journee()
        self.assertIs(journee.noms_clubs, noms_clubs)

    def test_noms_joueurs(self):
        journee = Journee()
        self.assertIs(journee.noms_joueurs, noms_joueurs)

    def test_niveaux(self):
        journee = Journee()
        self.assertIs(journee.niveaux, niveaux)

    def test_points(self):
        journee = Journee()
        self.assertIs(journee.points.all(), np.zeros((20,)).all())

    def test_buts(self):
        journee = Journee()
        self.assertEqual(journee.buts_marques.all(), np.zeros((20,)).all())

    def test_buts_dom(self):
        journee = Journee()
        self.assertEqual(journee.dom_ext.all(), np.eye(20).all())

    def test_nb_rencontres_par_jour(self):
        journee = Journee()
        self.assertEqual(journee.nb_rencontres_par_jour, 10)

    def test_numero_journee(self):
        journee = Journee()
        self.assertEqual(journee.nb_jours_restants, 38)
        journee.classement_journee()
        self.assertEqual(journee.nb_jours_restants, 37)


class TestSaison(unittest.TestCase):
    def test_nom_tournoi(self):
        saison = Saison()
        self.assertEqual(saison.nom, "Ligue 1")

    def test_nb_jours_total(self):
        saison = Saison()
        self.assertEqual(saison.nb_jours_total, 38)


if __name__ == '__main__':
    unittest.main()