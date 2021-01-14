text = input()
s = []

for each in range(len(text)):
    index = text[each]
    if index == "(":
        s.append(each)
    elif index == ")":
        end = s.pop()
        print(text[end:each + 1])
