
class Book:

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
    
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
        print(f"{self.title} availability: {self.available}")
        
