import pandas as pd

fichier = open("noms_clubs.txt", 'r')
noms_clubs = []
fichier.seek(0)  # Mettre le curseur au début du fichier
for club in fichier:  # Il y a un club par ligne
    club = club.strip(" \n")
    noms_clubs.append(club)
fichier.close() # Fermeture du fichier après lecture

fichier = open("noms_joueurs.txt", 'r')
noms_joueurs = []
fichier.seek(0)  # Mettre le curseur au début du fichier
for ligne in fichier:  # Il y a un club par ligne
    equipe = []
    noms = ligne.strip(" \n")
    noms = noms.split()
    for nom in noms:
        equipe.append(nom)
    noms_joueurs.append(equipe)
fichier.close() # Fermeture du fichier après lecture

# recap_saison = pd.DataFrame({"Classement" : [i for i in range(1, 21)], 'Nom du club' : noms_clubs, "Nombre de points" : [], "Nombre de buts" : []})
# recap_joueurs = pd.DataFrame({'Nom du joueur' : noms_joueurs, "Nombre de buts" : [], "Note" : []})