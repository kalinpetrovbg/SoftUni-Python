class ValueCannotBeNegative(Exception):
    pass

numbers = [1, 2, 4, 7, -4, 5, 0]

for num in numbers:
    if num > 0:
        print(num)
    else:
        raise ValueCannotBeNegative

