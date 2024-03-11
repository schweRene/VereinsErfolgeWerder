from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1100)
        icon = QtGui.QIcon("F:/Workspace/Bremen/logo.bmp")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 green, stop:1 white);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Erstellen des Layouts für das Zentrieren des Bildes und Textes
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(40, 20, 40, 10)  # Setzen des Abstands zu den Rändern

        # Erstellen des QLabel für das Bild und Hinzufügen zum Layout
        self.stadiolbl = QtWidgets.QLabel(self.centralwidget)
        self.stadiolbl.setBaseSize(QtCore.QSize(1920, 1080))
        self.stadiolbl.setText("")
        self.stadiolbl.setPixmap(QtGui.QPixmap("F:/Workspace/Bremen/stadion.jpg").scaledToHeight(400))
        self.stadiolbl.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.stadiolbl)

        # Erstellen des QLabel für den Text unter dem Bild und Hinzufügen zum Layout
        self.werderlbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(90)
        self.werderlbl.setFont(font)
        self.werderlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.werderlbl.setObjectName("werderlbl")
        self.werderlbl.setStyleSheet("color: white; font-size: 90px;")
        self.werderlbl.setText("SV Werder Bremen")
        layout.addWidget(self.werderlbl)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: white; color: black; font-size: 25px;")
        self.statusbar.setFixedHeight(50)  # Festlegen der Höhe der Statusleiste
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SV Werder Bremen"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
