from Database import Database

class BookManager:

    @staticmethod
    def add_book(title, author, genre, year_published, publisher=None, rating=None, language=None):
        conn = Database.create_connection()
        cursor = conn.cursor()

        # Insert query to handle both mandatory and optional columns
        cursor.execute('''
            INSERT INTO Books (title, author, genre, year_published, publisher, rating, language)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, genre, year_published, publisher, rating, language))

        conn.commit()
        conn.close()
        print("Book added successfully.")

if __name__ == "__main__":
    BookManager.add_book(
        "Sample Book", 
        "Author Name", 
        "Fiction", 
        2023, 
        publisher="Sample Publisher", 
        rating=4.5, 
        language="English"
    )
