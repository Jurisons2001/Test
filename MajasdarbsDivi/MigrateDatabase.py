from Database import Database
import sqlite3

    # Class that manages database migrations

class DatabaseMigrator:

    # Adds a new 'self-selected' column to the Books table if it doesn't exist
    # To add another name, instead of "publisher" in the code, we write the column name of our choice
    # after execution, the "AddToDatabase" file add_book method must be updated so that a new book can be added
    
    @staticmethod
    def migrate():
        conn = Database.create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''ALTER TABLE Books ADD COLUMN publisher TEXT''')
            conn.commit()
            print("New column 'publisher' added to table Books.")

        except sqlite3.OperationalError:
            print("Column 'publisher' already exists.")

        finally:
            conn.close()

if __name__ == "__main__":
    DatabaseMigrator.migrate()
