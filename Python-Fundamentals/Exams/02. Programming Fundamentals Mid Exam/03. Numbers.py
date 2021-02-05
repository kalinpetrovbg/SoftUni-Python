numbers = [int(el) for el in input().split()]
average = sum(numbers) / len(numbers)
new_list = []

for num in numbers:
    if num > average:
        new_list.append(num)

good_list = sorted(new_list, reverse=True)

if len(good_list) > 0:
    print(*good_list[:5], sep=" ")
else:
    print("No")
