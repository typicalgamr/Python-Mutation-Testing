import pytest
from library import Book, Library

def test_add_book():
    library = Library()
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    assert library.add_book(book) is True
    assert library.add_book(book) is False  # Duplicate ISBN

def test_remove_book():
    library = Library()
    book = Book("1984", "George Orwell", "1234567891")
    library.add_book(book)
    assert library.remove_book("1234567891") is True
    assert library.remove_book("1234567891") is False  # Already removed

def test_borrow_book():
    library = Library()
    book = Book("To Kill a Mockingbird", "Harper Lee", "1234567892")
    library.add_book(book)
    assert library.borrow_book("1234567892") is True
    assert library.borrow_book("1234567892") is False  # Already borrowed

def test_return_book():
    library = Library()
    book = Book("The Catcher in the Rye", "J.D. Salinger", "1234567893")
    library.add_book(book)
    library.borrow_book("1234567893")
    assert library.return_book("1234567893") is True
    assert library.return_book("1234567893") is False  # Already returned

def test_search_by_title():
    library = Library()
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "1234567894")
    book2 = Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", "1234567895")
    library.add_book(book1)
    library.add_book(book2)
    results = library.search_by_title("hobbit")
    assert len(results) == 1
    assert results[0].title == "The Hobbit"
