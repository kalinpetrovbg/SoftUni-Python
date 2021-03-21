def min_num(nums):
    return f"The minimum number is {min(nums)}"

def max_num(nums):
    return f"The maximum number is {max(nums)}"

def sum_nums(nums):
    return f"The sum number is: {sum(nums)}"

nums = [int(n) for n in input().split()]

print(min_num(nums))
print(max_num(nums))
print(sum_nums(nums))