import sqlite3
import json

#Šī klase nodrošina funkcionalitāti datubāzes savienojuma izveidei un tabulu pārvaldībai.

#Ielādē konfigurācijas failu, lai iegūtu datubāzes ceļu.

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

DATABASE_PATH = config["database_path"]

class Database:

    @staticmethod
    def create_connection():
        return sqlite3.connect(DATABASE_PATH)

#Izveido tabulu 'Books', ja tā vēl neeksistē. Tabulas struktūra ir piemērota grāmatu uzglabāšanai.

    @staticmethod
    def create_table():
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT,
                year_published INTEGER
            )
        ''')
        conn.commit()
        conn.close()

if __name__ == "__main__":
    Database.create_table()
