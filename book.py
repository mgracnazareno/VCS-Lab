
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
    

        
