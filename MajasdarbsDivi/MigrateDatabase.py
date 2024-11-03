from Database import Database
import sqlite3

class DatabaseMigrator:

    @staticmethod
    def migrate():
        conn = Database.create_connection()
        cursor = conn.cursor()
        
        # Add a new column 'publisher' to the Books table if it doesn't already exist
        try:
            cursor.execute('''ALTER TABLE Books ADD COLUMN deleted TEXT''')
            conn.commit()
            print("Database migration completed successfully.")

        except sqlite3.OperationalError:
            print("Column 'deleted' already exists.")

        finally:
            conn.close()

# Run the migration
if __name__ == "__main__":
    DatabaseMigrator.migrate()
