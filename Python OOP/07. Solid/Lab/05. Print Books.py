from abc import ABC, abstractmethod

class Book:
    def __init__(self, name, author, content):
        self.name = name
        self.author = author
        self.content = content

class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass

class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content

class AuthorFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.author


class Printer:
    def print(self, book: Book, formatter: Formatter):
        return formatter.format(book)

book = Book("Title of the book", "John Levine", "Content of the book")
printer = Printer()

print(printer.print(book, AuthorFormatter()))
print(printer.print(book, ContentFormatter()))