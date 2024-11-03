import sqlite3
import json

# Load configuration from external configuration file

with open('config.json', 'r') as config_file:
    config = json.load(config_file)


class Database:

# Connects to the book database

    @staticmethod
    def create_connection():
        return sqlite3.connect(config["database_path"])


# Creates the table Books, if it does not exist, you can add or subtract cells of your choice

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

# Closes the cursor and database connection session.

        conn.commit()
        conn.close()


if __name__ == "__main__":
    Database.create_table()
