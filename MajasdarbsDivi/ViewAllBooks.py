from Database import Database

class BookViewer:
    """Provides methods to view book information."""

    @staticmethod
    def view_all_books():
        """Fetch and display all books from the Books table."""
        
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

# Example usage
if __name__ == "__main__":
    BookViewer.view_all_books()
