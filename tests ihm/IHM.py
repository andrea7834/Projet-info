from PyQt5.QtCore import Qt, QAbstractTableModel, QRect, QCoreApplication, QMetaObject, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QTableView, QHBoxLayout, QLineEdit, QMenuBar, QStatusBar, QMainWindow
import Saison
import numpy as np
import sys
import pandas as pd

class PandasModel(QAbstractTableModel):
    def __init__(self, df = pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()

    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QVariant()
        elif orientation == Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QVariant()

    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if not index.isValid():
            return QVariant()

        return QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            value = value.toPyObject()
        else:
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QModelIndex()):
        return len(self._df.index)

    def columnCount(self, parent=QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ligue 1 Uber Eats")
        MainWindow.resize(662, 512)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("Case_centrale")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("Case_horizontale")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("Case_verticale")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("Tableau")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("Quitter")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 662, 21))
        self.menubar.setObjectName("Barre_Menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("Barre_statut")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ligue 1 Uber Eats", "Ligue 1 Uber Eats"))
        self.pushButton.setText(_translate("Quitter", "Quitter"))
        self.pushButton.clicked.connect(self.on_button_clicked)
        MainWindow.show()

    def on_button_clicked(self):
        alert = QMessageBox()
        alert.setText('You decided to quit!')
        alert.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    niveaux = np.array([0.5, 0.25, 1.5, 1.25, 2.5, 4.75, 4, 2.75,
                        3.5, 4.5, 4.25, 2, 1.75, 3, 5, 3.25,
                        3.75, 1, 2.25, 0.75]).reshape((20, 1))

    # Extraction de la liste des joueurs
    fichier = open("../noms_joueurs.txt", 'r')
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
    fichier = open("../noms_clubs.txt", 'r')
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
    # # window.setLayout(layout)
    # # bouton_quit.show()
    # # window.show()
    #
    # df = classement_journee.to_csv("journee.csv")
    # model = pandasModel(df)
    # view = QTableView()
    # view.setModel(model)
    # view.resize(800, 600)
    # view.show()

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())