from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAction

from erfolge import Ui_ErfolgeWindow
from erfolgecontroller import ErfolgeController
from PyQt5 import QtWidgets, QtCore
import logging


class ErfolgeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ErfolgeWindow()
        self.ui.setupUi(self)

        self.db_name = "werder.db"
        self.controller = ErfolgeController(self.db_name)

        self.ui.saveBtn.clicked.connect(self.save_erfolge)

        self.refresh_table()

        # Verbinden Sie das keyPressEvent-Ereignis des TableWidgets
        self.ui.erfolgeTbl.keyPressEvent = self.custom_keyPressEvent

        from menuhandler import MenuHandler
        self.menu_handler = MenuHandler(self)
        self.menu_handler.add_window_action('Saisonübersicht', self.menu_handler.show_saison_window)
        self.menu_handler.add_window_action('Erfolgeübersicht', self.menu_handler.show_erfolge_window)
        self.menu_handler.add_window_action('Trainerübersicht', self.menu_handler.show_trainer_window)
        self.menu_handler.add_window_action('Spielerübersicht', self.menu_handler.show_spieler_window)




    def save_erfolge(self):
        new_rows = []
        existing_data = self.controller.get_all_erfolge()
        existing_ids = {row[0] for row in existing_data}  # Menge der vorhandenen IDs

        for row in range(self.ui.erfolgeTbl.rowCount()):
            row_data = []
            for column in range(self.ui.erfolgeTbl.columnCount()):
                item = self.ui.erfolgeTbl.item(row, column)
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
        self.controller.delete_erfolge()

        if new_rows:
            # Hier werden die neuen Daten validiert und gespeichert
            self.controller.save_erfolge(new_rows)

            logging.debug(f'Anzahl der Einträge: {len(new_rows)}')
            logging.debug(f'Neue Daten: {new_rows}')
            logging.debug(f'Daten neu gespeichert: {new_rows}')

        else:
            logging.debug('Keine neuen Daten zum Speichern gefunden.')

        # Aktualisieren Sie die Tabelle, um die neuen Daten anzuzeigen
        self.refresh_table()

    def refresh_table(self):
        erfolge_data = self.controller.get_all_erfolge()

        self.ui.erfolgeTbl.setRowCount(len(erfolge_data) + 1)  # Eine zusätzliche Zeile hinzufügen
        self.ui.erfolgeTbl.setColumnCount(3)  # Setzen Sie die Anzahl der Spalten entsprechend Ihrer Datenbanktabelle

        for row_index, row_data in enumerate(erfolge_data):
            for column_index, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.ui.erfolgeTbl.setItem(row_index, column_index, item)

        #Entfernen der Zeilennummerierung
        self.ui.erfolgeTbl.verticalHeader().setVisible(False)

        # Vertikale Ausrichtung der Zeileninhalte zentrieren
        for row in range(self.ui.erfolgeTbl.rowCount()):
            for column in range(self.ui.erfolgeTbl.columnCount()):
                item = self.ui.erfolgeTbl.item(row, column)
                if item:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)

    # Überschreiben der keyPressEvent-Methode, um auf die Tab-Taste zu reagieren
    # Vorhandene keyPressEvent-Methode um die Entf-Taste erweitern
    def custom_keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            current_row = self.ui.erfolgeTbl.currentRow()
            current_col = self.ui.erfolgeTbl.currentColumn()
            if current_col == self.ui.erfolgeTbl.columnCount() - 1 and current_row == self.ui.erfolgeTbl.rowCount() - 1:
                # Fügen Sie eine neue Zeile hinzu, wenn Tab in der letzten Spalte und letzten Zeile gedrückt wird
                self.ui.erfolgeTbl.insertRow(self.ui.erfolgeTbl.rowCount())
                # Setzen Sie den Fokus auf die erste Zelle der neuen Zeile
                self.ui.erfolgeTbl.setCurrentCell(current_row + 1, 0)
            else:
                # Weiterleitung des keyPressEvent-Ereignisses an die Basisimplementierung
                QtWidgets.QTableWidget.keyPressEvent(self.ui.erfolgeTbl, event)
        elif event.key() == QtCore.Qt.Key_Delete:  # Hinzufügen für Entf-Taste
            selected_rows = self.ui.erfolgeTbl.selectedItems()
            if selected_rows:
                rows_to_delete = set(item.row() for item in selected_rows)
                for row in sorted(rows_to_delete, reverse=True):
                    erfolge_id = self.ui.erfolgeTbl.item(row, 0).text()  # Annahme: ID ist in der ersten Spalte
                    self.controller.delete_erfolge()
                    self.ui.erfolgeTbl.removeRow(row)
        else:
            # Weiterleitung des keyPressEvent-Ereignisses an die Basisimplementierung
            QtWidgets.QTableWidget.keyPressEvent(self.ui.erfolgeTbl, event)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ErfolgeWindow()
    window.show()
    sys.exit(app.exec_())
