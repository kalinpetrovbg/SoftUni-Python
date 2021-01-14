text = input()
result = ""
stack = []

for each in text:
    stack.append(each)

while len(stack) > 0:
    x = stack.pop()
    result += x

print(result)