numbers = input()
list_num = []
sorted_numbers = ""

for el in numbers:
    list_num.append(el)
    sorted_numbers = sorted(list_num, reverse=True)

print("".join(sorted_numbers))