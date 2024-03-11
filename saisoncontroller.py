import sqlite3
import logging

class SaisonController:
    def __init__(self, database_name):
        self.db_name = database_name
        self.create_table()
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Saisons
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Saison INTEGER,
            Platz INTEGER,
            Siege INTEGER,
            Unentschieden INTEGER,
            Niederlagen INTEGER,
            Tore Varchar(255),
            Tordifferenz INTEGER,
            Punkte INTEGER,
            Liga VARCHAR(255))'''
        )
        conn.commit()
        conn.close()

    def save_saison(self, saison_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for data_row in saison_data:
            c.execute('''
                INSERT INTO Saisons (Saison, Platz, Siege, Unentschieden, Niederlagen, Tore, Tordifferenz, Punkte, Liga)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', data_row[1:])
        conn.commit()
        conn.close()

    def delete_saison(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM Saisons")
        conn.commit()
        conn.close()

    def get_all_saison(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM Saisons")
        data = c.fetchall()
        conn.close()
        return data
