import sqlite3
import logging

class ErfolgeController:
    def __init__(self, database_name):
        self.db_name = database_name
        self.create_table()
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Erfolge
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Titel VARCHAR(70),
            Jahr INTEGER)''')
        conn.commit()
        conn.close()

    def save_erfolge(self, erfolge_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for data_row in erfolge_data:
            c.execute('''
                INSERT INTO Erfolge (Titel, Jahr)
                VALUES (?, ?)''', data_row[1:])
        conn.commit()
        conn.close()

    def delete_erfolge(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM Erfolge")
        conn.commit()
        conn.close()

    def get_all_erfolge(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM Erfolge")
        data = c.fetchall()
        conn.close()
        return data
