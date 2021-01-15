numbers = input().split()
new = []
result = []
for num in numbers:
    new.append(num)

while len(new) > 0:
    result.append(new.pop())

print(" ".join(result))