def tags(tag):
    def inner(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return inner


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
