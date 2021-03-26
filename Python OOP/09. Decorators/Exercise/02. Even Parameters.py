def even_parameters(function):
    def wrapper(*args):
        for a in args:
            if not isinstance(a, int) or a % 2 != 0:
                return "Please use only even numbers!"
        result = function(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


@even_parameters
def func():
    return "hi"

print(func())

