import sqlite3
import logging

class TrainerController:
    def __init__(self, database_name):
        self.db_name = database_name
        self.create_table()
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS trainer
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             Vorname VARCHAR(255),
             Nachname VARCHAR(255),
             Von INTEGER,
             Bis INTEGER)'''
                  )
        conn.commit()
        conn.close()

    def save_trainer(self, trainer_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        for data_row in trainer_data:
            c.execute('''
                INSERT INTO trainer(Vorname, Nachname, Von, Bis)
                VALUES(?, ?, ?, ?)''', data_row[1:])
        conn.commit()
        conn.close()

    def delete_trainer(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM trainer")
        conn.commit()
        conn.close()

    def get_all_trainer(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM trainer")
        data = c.fetchall()
        conn.close()
        return data
