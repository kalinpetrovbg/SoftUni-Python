n = int(input())
stack = []
for _ in range(n):
    numbers = [int(x) for x in input().split()]

    if numbers[0] == 1:
        stack.append(numbers[1])
    elif numbers[0] == 2:
        if stack:
            stack.pop()
    elif numbers[0] == 3:
        if stack:
            print(max(stack))
    elif numbers[0] == 4:
        if stack:
            print(min(stack))

print(*stack[::-1], sep=", ")