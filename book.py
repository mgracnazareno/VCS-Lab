
class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
    
    
    
    @classmethod
    def change_library_new(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        if(len(title.strip()) == 0):
            return True
        else:
            return False
        
    # instance methods
    def borrow(self):
        if(self.available == True):
            print(f"{self.title} Borrowed! ")
        else:
            self.available = False
            print(f"{self.title} has been borrowed.")

    def return_book(self):
        if(self.available == False):
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not borrowed")
    
    def display_info(self):
        # print(f"Title: {self.title} availability: {self.available}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {self.available}")
        
