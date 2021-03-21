class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, books):
        self.books = list(books)

    def find_book(self, title):
        found = [b for b in self.books if b.title == title][0]
        return found