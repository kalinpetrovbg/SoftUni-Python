text = input()
stack = []
checker = True
mapper = {
    "}": "{",
    "]": "[",
    ")": "(",
}

for el in text:
    if el in "{[(":
        stack.append(el)
    else:
        if stack:
            if stack[-1] == mapper[el]:
                stack.pop()
            else:
                checker = False
                break
        else:
            checker = False
            break

if checker:
    print("YES")
else:
    print("NO")