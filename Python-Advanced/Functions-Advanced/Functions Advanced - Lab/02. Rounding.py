def round_numbers(list_nums):
    return list(map(round, list_nums))

nums = map(float, input().split())
print(round_numbers(nums))