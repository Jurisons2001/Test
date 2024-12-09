from Database import Database

#Šī klase nodrošina funkcionalitāti, lai skatītu visas grāmatas, kas ir saglabātas datubāzē.

class BookViewer:

    @staticmethod
    def view_all_books():
        conn = Database.create_connection()
        cursor = conn.cursor()

#Saņem tabulas kolonnu nosaukumus no datubāzes shēmas.

        cursor.execute("PRAGMA table_info(Books)")
        columns = [col[1] for col in cursor.fetchall()]
        
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()

 #Izdrukā kolonnu nosaukumus kā galveni.
 
        print("\t".join(columns))
        print("-" * 50)

 #Izdrukā katru grāmatas ierakstu rindu.

        for row in rows:
            print("\t".join(map(str, row)))

        conn.close()

if __name__ == "__main__":
    BookViewer.view_all_books()
