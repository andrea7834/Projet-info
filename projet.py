import random
from math import exp
from math import factorial

class Club:
    def __init__(self, nom, niveau):
        """ On définit la classe Club qui regroupe le nom de chaque club, ses joueurs,
        son nombre de points et le nombre de buts marqués lors de la saison

        Input : nom du club (str)
        Output : None
        """
        self.nom = nom
        self.niveau = niveau
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
        elif buts_marques < buts_encaisses:
            adversaire.points += 3
        elif buts_marques == buts_encaisses:
            self.points += 1
            adversaire.points += 1

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
        self.niveau_dom = 0
        self.niveau_ext = 0
        self.proba_dom = 1
        self.proba_ext = 1

    def jouer(self, adversaire):
        """On définit la fonction jouer permettant de simuler un match joué

        Input : None
        Output : None
        """

        #Simule un match entre le club et son adversaire
        niveau_dom = self.niveau
        niveau_ext = adversaire.niveau

        # Calcule la probabilité de marquer des buts pour chaque club en utilisant leur niveau
        proba_dom = self.proba_dom * self.proba_ext * self.niveau_dom
        proba_ext = self.proba_dom * self.proba_ext * self.niveau_ext

        #génération aléatoires des buts en suivant une loi de poisson
        buts_dom = int(np.random.poisson(proba_dom))
        buts_ext = int(np.random.poisson(proba_ext))


        # Mise à jour des statistiques des joueurs et des clubs
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
        c = Club("Paris Saint-Germain")
        assert str(c) == "Paris Saint-Germain"
        assert len(c.joueurs) == 0
        assert c.points == 0
        assert c.buts_marques == 0

    def test_creer_joueurs(self):
        j = Joueur("Mbappé")
        assert str(j) == "Mbappé"
        assert j.note == 0
        assert j.buts_marques == 0

    def test_creer_match(self):
        c1 = Club("Paris Saint-Germain")
        c2 = Club("Olympique de Marseille")
        m = Match(c1, c2)
        assert str(m) == "Paris Saint-Germain 0 - 0 Olympique de Marseille"
        assert m.buts_dom == 0
        assert m.buts_ext == 0

    def test_jouer_match(self):
        c1 = Club("Paris Saint-Germain")
        c2 = Club("Olympique de Marseille")
        m = Match(c1, c2)
        m.jouer()
        assert m.buts_dom != 0 or m.buts_ext != 0
        assert m.buts_dom + m.buts_ext > 0
        assert m.equipe_dom.points + m.equipe_ext.points == 3 or m.equipe_dom.points + m.equipe_ext.points == 2

    def test_creer_championnat(self):
        c1 = Club("Paris Saint-Germain")
        c2 = Club("Olympique de Marseille")
        ch = Championnat([c1, c2])
        assert str(ch) == "Championnat avec 2 clubs"
        assert len(ch.matchs) == 0
        assert ch.nb_journees == 0

    def test_jourdematch(self):
        c1 = Club("Paris Saint-Germain")
        c2 = Club("Olympique de Marseille")
        ch = Championnat([c1, c2])
        ch.jouer_journee()
        assert len(ch.matchs) == 1
        assert ch.nb_journees == 1
        assert c1.points + c2.points >= 2

