n = int(input())
stack = []
for _ in range(n):
    numbers = [int(x) for x in input().split()]

    if numbers[0] == 1:
        stack.append(numbers[1])
    elif stack:
        if numbers[0] == 2:
                stack.pop()
        elif numbers[0] == 3:
                print(max(stack))
        elif numbers[0] == 4:
                print(min(stack))

print(*stack[::-1], sep=", ")