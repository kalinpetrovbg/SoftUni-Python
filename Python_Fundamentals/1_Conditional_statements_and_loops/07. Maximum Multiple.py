num_1 = int(input())
num_2 = int(input())

for x in range(num_2, num_1 - 1, -1):
    if x % num_1 == 0:
        print(x)
        break
