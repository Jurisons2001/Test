from Database import Database

class BookViewer:

    @staticmethod
    def view_all_books():
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(Books)")
        columns = [col[1] for col in cursor.fetchall()]
        
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()

        # Print column headers
        print("\t".join(columns))
        print("-" * 50)

        # Print rows
        for row in rows:
            print("\t".join(map(str, row)))

        conn.close()

if __name__ == "__main__":
    BookViewer.view_all_books()
