from book import Book


# create at least 2 book objects
book1 = Book("Python Programming", "Tony Gaddis", False)
book2 = Book("Verite", "Colleen Hover", True)

#print attribute values
print(f"-- Book 1 --")
print(f" {book1.title}")
print(f" {book1.author}")
print(f" {book1.available}")

print(f"-- Book 2 --")
print(f" {book2.title}")
print(f" {book2.author}")
print(f"{book2.available}")


book1.borrow()
book2.borrow()

book1.return_book()
book2.return_book()