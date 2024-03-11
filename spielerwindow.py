from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from spieler import Ui_SpielerWindow
from homeui import Ui_MainWindow
from spielercontroller import SpielerController
from PyQt5 import QtWidgets, QtCore
import logging

class SpielerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SpielerWindow()
        self.ui.setupUi(self)

        self.db_name = "werder.db"
        self.controller = SpielerController(self.db_name)

        self.ui.saveBtn.clicked.connect(self.save_spieler)

        self.refresh_table()

        # Verbinden Sie das keyPressEvent-Ereignis des TableWidgets
        self.ui.spielerTbl.keyPressEvent = self.custom_keyPressEvent

        from menuhandler import MenuHandler
        self.menu_handler = MenuHandler(self)
        self.menu_handler.add_window_action('Saisonübersicht', self.menu_handler.show_saison_window)
        self.menu_handler.add_window_action('Erfolgeübersicht', self.menu_handler.show_erfolge_window)
        self.menu_handler.add_window_action('Trainerübersicht', self.menu_handler.show_trainer_window)
        self.menu_handler.add_window_action('Spielerübersicht', self.menu_handler.show_spieler_window)

    def save_spieler(self):
        new_rows = []
        existing_data = self.controller.get_all_spieler()
        existing_ids = {row[0] for row in existing_data}  # Menge der vorhandenen IDs

        for row in range(self.ui.spielerTbl.rowCount()):
            row_data = []
            for column in range(self.ui.spielerTbl.columnCount()):
                item = self.ui.spielerTbl.item(row, column)
                if item and item.text():  # Überprüfen, ob das Item existiert und nicht leer ist
                    row_data.append(item.text())
                else:
                    row_data.append('')  # Leeren Wert hinzufügen, wenn das Item leer ist
            new_rows.append(row_data)

        for index, row in enumerate(new_rows):
            if not row[0]:  # Wenn keine ID vorhanden ist, eine neue vergeben
                new_id = max(existing_ids) + 1 if existing_ids else 1
                new_rows[index][0] = str(new_id)
                existing_ids.add(new_id)

        # Hier löschen wir alle vorhandenen Daten in der Datenbank
        self.controller.delete_spieler()

        if new_rows:
            # Hier werden die neuen Daten validiert und gespeichert
            self.controller.save_spieler(new_rows)

            logging.debug(f'Anzahl der Einträge: {len(new_rows)}')
            logging.debug(f'Neue Daten: {new_rows}')
            logging.debug(f'Daten neu gespeichert: {new_rows}')

        else:
            logging.debug('Keine neuen Daten zum Speichern gefunden.')

        # Aktualisieren Sie die Tabelle, um die neuen Daten anzuzeigen
        self.refresh_table()

    def refresh_table(self):
        spieler_data = self.controller.get_all_spieler()

        self.ui.spielerTbl.setRowCount(len(spieler_data) + 1)  # Eine zusätzliche Zeile hinzufügen
        self.ui.spielerTbl.setColumnCount(9)  # Setzen Sie die Anzahl der Spalten entsprechend Ihrer Datenbanktabelle

        for row_index, row_data in enumerate(spieler_data):
            for column_index, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.ui.spielerTbl.setItem(row_index, column_index, item)

        #Entfernen der Zeilennummerierung
        self.ui.spielerTbl.verticalHeader().setVisible(False)

        # Vertikale Ausrichtung der Zeileninhalte zentrieren
        for row in range(self.ui.spielerTbl.rowCount()):
            for column in range(self.ui.spielerTbl.columnCount()):
                item = self.ui.spielerTbl.item(row, column)
                if item:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)

    # Überschreiben der keyPressEvent-Methode, um auf die Tab-Taste zu reagieren
    # Vorhandene keyPressEvent-Methode um die Entf-Taste erweitern
    def custom_keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            current_row = self.ui.spielerTbl.currentRow()
            current_col = self.ui.spielerTbl.currentColumn()
            if current_col == self.ui.spielerTbl.columnCount() - 1 and current_row == self.ui.spielerTbl.rowCount() - 1:
                # Fügen Sie eine neue Zeile hinzu, wenn Tab in der letzten Spalte und letzten Zeile gedrückt wird
                self.ui.spielerTbl.insertRow(self.ui.spielerTbl.rowCount())
                # Setzen Sie den Fokus auf die erste Zelle der neuen Zeile
                self.ui.spielerTbl.setCurrentCell(current_row + 1, 0)
            else:
                # Weiterleitung des keyPressEvent-Ereignisses an die Basisimplementierung
                QtWidgets.QTableWidget.keyPressEvent(self.ui.spielerTbl, event)
        elif event.key() == QtCore.Qt.Key_Delete:  # Hinzufügen für Entf-Taste
            selected_rows = self.ui.spielerTbl.selectedItems()
            if selected_rows:
                rows_to_delete = set(item.row() for item in selected_rows)
                for row in sorted(rows_to_delete, reverse=True):
                    trainer_id = self.ui.spielerTbl.item(row, 0).text()  # Annahme: ID ist in der ersten Spalte
                    self.controller.delete_spieler()
                    self.ui.spielerTbl.removeRow(row)
        else:
            # Weiterleitung des keyPressEvent-Ereignisses an die Basisimplementierung
            QtWidgets.QTableWidget.keyPressEvent(self.ui.spielerTbl, event)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SpielerWindow()
    window.show()
    sys.exit(app.exec_())
