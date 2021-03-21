def size(number):
    if 6 <= len(number) <= 10:
        return True
    else:
        return False


def nums_char(number):
    for char in number:
        if not char.isalnum():
            return False
    return True


def counters(number):
    counter = 0
    for char in number:
        if char.isdigit():
            counter += 1
    if counter >= 2:
        return True
    else:
        return False


text = input()

if not size(text):
    print(f"Password must be between 6 and 10 characters")
if not nums_char(text):
    print("Password must consist only of letters and digits")
if not counters(text):
    print(f"Password must have at least 2 digits")
if size(text) and nums_char(text) and counters(text):
    print("Password is valid")