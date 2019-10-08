import unittest
import Book
from apiclient.discovery import build


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, isbn):
        assert isbn.isdigit() and ( ( isbn.__len__() == 10 ) or ( isbn.__len__() == 13 ) )

        api_key = "AIzaSyC7HJG5DAiaexvwspVkJaxG0KJzhoGdHes"
        service = build('books', 'v1', developerKey=api_key)
        request = service.volumes().list(source="public", q="isbn: " + isbn)
        response = request.execute()
        book = response['items'][0]

        self.books.append(Book.Book(isbn, book["volumeInfo"]["title"]))



class test_Library(unittest.TestCase):
    def test_init(self):
        test_library = Library()
        test_library.add_book("9780547928203")
        self.assertEqual("The Two Towers", test_library.books[0].title)


if __name__ == "__main__":
    unittest.main()