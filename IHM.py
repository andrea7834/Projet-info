from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QTableView
import Saison
import numpy as np
import sys
import pandas as pd


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You decided to quit!')
    alert.exec()

if __name__ == '__main__':
    niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                        3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                        3.75, 1, 2.25, 0.75]).reshape((20, 1))

    # Extraction de la liste des joueurs
    fichier = open("noms_joueurs.txt", 'r')
    noms_joueurs = []
    fichier.seek(0)
    for ligne in fichier:  # Il y a une équipe de 11 joueurs par ligne
        equipe = []
        noms = ligne.strip(" \n")
        noms = noms.split()  # Le nom de chaque joueur est séparé par un espace
        for nom in noms:
            equipe.append(nom)
        noms_joueurs.append(equipe)
    fichier.close()  # Fermeture du fichier après lecture

    # Extraction de la liste des clubs
    fichier = open("noms_clubs.txt", 'r')
    noms_clubs = []
    fichier.seek(0)  # Mettre le curseur au début du fichier
    i = 0
    for nom_club in fichier:  # Il y a un club par ligne
        nom_club = nom_club.strip(" \n")
        noms_clubs.append(nom_club)
        i += 1
    fichier.close()  # Fermeture du fichier après lecture

    saison = Saison.Saison(noms_clubs, noms_joueurs, niveaux)
    classement_journee = saison.classement_journee()
    app = QApplication(sys.argv)

    # Customisation de la fenêtre
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QPushButton { margin: 10ex; }")

    # window = QWidget()
    # layout = QVBoxLayout()
    # bouton_quit = QPushButton('Quit')
    # layout.addWidget(bouton_quit)
    # bouton_quit.clicked.connect(on_button_clicked)
    # window.setLayout(layout)
    # bouton_quit.show()
    # window.show()

    df = classement_journee.to_csv("journee.csv")
    model = pandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())