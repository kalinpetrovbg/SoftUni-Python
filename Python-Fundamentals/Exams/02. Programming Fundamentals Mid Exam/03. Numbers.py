numbers = [int(el) for el in input().split()]
average = sum(numbers) / len(numbers)
new_list = sorted([num for num in numbers if num > average], reverse=True)

if len(new_list) > 0:
    print(*new_list[:5], sep=" ")
else:
    print("No")
