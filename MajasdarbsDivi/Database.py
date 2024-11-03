import sqlite3
import json

# Load configuration from an external confg file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

class Database:
    """Handles database connection and setup."""

    @staticmethod
    def create_connection():
        """Establish a connection to the Books database."""
        return sqlite3.connect(config["database_path"])

    @staticmethod
    def create_table():
        """Create the Books table if it doesn't exist."""
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT,
                year_published INTEGER,
                isbn TEXT UNIQUE,
                available_copies INTEGER
            )
        ''')
        conn.commit()
        conn.close()

# Initialize the database table
if __name__ == "__main__":
    Database.create_table()
