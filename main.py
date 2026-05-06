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


print(f"\n -- Book Status  Borrowed --")
book1.borrow()
book2.borrow()

print(f"\n -- Book Status  Returned--")
book1.return_book()
book2.return_book()
print("\n-- Book Info --")
book1.display_info()
print()
book2.display_info()

