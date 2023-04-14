import random

class Club:
    def __init__(self, nom):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison

        Input : nom du club (str)
        Output : None
        """
        self.nom = nom
        self.joueurs = []
        self.points = 0
        self.buts_marques = 0

    def ajouter_joueur(self, joueur):
        """On définit la fonction ajouter_joueur permettant d'ajouter un joueur dans l'équipe du club

        Input : nom du joueur (str)
        Output : None
        """
        self.joueurs.append(joueur)

    def jouer_match(self, adversaire, buts_marques, buts_encaisses):
        """On définit la fonction jouer_match ajoutant un match dans le tableau des matchs

        Inputs : adversaire (str)
                    buts_marques (int)
                    buts_encaisses (int)
        Output : None
        """
        if buts_marques > buts_encaisses:
            self.points += 3
        elif buts_marques == buts_encaisses:
            self.points += 1
            adversaire.points += 1
        elif buts_marques < buts_encaisses:
            adversaire.points += 3
        self.buts_marques += buts_marques
        adversaire.buts_marques += buts_encaisses

    def __str__(self):
        """On définit __str__ la fonction retournant une chaine de caractères avec le nom du club
        Input : None
        Output : None
        """
        return self.nom


class Joueur:
    def __init__(self, nom, note):
        """On définit la classe Joueur définissant les caractéristiques d'un joueur

        Input  :  nom du joueur (str)
                    note du joueur (float)
        Output : None
        """
        self.nom = nom
        self.note = note
        self.buts_marques = 0

    def marquer_but(self):
        """On définit la fonction marquer_but mettant à jour le nombre de buts marqués
        par le joueur lorsqu'il marque un but

        Input : None
        Output : None
        """
        self.buts_marques += 1

    def __str__(self):
        return self.nom


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

    def jouer(self):
        """On définit la fonction jouer permettant de simuler un match joué

        Input : None
        Output : None
        """

        # Simulation du match (génération aléatoire des buts marqués)
        self.buts_dom = random.randint(0, 5)
        self.buts_ext = random.randint(0, 5)

        # Mise à jour des joueurs et des clubs
        for joueur in self.equipe_dom.joueurs:
            joueur.marquer_but()
        for joueur in self.equipe_ext.joueurs:
            joueur.marquer_but()
        self.equipe_dom.jouer_match(self.equipe_ext, self.buts_dom, self.buts_ext)
        self.equipe_ext.jouer_match(self.equipe_dom, self.buts_ext, self.buts_dom)

    def __str__(self):
        print(f"{self.equipe_dom.nom} : {self.buts_dom}  VS {self.buts_ext} {self.equipe_ext.nom} ")


class Championnat:
    def __init__(self, clubs):
        """On définit la classe Chapionnat regroupant les matchs d'une journée et le récapitulatif de la saison

        Input : le nom de tous les clubs (list)
        Output : None
        """
        self.nom = "Ligue 1"
        self.clubs = clubs
        self.matchs = []
        self.nb_matchs = 0
        self.nb_journees = 0

    def jouer_journee(self):
        """ On définit la fonction jouer_journee le récapitulatif des matchs joués en une journée

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
        self.clubs.sort(key=lambda x: (x.points, x.buts_marques), reverse=True)

    def jouer_saison(self):
        """ On définit la fonction jouer_saison le récapitulatif des matchs joués sur la saison

            Input : None
            Output : None
            """
        for i in range(self.nb_journees):
            self.jouer_journee()

if __name__ == "__main__":

    club1 =  Club("AC Ajaccio")
    club2 = Club("Anger")
    club3 = Club("Auxerre")
    club4 = Club("Brest")
    club5 = Club("Clermont")
    club6 = Club("Lens")
    club7 = Club("Lille")
    club8 = Club("Lorient")
    club9 = Club("OL")
    club10 = Club("OM")
    club11 = Club("Monaco")
    club12 = Club("Montpellier")
    club13 = Club("Nantes")
    club14 = Club("Nice")
    club15 = Club("PSG")
    club16 = Club("Reims")
    club17 = Club("Rennes")
    club18 = Club("Strasbourg")
    club19 = Club("Toulouse")
    club20 = Club("Troyes")

    clubs = [club1, club2, club3, club4, club5, club6, club7, club8, club9, club10,
             club11, club12, club13, club14, club15, club16, club17, club18, club19, club20]

    i = 0
    for club in clubs:
        for i in range(1, 21):
            joueur = Joueur(str(i), random.randint(0, 20))
            club.ajouter_joueur(joueur)

    match = Match(club1, club2)
    match.jouer()
    print(f"Score final : {club1} {match.buts_dom} - {match.buts_ext} {club2}")

    # Tests unitaires
    # def test_club():
    #     club = Club("PSG")
    #     assert