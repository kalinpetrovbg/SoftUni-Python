n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
value = sum([matrix[i][i] for i in range(n)])
print(value)