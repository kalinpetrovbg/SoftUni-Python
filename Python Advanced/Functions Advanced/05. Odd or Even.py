def calculate_odd(nums):
    result = list(filter(lambda x: x % 2 != 0, nums))
    return sum(result) * len(nums)

def calculate_even(nums):
    result = list(filter(lambda x: x % 2 == 0, nums))
    return sum(result) * len(nums)

def odd_vs_even(comm):
    if comm == "Odd":
        return calculate_odd(numbers)
    elif comm == "Even":
        return calculate_even(numbers)

command = input()
numbers = [int(num) for num in input().split()]

print(odd_vs_even(command))
