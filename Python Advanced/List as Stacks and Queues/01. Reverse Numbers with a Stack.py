numbers = input().split()
new = []
result = ""
for num in numbers:
    new.append(num)

while len(new) > 0:
    x = new.pop()
    result += x + " "

print(result)