from library import Book, Library

def main():
    library = Library()

    while True:
        print("\n=== SYSTEM BIBLIOTECZNY ===")
        print("1. Dodaj książkę")
        print("2. Wyświetl książki")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Wyszukaj książkę")
        print("6. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok wydania: ")
            library.add_book(Book(title, author, year))

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            library.borrow_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.search_books()

        elif choice == "6":
            print("Zamykanie programu...")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
