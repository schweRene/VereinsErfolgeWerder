import sqlite3

class WerderDatabase:
    def __init__(self, db_name='werder.db'):
        #Verbindung zur Datenbank herstellen
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Erfolge
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Titel VARCHAR(70),
                            Jahr INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Trainer
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Vorname VARCHAR(255),
                            Nachname VARCHAR(255),
                            Von INTEGER,
                            Bis INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Saisons
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Saison INTEGER,
                            Platz INTEGER,
                            Siege INTEGER,
                            Unentschieden INTEGER,
                            Niederlagen INTEGER,
                            Tore VARCHAR(255),
                            Tordifferenz INTEGER,
                            Punkte INTEGER,
                            Liga VARCHAR(255))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Spieler
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Vorname VARCHAR(255),
                            Nachname VARCHAR(255),
                            Nationalität VARCHAR(255),
                            Von INTEGER,
                            Bis INTEGER,
                            Ligaspiele INTEGER,
                            Ligatore INTEGER,
                            Position VARCHAR(255))''')

        #Änderungen speichern und Verbindung schließen
        self.conn.commit()

if __name__ == '__main__':
    db = WerderDatabase()
    db.create_tables()