from Database import Database

class BookDeleter:
    """Manages the deletion of books."""

    @staticmethod
    def delete_book(id):
        """Delete a book from the Books table by ID."""
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("Book deleted successfully.")

# Example usage
if __name__ == "__main__":
    BookDeleter.delete_book("1")
