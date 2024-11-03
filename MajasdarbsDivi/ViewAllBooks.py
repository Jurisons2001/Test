from Database import Database

# This class provides methods for viewing book information
# Method that gets and displays all books from the Books table

class BookViewer:

    @staticmethod
    def view_all_books():

        conn = Database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()


if __name__ == "__main__":
    BookViewer.view_all_books()
