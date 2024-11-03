from Database import Database

# This class manages the deletion of books

class BookDeleter:

# The method that deletes a book from the Books table by ID can also be changed and put another parameter.    

    @staticmethod
    def delete_book(id):
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Books WHERE id = ?", (id,))
        conn.commit()

        conn.close()
        print("Book deleted.")

# ID must be an integer value

if __name__ == "__main__":
    BookDeleter.delete_book(1)  
