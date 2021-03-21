class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, books):
        self.books = list(books)

    def find_book(self, title):
        found = [b for b in self.books if b.title == title][0]
        return f"Book found: {found.title}"

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)


a = Book("History", "Kalin Petrov")
b = Book("Math", "Kalin Petrov")
c = Book("Spanish", "Kalin Petrov")

lib = Library([])

lib.add_book(a)
lib.add_book(b)
lib.add_book(c)

print(lib.find_book("Spanish"))