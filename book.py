
class Book:
    library_name = "Central Library"
    count = 0

    def __init__(self, title, author, available = True, genre="Unknown"):
        self.title = title
        self.author = author
        self.available = available
        self.genre = genre
        Book.count += 1
    
    @classmethod
    def show_count(cls):
        print(f"Total books: {cls.count}")
    
    @classmethod
    def change_library_name(cls, new_name):
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

    @classmethod
    def from_string(cls, data):
        title, author, available, genre = data.split(",")
        return cls(title, author , available, genre)
    
    def display_info(self):
        # print(f"[{self.library_name}] {self.title} by {self.author} - Available {self.available}")
        print(f"Title: {self.title} ")
        print(f"Author: {self.title}")
        print(f"Availability: {self.available}")
        print(f"Genre: {self.genre}" )
        # print(f"Availability: {self.available}")
        
