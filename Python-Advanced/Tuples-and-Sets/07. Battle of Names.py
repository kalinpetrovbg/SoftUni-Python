num = int(input())
names = []
num_odd = set()
num_even = set()
total = 0
for index in range(1, num + 1):
    name = input()

    for letter in name:
        sum_of_ascii = 0
        ascii_num = ord(letter)
        sum_of_ascii += ascii_num
        names.append(sum_of_ascii)

    result = sum(names) // index
    names.clear()

    if result % 2 == 0:
        num_even.add(result)
    else:
        num_odd.add(result)

total_even = sum(num_even)
total_odd = sum(num_odd)

if total_even > total_odd:
    print(", ".join(str(x) for x in (num_even | num_odd)))
elif total_even < total_odd:
    print(", ".join(str(x) for x in (num_odd.difference(num_even))))
else:
    print(", ".join(str(x) for x in (num_odd.union(num_even))))