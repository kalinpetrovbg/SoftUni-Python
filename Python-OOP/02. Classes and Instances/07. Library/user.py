class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library: 'Library'):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            if self.username not in library.rented_books.keys():
                library.rented_books[self.username] = {}
            library.rented_books[self.username].update({book_name: days_to_return})
            library.days_to_return_book[book_name] = days_to_return
            library.books_available[author].remove(book_name)
            return f'{book_name} successfully rented for the next {days_to_return} days!'
        return f'The book "{book_name}" is already rented and ' \
               f'will be available in {library.days_to_return_book[book_name]} days!'

    def return_book(self, author, book_name, library: 'Library'):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.rented_books[self.username].pop(book_name)
        library.days_to_return_book.pop(book_name)
        library.books_available[author].append(book_name)
        self.books.remove(book_name)

    def info(self):
        return f'{", ".join(sorted(self.books))}'

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'
