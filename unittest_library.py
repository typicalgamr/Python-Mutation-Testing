import unittest
from library import Book, Library

class TestBook(unittest.TestCase):
    def test_borrow(self):
        book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
        self.assertTrue(book.borrow())
        self.assertFalse(book.borrow())  # Already borrowed

    def test_return_book(self):
        book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
        book.borrow()
        self.assertTrue(book.return_book())
        self.assertFalse(book.return_book())  # Already returned

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
        self.assertTrue(library.add_book(book))
        self.assertFalse(library.add_book(book))  # Duplicate ISBN

    def test_remove_book(self):
        library = Library()
        book = Book("1984", "George Orwell", "1234567891")
        library.add_book(book)
        self.assertTrue(library.remove_book("1234567891"))
        self.assertFalse(library.remove_book("1234567891"))  # Already removed

    def test_borrow_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee", "1234567892")
        library.add_book(book)
        self.assertTrue(library.borrow_book("1234567892"))
        self.assertFalse(library.borrow_book("1234567892"))  # Already borrowed

    def test_return_book(self):
        library = Library()
        book = Book("The Catcher in the Rye", "J.D. Salinger", "1234567893")
        library.add_book(book)
        library.borrow_book("1234567893")
        self.assertTrue(library.return_book("1234567893"))
        self.assertFalse(library.return_book("1234567893"))  # Already returned

    def test_search_by_title(self):
        library = Library()
        book1 = Book("The Hobbit", "J.R.R. Tolkien", "1234567894")
        book2 = Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", "1234567895")
        library.add_book(book1)
        library.add_book(book2)
        results = library.search_by_title("hobbit")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Hobbit")

if __name__ == '__main__':
    unittest.main()
