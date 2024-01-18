class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    books = []
    borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        try:
            for book in self.books:
                if book.title == book_title:
                    self.books.remove(book)
                    print("Livre effacée de la liste.")
                else:
                    raise Exception("Livre introuvable.")
        except Exception as e:
            print(e)

    def borrow_book(self, book_title):
        try:
            for book in self.books:
                if book.title == book_title:
                    self.borrow_book.append(book)
                    self.books.remove(book)
                    print("Livre déplacée dans la liste des livres                           empruntées")
                else:
                    raise Exception("Livre introuvable.")
        except Exception as e:
            print(e)

    def return_book(self, book_title):
        try:
            for book in self.books:
                if book.title == book_title:
                    self.books.append(book)
                    self.borrow_book.remove(book)
                    print("Livre déplacée dans la liste des livres                           empruntées")
                else:
                    raise Exception("Livre introuvable.")
        except Exception as e:
            print(e)

    def availble_books(self):
        print("\nListe des livres : \n")
        for book in self.books:
            print(f"{book.title} - {book.author} - {book.year}")

    def borrowed_books(self):
        print("\nListe des livres : \n")
        for book in self.borrow_books:
            print(f"{book.title} - {book.author} - {book.year}")


book = Book("La Parure", "Frankestine Due", 2003)
book2 = Book("Folie et Art", "Lourd Tempest", 2009)
book3 = Book("Maths en furie", "Potrin Louis", 2015)

library = Library()

library.add_book(book)
library.add_book(book2)
library.add_book(book3)

library.borrow_book("La Parure")
library.availble_books()
library.borrowed_books()
library.return_book("La Parure")
library.availble_books()
library.borrowed_books()

library.borrow_book("La Parue")
library.return_book("La Parue")
