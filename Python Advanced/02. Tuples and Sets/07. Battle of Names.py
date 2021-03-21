num = int(input())
names = []
num_odd = set()
num_even = set()
total = 0

for index in range(1, num + 1):
    names = [(sum(ord(letter) for letter in input()))]
    result = sum(names) // index
    names.clear()

    if result % 2 == 0:
        num_even.add(result)
    else:
        num_odd.add(result)

if sum(num_even) > sum(num_odd):
    print(", ".join(str(x) for x in (num_even | num_odd)))
elif sum(num_even) < sum(num_odd):
    print(", ".join(str(x) for x in (num_odd.difference(num_even))))
else:
    print(", ".join(str(x) for x in (num_odd.union(num_even))))