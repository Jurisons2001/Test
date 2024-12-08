from Database import Database

#Šī klase nodrošina funkcionalitāti grāmatas dzēšanai no datubāzes, izmantojot tās ID.

class BookDeleter:

#Izveido savienojumu ar datubāzi.

    @staticmethod
    def delete_book(book_id):
        conn = Database.create_connection()
        cursor = conn.cursor()

#Izpilda SQL pieprasījumu, lai izdzēstu grāmatu ar norādīto ID.

        cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        print(f"Book with ID {book_id} deleted successfully.")

if __name__ == "__main__":

#Norāda grāmatas ID, kuru vēlaties izdzēst.
#Nomainiet '1' uz nepieciešamo grāmatas ID.
    BookDeleter.delete_book(1)