if __name__ == "__main__":

    club1 =  Club("Ajaccio")
    joueurs1 = ["Leroy", "Michelin", "Alphonse", "Lebas", "Diallo", "Vidal", "Gonzalez", "N'Diaye", "Silla", "Roure", "Hamouma"]
    club2 = Club("Angers")
    joueurs2 = ["Borne", "Doumbia", "Camara", "Mendy", "Masson", "Capelle", "Guillaume", "Alioui", "Sima", "Corduan", "Bamba"]
    club3 = Club("Auxerre")
    joueurs3 = ["De Percin", "Lipinski", "Pellenard", "Jeanvier", "Bain", "Dembélé", "Da Costa", "Danois", "Autret", "Dugimont","Merdji"]
    club4 = Club("Brest")
    joueurs4 = ["Blasquez", "Duverne", "Brassier", "Chardonnet", "Magnetti", "Del Castillo", "Le Douaron", "Lemaréchal", "Tavarès", "Mounié", "Elis"]
    club5 = Club("Clermont")
    joueurs5 = ["Margueron", "Boyer", "Borges", "Wieteska", "Cissé", "Versini", "Maurer", "Massolin", "Rajot", "Bayo", "Gastien"]
    club6 = Club("Lens")
    joueurs6 = ["Vincensini", "Ganiou", "Sylla", "Medina", "Fortès", "Boura", "Gradit", "Le Cardinal", "Pereira", "Varane", "Valencia"]
    club7 = Club("Lille")
    joueurs7 = ["Chevalier", "Burlet", "Ribeiro", "Fonte", "Yoro", "Gudmundsson", "Martin", "Cabella", "Gomes", "André",  "David"]
    club8 = Club("Lorient")
    joueurs8 = ["Pattier", "Silva", "Talbi", "Matsima", "Laporte", "Le Goff", "Kroupi", "Pelon", "Innocent", "Ponceau", "Le Fée"]
    club9 = Club("OL")
    joueurs9 = ["Lopès", "Gusto", "Tagliafico", "Sanchez", "Caqueret", "Lepenant", "Tolisso", "Lega", "Bercola", "Aouar", "Cherki"]
    club10 = Club("OM")
    joueurs10 = ["Blanco", "Bailly", "Gigot", "Balerdi", "Clauss", "Lopez", "Payet", "Harit", "Kaboré", "Rongier", "Ounahi"]
    club11 = Club("AS Monaco")
    joueurs11 = ["Lienard", "Serrano", "Maripan", "Sibidé", "Jakobs", "Embolo", "Pelé", "Henrique", "Aguilar", "Ben Yedder", "Ben Seguir"]
    club12 = Club("Montpellier")
    joueurs12 = ["Lecomte", "Sainte-Luce", "Tchato", "Sakho", "Mavididi", "Savanier", "Maouassa", "Nordin", "Germain", "Wahi", "Khazri"]
    club13 = Club("Nantes")
    joueurs13 = ["Descamps", "Girotto", "Guessand", "Blas", "Coco", "Ganago", "Mollet", "Simon", "Delort", "Castelletto", "Pallois"]
    club14 = Club("Nice")
    joueurs14 = ["Guarrido", "Dante", "Bryan", "Attal", "Beka Beka", "Laborde", "Pépé", "Moffi", "Diop", "Brahimi", "Thuram"]
    club15 = Club("PSG")
    joueurs15 = ["Letellier", "Kipembé", "Ramos", "Mbappé", "Messi", "Verrati", "Neymar", "Mendès", "Sanchès", "Soler", "Ruiz"]
    club16 = Club("Reims")
    joueurs16 = ["Lemaître", "Abdelhamid", "Lopy", "Cajuste", "Ito", "Zeneli", "Balogin", "Flips", "Serhuis", "Munetsi", "Moalida"]
    club17 = Club("Rennes")
    joueurs17 = ["Salin", "Rodon", "Theate", "Wooh", "Assignon", "Traoré", "Terrier", "Santamaria", "Kalimuendo", "Gouiri", "Majer"]
    club18 = Club("Strasbourg")
    joueurs18 = ["Sels", "Perrin", "Le Marchand", "H.Diallo", "Mothiba", "Gameiro", "Djiku", "Bellegarde", "Liénard", "Sanson", "Delaine"]
    club19 = Club("Toulouse")
    joueurs19 = ["Himeur", "Dallinga", "Chaïbi", "Ratao", "Onaiwu", "Healey", "Spierings", "Aboukhlal", "Van den Boomen", "Dejaegere", "Desler"]
    club20 = Club("Troyes")
    joueurs20 = ["Moulin", "Baldé", "Ugbo", "Ripart", "Lopez", "Odobert", "Chavalerin", "Conté", "Palaversa", "Porozo", "Salmier"]

    clubs = [club1, club2, club3, club4, club5, club6, club7, club8, club9, club10,
             club11, club12, club13, club14, club15, club16, club17, club18, club19, club20]
    joueurs =  [joueurs1, joueurs2, joueurs3, joueurs4, joueurs5, joueurs6, joueurs7,
                joueurs8, joueurs9, joueurs10, joueurs11, joueurs12, joueurs13, joueurs14,
                joueurs15, joueurs16, joueurs17, joueurs18, joueurs19, joueurs20]

    for club in clubs:
        for joueur in joueurs:
            Joueur(joueur, random.randint(0, 20))
            club.ajouter_joueur(joueur)

    match = Match(club1, club2)
    match.jouer()
    print(f"Score final : {club1} {match.buts_dom} - {match.buts_ext} {club2}")

    # Tests unitaires
    # def test_club():
    #     club = Club("PSG")
    #     assert