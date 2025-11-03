#Klasa Książka
class Book:
    # Inicjalizacja obiektu książki
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    # Wypożyczenie książki
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"Książka '{self.title}' została wypożyczona."
        else:
            return f"Książka '{self.title}' jest już wypożyczona."

    # Zwrócenie książki
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Książka '{self.title}' została zwrócona."
        else:
            return f"Książka '{self.title}' nie była wypożyczona."


#Klasa Biblioteka
class Library:
    # Inicjalizacja biblioteki
    def __init__(self):
        self.books = [
            Book("Song of Ice and Fire", "George R.R. Martin", 1996, False),
            Book("Call of Cthulhu", "H.P. Lovecraft", 1928),
            Book("The Hobbit", "J.R.R. Tolkien", 1937)
        ]

    # Dodanie nowej książki do biblioteki
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} dodano do biblioteki.")

    # Wyświetlenie wszystkich książek
    def list_books(self):
        if not self.books:
            print("Biblioteka jest pusta.")
        else:
            print("\nLista książek w bibliotece:")
            for i, book in enumerate(self.books, start=1):
                status = "dostępna" if book.is_available else "wypożyczona"
                print(f"{i}. {book.title} – {book.author} ({book.year}) [{status}]")

    # Wypożyczenie książki
    def borrow_book(self):
        if not self.books:
            print("Brak książek w bibliotece.")
            return

        print("\n=== WYPOŻYCZ KSIĄŻKĘ ===")
        self.list_books()  
        try:
            choice = int(input("\nPodaj numer książki do wypożyczenia: "))
            if 1 <= choice <= len(self.books):
                book = self.books[choice - 1]
                print(book.borrow_book())
            else:
                print("Nieprawidłowy numer.")
        except ValueError:
            print("Musisz wpisać liczbę.")

    # Zwrócenie książki 
    def return_book(self):
        if not self.books:
            print("Brak książek w bibliotece.")
            return

        print("\n=== ZWRÓĆ KSIĄŻKĘ ===")
        self.list_books()  
        try:
            choice = int(input("\nPodaj numer książki do zwrotu: "))
            if 1 <= choice <= len(self.books):
                book = self.books[choice - 1]
                print(book.return_book())
            else:
                print("Nieprawidłowy numer.")
        except ValueError:
            print("Musisz wpisać liczbę.")

    # Wyszukiwanie książek po tytule lub autorze
    def search_books(self):
        if not self.books:
            print("Biblioteka jest pusta.")
            return

        keyword = input("Wpisz tytuł lub autora do wyszukania: ").lower()
        found_books = [
            book for book in self.books
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

        if found_books:
            print("\nZnalezione książki:")
            for i, book in enumerate(found_books, start=1):
                status = "dostępna" if book.is_available else "wypożyczona"
                print(f"{i}. {book.title} – {book.author} ({book.year}) [{status}]")
        else:
            print("Nie znaleziono żadnych książek pasujących do wyszukiwania.")

    
