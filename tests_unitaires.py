from championnat import Match, Championnat
from equipes import  Club, Joueur
import unittest
"""
Ce module contient les tests unitaires 
"""

class testClub(unittest.TestCase):
    def test_creer_club(self):
        c = Club("Paris Saint-Germain", 5)
        assert str(c) == "Paris Saint-Germain : 0 points"
        assert len(c.joueurs) == 0
        assert c.points == 0
        assert c.buts_marques == 0

class testJoueur(unittest.TestCase):
    def test_creer_joueurs(self):
        j = Joueur("Mbappé")
        assert str(j) == "Mbappé (0)"
        assert j.note == 0
        assert j.buts_marques == 0

class testChampionnat(unittest.TestCase):

    def test_creer_championnat(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        ch = Championnat([c1, c2])
        assert len(ch.matchs) == 0
        assert ch.nb_journees == 0
    def test_jour_de_match(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        ch = Championnat([c1, c2])
        ch.jouer_journee()
        assert ch.nb_journees == 1
        assert c1.points + c2.points >= 2


class testMatch(unittest.TestCase):

    def test_creer_match(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        m = Match(c1, c2)
        assert str(m) == "Paris Saint-Germain : 0 VS 0 : Olympique de Marseille"
        assert m.buts_dom == 0
        assert m.buts_ext == 0

    '''def test_jouer_match(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        m = Match(c1, c2)
        m.jouer()
        assert c1.points != 0 or c2.points != 0
        assert c1.points + c2.points > 0
        assert m.equipe_dom.points ==3'''

    def test_victoire_implique_plus_de_buts(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        m = Match(c1, c2)
        m.jouer()
        if c1.points > c2.points:
            assert c1.buts_marques > c2.buts_marques
        elif c2.points > c1.points:
            assert c2.buts_marques > c1.buts_marques
        else:
            # Match nul
            assert c1.buts_marques == c2.buts_marques

'''
class autre():
    def test_nombre_points_par_journee(self):
        j = Championnat.jouer_journee(self.nb_journees)
        nb_matchs = len(j.matchs)
        nb_points = sum([match.nb_points_gagnes() for match in j.matchs])
        assert 2 * nb_matchs <= nb_points
        assert nb_points <= 3 * nb_matchs

    def test_nombre_matchs_par_journee(self.nb_journee, nb_clubs):
        nb_matchs = len(journee.matchs)
        assert nb_matchs == nb_clubs // 2'''