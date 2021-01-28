def abs_numbers(list_numbers):
    return list(map(abs, list_numbers))

numbers = [float(x) for x in input().split()]
print(abs_numbers(numbers))