
class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
    
    @classmethod
    def change_library_new(cls, new_name):
        cls.library_name = new_name
        
        
