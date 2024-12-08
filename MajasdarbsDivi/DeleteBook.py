from Database import Database

class BookDeleter:

    @staticmethod
    def delete_book(book_id):
        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        print(f"Book with ID {book_id} deleted successfully.")

if __name__ == "__main__":
    # Replace 1 with the ID of the book you want to delete
    BookDeleter.delete_book(1)
