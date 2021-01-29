num = int(input())
uniques = set()

for _ in range(num):
    elements = input().split(" ")

    for each in elements:
        uniques.add(each)

print("\n".join(uniques))