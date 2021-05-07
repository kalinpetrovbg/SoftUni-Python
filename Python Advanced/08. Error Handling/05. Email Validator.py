# To solve it

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

VALID_DOMAINS = "com", "bg", "org", "net"

def valid_email(e):
    try:
        name, domain = e.split("@")
    except:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    try:
        name, extension = e.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")
    if extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")

    return True


email = input()

while not email == "End":
    if valid_email(email):
        print("Email is valid")
    email = input()
