from user import User

class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def __init__(self):
        pass

    def add_user(self, user):
        if user in Library.user_records:
            return f"User with id = {user.id} already registered in the library!"
        Library.user_records.append(user)

    def remove_user(self, user):
        if user not in Library.user_records:
            return "We could not find such user to remove!"
        Library.user_records.remove(user)

    def change_username(self, user_id, new_username):
        try:
            is_in = [u for u in User if u.user_id == user_id][0]
            if is_in.username == new_username:
                return f"Please check again the provided username - " \
                       f"it should be different than the username used so far!"
            is_in.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {is_in.user_id}"
        except IndexError:
            return f"There is no user with id = {user_id}!"
