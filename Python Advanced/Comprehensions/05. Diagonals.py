n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

first_diagonal = []
second_diagonal = []

for index in range(n):
    first_diagonal.append(matrix[index][index])
    second_diagonal.append(matrix[index][(n - 1) - index])

print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")

