class Book( object ):
    def __init__( self,  isbn = None, title = "" ):
        self.isbn = isbn
        self.title = title

    def __str__( self ):
        return self.title

    def set_title( self, new_title ):
        self.title = new_title

"""
little_women = Book( "Little Women" )
print ( little_women.title )

little_women.set_title( "Little Women by Louisa May Alcott" )
print( little_women )
"""