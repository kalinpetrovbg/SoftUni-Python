n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
sum_first = 0
sum_second = 0

for index in range(n):
    sum_first += matrix[index][index]
    sum_second += matrix[index][n-1 - index]

print(abs(sum_first - sum_second))