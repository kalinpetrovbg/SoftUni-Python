def multiply(n):
    def inner(function):
        def decorator(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * n
        return decorator
    return inner


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
