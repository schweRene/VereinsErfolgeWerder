from PyQt5.QtWidgets import QMenuBar, QAction
from saisonwindow import SaisonWindow
from spielerwindow import SpielerWindow
from trainerwindow import TrainerWindow
from erfolgewindow import ErfolgeWindow


class MenuHandler:

    def __init__(self, parent=None):
        self.parent = parent
        self.menubar = parent.menuBar()

    def add_window_action(self, name, method):
        action = QAction(name, self.parent)
        action.triggered.connect(method)
        self.parent.menuBar().addAction(action)

    def create_menu(self):
        # Menüs erstellen
        start_menu = self.menubar.addMenu('Startseite')
        saison_menu = self.menubar.addMenu('Saisonübersicht')
        trainer_menu = self.menubar.addMenu('Trainerübersicht')
        erfolge_menu = self.menubar.addMenu('Erfolgeübersicht')
        spieler_menu = self.menubar.addMenu('Spielerübersicht')

        # Aktionen für die Menüs erstellen
        start_action = QAction('Startseite anzeigen', self.parent)
        start_menu.addAction(start_action)
        start_action.triggered.connect(self.parent.show_home_window)

        saison_action = QAction('Saisonübersicht anzeigen', self.parent)
        saison_menu.addAction(saison_action)
        saison_action.triggered.connect(self.parent.show_saison_window)

        trainer_action = QAction('Trainerübersicht anzeigen', self.parent)
        trainer_menu.addAction(trainer_action)
        trainer_action.triggered.connect(self.parent.show_trainer_window)

        erfolge_action = QAction('Erfolgeübersicht anzeigen', self.parent)
        erfolge_menu.addAction(erfolge_action)
        erfolge_action.triggered.connect(self.parent.show_erfolge_window)

        spieler_action = QAction('Spielerübersicht anzeigen', self.parent)
        spieler_menu.addAction(spieler_action)
        spieler_action.triggered.connect(self.parent.show_spieler_window)

    def show_saison_window(self):
        # Fenster schließen bei Wechsel auf eine andere Seite
        self.parent.close()
        # Saisonfenster erstellen und anzeigen
        self.parent.saison_window = SaisonWindow()
        self.parent.saison_window.show()

    def show_trainer_window(self):
        self.parent.close()
        self.parent.trainer_window = TrainerWindow()
        self.parent.trainer_window.show()

    def show_erfolge_window(self):
        self.parent.close()
        self.parent.erfogle_window = ErfolgeWindow()
        self.parent.erfogle_window.show()

    def show_spieler_window(self):
        self.parent.close()
        self.parent.spieler_window = SpielerWindow()
        self.parent.spieler_window.show()

    def show_home_window(self):
        self.parent.close()
        self.parent.home_window = HomeWindow()
        self.parent.home_window.show()
