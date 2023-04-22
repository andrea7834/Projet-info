from championnat import Club, Joueur, Match, Championnat

"""
Ce module contient les tests unitaires 
"""

class test():

    ##tests obligatoires
    def test_victoire_implique_plus_de_buts(club1, club2, score1, score2):
        if score1 > score2:
            assert club1.buts_marques > club2.buts_marques
        elif score2 > score1:
            assert club2.buts_marques > club1.buts_marques
        else:
            # Match nul
            assert club1.buts_marques == club2.buts_marques

    def test_nombre_points_par_journee(journee):
        nb_matchs = len(journee.matchs)
        nb_points = sum([match.nb_points_gagnes() for match in journee.matchs])
        assert 2 * nb_matchs <= nb_points <= 3 * nb_matchs

    def test_nombre_matchs_par_journee(journee, nb_clubs):
        nb_matchs = len(journee.matchs)
        assert nb_matchs == nb_clubs // 2

    ##tests supplémentaires

    def test_creer_club(self):
        c = Club("Paris Saint-Germain", 5)
        assert str(c) == "Paris Saint-Germain"
        assert len(c.joueurs) == 0
        assert c.points == 0
        assert c.buts_marques == 0

    def test_creer_joueurs(self):
        j = Joueur("Mbappé", 8.5)
        assert str(j) == "Mbappé"
        assert j.note == 0
        assert j.buts_marques == 0

    def test_creer_match(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        m = Match(c1, c2)
        assert str(m) == "Paris Saint-Germain 0 - 0 Olympique de Marseille"
        assert m.buts_dom == 0
        assert m.buts_ext == 0

    def test_jouer_match(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        m = Match(c1, c2)
        m.jouer()
        assert m.buts_dom != 0 or m.buts_ext != 0
        assert m.buts_dom + m.buts_ext > 0
        assert m.equipe_dom.points + m.equipe_ext.points == 3 or m.equipe_dom.points + m.equipe_ext.points == 2

    def test_creer_championnat(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        ch = Championnat([c1, c2])
        assert str(ch) == "Championnat avec 2 clubs"
        assert len(ch.matchs) == 0
        assert ch.nb_journees == 0

    def test_jourdematch(self):
        c1 = Club("Paris Saint-Germain", 5)
        c2 = Club("Olympique de Marseille", 4.5)
        ch = Championnat([c1, c2])
        ch.jouer_journee()
        assert len(ch.matchs) == 1
        assert ch.nb_journees == 1
        assert c1.points + c2.points >= 2