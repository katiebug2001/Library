import Library
import sys

print("Please enter an isbn number: ")
isbn = sys.stdin.readline()
isbn = isbn.strip()

my_library = Library.Library()

my_library.add_book(isbn)
print(my_library.books[0])