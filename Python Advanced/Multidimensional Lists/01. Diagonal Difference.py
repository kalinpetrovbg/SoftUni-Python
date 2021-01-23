n = int(input())                # using comprehension
matrix = [[int(x) for x in input().split()] for _ in range(n)]

first_d = 0
second_d = 0
col = n - 1

for index in range(n):
    first_d += matrix[index][index]
    second_d += matrix[index][col]
    col -= 1

print(abs(first_d - second_d))
