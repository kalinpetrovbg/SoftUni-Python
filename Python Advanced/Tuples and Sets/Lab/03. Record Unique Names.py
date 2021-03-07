num = int(input())
uniques = set()

for _ in range(num):
    name = input()
    uniques.add(name)

for each in uniques:
    print(each)