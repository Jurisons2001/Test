from Database import Database

class BookManager:
    """Manages book operations, including adding news books."""

    @staticmethod
    def add_book(title, author, genre, year_published, isbn, available_copies):
        """Add a new book to the Books table."""
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Books (title, author, genre, year_published, isbn, available_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, author, genre, year_published, isbn, available_copies))
        conn.commit()
        conn.close()
        print("Book added successfully.")

# Example usage
if __name__ == "__main__":
    BookManager.add_book("Sample Book", "Author Name", "Fiction", 2023, "122234567890", 5)
