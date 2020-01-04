#!/usr/bin/env python3
import Library
import sys
import pickle


my_library = pickle.load( open( "my_library_file.pickle", "rb" ) )


print("your library:\n")

for book in my_library.books :
    print( book.title )
