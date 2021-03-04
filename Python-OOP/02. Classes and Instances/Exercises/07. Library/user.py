class User:
    books = []

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in Library.rented_books.items():
            return f"The book \"{book_name}\" is already rented and will be available in {days_to_return} days!"
        if book_name not in Library.books_available.items():
            pass
        if book_name in Library.books_available.items():
            Library.books_available[book_name] = author
            Library.rented_books[book_name] = author
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        del Library.books_available[book_name]
        del Library.rented_books[book_name]
        self.books.remove(book_name)

    def info(self):
        return ", ".join(self.books)


from library import Library

user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
