def type_check(value):
    def inner(func):
        def wrapper(*args):
            for a in args:
                if type(a) != value:
                    return "Bad Type"
            result = func(*args)
            return result
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
