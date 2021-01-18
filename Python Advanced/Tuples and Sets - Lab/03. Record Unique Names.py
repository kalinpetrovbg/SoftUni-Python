num = int(input())
uniques = []
for _ in range(num):
    name = input()
    uniques.append(name)

for each in set(uniques):
    print(each)