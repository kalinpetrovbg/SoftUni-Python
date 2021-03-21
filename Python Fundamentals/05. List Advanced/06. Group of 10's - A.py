import math

integers_list = input().split(',')
numbers = [int(el) for el in integers_list]

for i in range(math.ceil(max(numbers) / 10)):
    group = [num for num in numbers if i * 10 < num <= (i + 1) * 10]
    print(f"Group of {(i + 1) * 10}'s: {group}")