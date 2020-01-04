#!/usr/bin/env python3
import Library
import sys
import pickle

with  open( "my_library_file.pickle", "rb" ) as my_file:
    my_library = pickle.load ( my_file )

print("Please enter an isbn number: ")
isbn = sys.stdin.readline()
isbn = isbn.strip()

my_library.add_book(isbn)
print(my_library.books[0])

with open( "my_library_file.pickle", "wb" ) as my_file:
    pickle.dump( my_library, my_file )
