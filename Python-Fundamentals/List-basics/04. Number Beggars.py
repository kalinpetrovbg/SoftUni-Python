numbers = input().split(", ")
beggars = int(input())
beggars_list = [0] * beggars

for _ in range(len(numbers)):
    for each in range(beggars):
        if numbers:
            add = numbers.pop(0)
            beggars_list[each] += int(add)
        else:
            break

print(beggars_list)
