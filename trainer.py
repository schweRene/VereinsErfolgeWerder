# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainerWindow(object):
    def setupUi(self, TrainerWindow):
        TrainerWindow.setObjectName("TrainerWindow")
        TrainerWindow.resize(1920, 1100)
        icon = QtGui.QIcon("F:/Workspace/Bremen/logo.bmp")
        TrainerWindow.setWindowIcon(icon)
        TrainerWindow.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 green, stop:1 white);")

        self.centralwidget = QtWidgets.QWidget(TrainerWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.trainerTbl = QtWidgets.QTableWidget(self.centralwidget)
        self.trainerTbl.setGeometry(QtCore.QRect(320, 50, 800, 800))  # Ändern Sie die Größe des TableWidgets
        self.trainerTbl.setStyleSheet("background-color:white;\nfont: 14pt \"Segoe UI\";")
        self.trainerTbl.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.trainerTbl.setAlternatingRowColors(False)
        self.trainerTbl.setObjectName("trainerTbl")
        self.trainerTbl.setColumnCount(5)
        self.trainerTbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.trainerTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainerTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainerTbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainerTbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainerTbl.setHorizontalHeaderItem(4, item)


        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(967, 870, 161, 41))  # Ändern Sie die Position des Speichern-Buttons
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveBtn.setFont(font)
        self.saveBtn.setStyleSheet("background-color:red;\n"
                                   "font: 14pt \"Segoe UI\";\n"
                                   "border-radius: 20px;")
        self.saveBtn.setObjectName("saveBtn")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1300, 30, 450, 300))  # Ändern Sie die Position des Bildes
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:/Workspace/Bremen/logo.jpg"))
        self.label.setObjectName("label")
        TrainerWindow.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1200, 350, 450, 300))  # Ändern Sie die Position des Bildes
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:/Workspace/Bremen/logo.bmp"))
        self.label.setObjectName("label")
        TrainerWindow.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1400, 700, 450, 200))  # Ändern Sie die Position des Bildes
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:/Workspace/Bremen/werder.png"))
        self.label.setObjectName("label")
        TrainerWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(TrainerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 22))
        self.menubar.setObjectName("menubar")
        TrainerWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(TrainerWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: white; color: black; font-size: 25px;")
        self.statusbar.setFixedHeight(50)  # Festlegen der Höhe der Statusleiste
        TrainerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrainerWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainerWindow)

    def retranslateUi(self, TrainerWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainerWindow.setWindowTitle(_translate("TrainerWindow", "SV Werder Bremen"))
        item = self.trainerTbl.horizontalHeaderItem(0)
        item.setText(_translate("TrainerWindow", "ID"))
        item = self.trainerTbl.horizontalHeaderItem(1)
        item.setText(_translate("TrainerWindow", "Vorname"))
        item = self.trainerTbl.horizontalHeaderItem(2)
        item.setText(_translate("TrainerWindow", "Nachname"))
        item = self.trainerTbl.horizontalHeaderItem(3)
        item.setText(_translate("TrainerWindow", "Von"))
        item = self.trainerTbl.horizontalHeaderItem(4)
        item.setText(_translate("TrainerWindow", "Bis"))
        self.saveBtn.setText(_translate("TrainerWindow", "Speichern"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainerWindow = QtWidgets.QMainWindow()
    ui = Ui_TrainerWindow()
    ui.setupUi(TrainerWindow)
    TrainerWindow.show()
    sys.exit(app.exec_())
