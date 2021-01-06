def sum_numbers(one_, two_):
    return one_ + two_


def add_and_subtract(one, two, three):
    result1 = sum_numbers(one, two)
    return result1 - three


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
