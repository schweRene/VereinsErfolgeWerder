import sqlite3
import logging

class SpielerController:
    def __init__(self, database_name):
        self.db_name = database_name
        self.create_table()
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Spieler
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Vorname VARCHAR(255),
            Nachname VARCHAR(255),
            Nationalität VARCHAR(255),
            Von INTEGER,
            Bis INTEGER,
            Ligaspiele INTEGER,
            Ligatore INTEGER,
            Position VARCHAR(255))'''
        )
        conn.commit()
        conn.close()

    def save_spieler(self, spieler_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for data_row in spieler_data:
            c.execute('''
                INSERT INTO Saisons (Vorname, Nachname, Nationalität, Von, Bis, Ligaspiele, Ligatore, Position)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data_row[1:])
        conn.commit()
        conn.close()

    def delete_spieler(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM Spieler")
        conn.commit()
        conn.close()

    def get_all_spieler(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM Spieler")
        data = c.fetchall()
        conn.close()
        return data
