from PyQt5.QtWidgets import QMainWindow, QApplication
from homeui import Ui_MainWindow
from menuhandler import MenuHandler
from saisonwindow import SaisonWindow

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Bild reponsiv machen
        self.ui.stadiolbl.setScaledContents(True)

        # Text größer machen
        font = self.ui.werderlbl.font()
        font.setPointSize(16)
        self.ui.werderlbl.setFont(font)

        # Menüleiste erstellen und mit dem Menuhandler verbinden
        self.menu_handler = MenuHandler(self)
        self.menu_handler.add_window_action('Saisonübersicht', self.menu_handler.show_saison_window)
        self.menu_handler.add_window_action('Erfolgeübersicht', self.menu_handler.show_erfolge_window)
        self.menu_handler.add_window_action('Trainerübersicht', self.menu_handler.show_trainer_window)
        self.menu_handler.add_window_action('Spielerübersicht', self.menu_handler.show_spieler_window)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())
