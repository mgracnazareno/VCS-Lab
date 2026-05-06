
class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
    
    def 
    
    @classmethod
    def change_library_new(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        if(len(title.strip()) == 0):
            return True
        else:
            return False
