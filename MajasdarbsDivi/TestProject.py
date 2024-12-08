import sys
from Database import Database
from AddToDatabase import BookManager
from DeleteBook import BookDeleter
from ViewAllBooks import BookViewer

def test_database_connection():
    try:
        conn = Database.create_connection()
        conn.cursor()
        conn.close()
        print("Database connection: SUCCESS")
        return True
    except Exception as e:
        print(f"Database connection: FAILED - {e}")
        return False

def test_create_table():
    try:
        Database.create_table()
        print("Table creation: SUCCESS")
        return True
    except Exception as e:
        print(f"Table creation: FAILED - {e}")
        return False

def test_add_book():
    try:
        BookManager.add_book(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            year_published=2024,
            publisher="Test Publisher",
            rating=5.0,
            language="English"
        )
        print("Adding book: SUCCESS")
        return True
    except Exception as e:
        print(f"Adding book: FAILED - {e}")
        return False

def test_view_books():
    try:
        print("Books in database:")
        BookViewer.view_all_books()
        print("Viewing books: SUCCESS")
        return True
    except Exception as e:
        print(f"Viewing books: FAILED - {e}")
        return False

def test_delete_book():
    try:
        BookDeleter.delete_book(2)  # Delete book with ID 1 (adjust if needed)
        print("Deleting book: SUCCESS")
        return True
    except Exception as e:
        print(f"Deleting book: FAILED - {e}")
        return False

if __name__ == "__main__":
    tests = [
        test_database_connection,
        test_create_table,
        test_add_book,
        test_view_books,
        test_delete_book
    ]

    success = True

    for test in tests:
        if not test():
            success = False

    if success:
        print("All tests passed.")
        sys.exit(0)  # Success
    else:
        print("Some tests failed.")
        sys.exit(1)  # Failure
