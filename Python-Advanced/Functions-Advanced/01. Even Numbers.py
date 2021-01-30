def even_numbers(list_nums):
    return list(filter(lambda x: x % 2 == 0, list_nums))

numbers = [int(num) for num in input().split()]

print(even_numbers(numbers))