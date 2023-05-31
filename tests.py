import unittest
import numpy as np
from Joueur import Joueur
from Club import Club
from Journee import Journee
from Saison import Saison
import pandas as pd

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

    def test_jouer_un_match(self):
        journee = Journee()

        equipe_a = "PSG"
        equipe_b = "OM"

        result = journee.jouer_un_match(equipe_a, equipe_b)

        # Vérifier que le résultat est une liste avec les éléments attendus
        self.assertEqual(len(result), 6)

        # Vérifier que les éléments de la liste sont du bon type
        self.assertIsInstance(result[0], int)  # buts_marques_a
        self.assertIsInstance(result[1], int)  # buts_marques_b
        self.assertIsInstance(result[2], int)  # points_a
        self.assertIsInstance(result[3], int)  # points_b
        self.assertIsInstance(result[4], list)  # buteurs_a
        self.assertIsInstance(result[5], list)  # buteurs_b

        # Vérifier que la bonne équipe a gagné
        if result[2] > result[3]:  # Si equipe_a a remporté le match
            self.assertGreater(result[0], result[1])  # Vérifier que equipe_a a marqué plus de buts que equipe_b
        elif result[3] > result[2]:  # Si equipe_b a remporté le match
            self.assertGreater(result[1], result[0])

    def test_classement_journee(self):
        journee = Journee()

        # Appeler la méthode classement_journee
        resultat = journee.classement_journee()

        # Vérifier que le résultat est un DataFrame de Pandas
        self.assertIsInstance(resultat, pd.DataFrame)

        # Vérifier que le DataFrame a les colonnes attendues
        noms_colonnes = ["Points dom", "Buteurs dom", "Clubs à domicile", "Buts dom", "Buts exté",
                            "Clubs à l'extérieur", "Buteurs exté", "Points exté"]
        self.assertListEqual(list(resultat.columns), noms_colonnes)

        # Vérifier que le DataFrame a le nombre de lignes attendu
        nbre_lignes = 10
        self.assertEqual(resultat.shape[0], nbre_lignes)

        # Vérifier que le nombre de points distribués est compris entre 2 et 3 fois le nombre de matchs
        nb_matchs = journee.nb_rencontres_par_jour
        nb_points_min = 2 * nb_matchs
        nb_points_max = 3 * nb_matchs
        total_points = resultat["Points dom"].sum() + resultat["Points exté"].sum()

        self.assertTrue(nb_points_min <= total_points <= nb_points_max)


        # Vérifier que le nombre de matchs joués par journée est égal au nombre de clubs/2
        nb_clubs = len(journee.noms_clubs)
        nb_matchs_attendus = nb_clubs // 2
        self.assertEqual(nb_matchs, nb_matchs_attendus)

class TestSaison(unittest.TestCase):
    def test_nom_tournoi(self):
        saison = Saison()
        self.assertEqual(saison.nom, "Ligue 1")

    def test_nb_jours_total(self):
        saison = Saison()
        self.assertEqual(saison.nb_jours_total, 38)


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


class TestObligatoire(unittest.TestCase):
   def f(self):
       a=1


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


'''class TestJournee(unittest.TestCase):
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
        self.assertEqual(journee.nb_jours_restants, 37)'''


class TestSaison(unittest.TestCase):
    def test_nom_tournoi(self):
        saison = Saison()
        self.assertEqual(saison.nom, "Ligue 1")

    def test_nb_jours_total(self):
        saison = Saison()
        self.assertEqual(saison.nb_jours_total, 38)


if __name__ == '__main__':
    unittest.main()