from project.user import User


class Library:
    def __init__(self):
        self.user_records: 'user objects' = []
        self.books_available: '{authors: [books]}' = {}
        self.rented_books: '{usernames: {book names: days left}}' = {}
        self.days_to_return_book: '{book_name: [days]}' = {}
        self.user_ids: '{user_id: user}' = {}

    def add_user(self, user):
        if user in self.user_records:
            return f'User with id = {user.user_id} already registered in the library!'
        self.user_records.append(user)
        self.user_ids[user.user_id] = user

    def remove_user(self, user: 'User'):
        if user not in self.user_records:
            return 'We could not find such user to remove!'
        self.user_ids.pop(user.user_id)
        self.user_records.remove(user)

    def change_username(self, user_id, new_username):
        try:
            user = self.user_ids.get(user_id)
            if user.username == new_username:
                return 'Please check again the provided username - it should be different than the username used so far!'
            user.username = new_username
            return f'Username successfully changed to: {user.username} for userid: {user_id}'
        except AttributeError:
            return f'There is no user with id = {user_id}!'


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
