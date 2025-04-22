class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books by ISBN
        self.borrowed_books = []  # List to keep track of borrowed books

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            return True
        return False  # Book with same ISBN already exists

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False  # Book not found

    def borrow_book(self, isbn):
        book = self.books.get(isbn)
        if book and book.borrow():
            self.borrowed_books.append(isbn)
            return True
        return False  # Book not available or already borrowed

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if book and book.return_book():
            self.borrowed_books.remove(isbn)
            return True
        return False  # Book was not borrowed

    def search_by_title(self, title):
        return [book for book in self.books.values() if title.lower() in book.title.lower()]
