from Database import Database

    # A class that manages book operations, including adding new books

class BookManager:

    # Adds a new book to the Books table
    
    @staticmethod
    def add_book(title, author, genre, year_published):

        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Books (title, author, genre, year_published)
            VALUES (?, ?, ?, ?)
        ''', (title, author, genre, year_published))

        conn.commit()
        conn.close()
        print("Book added.")

# Here we create the information of the attached book, see the line 10 to guide you.

if __name__ == "__main__":
    BookManager.add_book("Sample Book", "Author Name", "Fiction", 2023)
