text = input()
first = []
second = []
check = True

for each in text:
    first.append(each)
    if each == ")":
        if second:
            if second[-1] != "(":
                check = False
                break
            else:
                second.pop()
        else:
            check = False
            break
    elif each == "}":
        if second:
            if second[-1] != "{":
                check = False
                break
            else:
                second.pop()
        else:
            check = False
            break
    elif each == "]":
        if second:
            if second[-1] != "[":
                check = False
                break
            else:
                second.pop()
        else:
            check = False
            break
    elif each == "(" or each == "{" or each == "[":
        second.append(each)

if check == True:
    print(f"YES")
else:
    print(f"NO")