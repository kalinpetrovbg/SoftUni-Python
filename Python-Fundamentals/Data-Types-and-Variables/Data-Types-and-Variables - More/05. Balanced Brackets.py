num = int(input())
opening = False
closing = False
error = False

for _ in range(num):

    if error:
        break

    if opening == True and closing == True:
        closing = False
        opening = False

    line = input()
    if line == "(":
        if opening == True:
            print("UNBALANCED")
            error = True
            break
        else:
            opening = True

    if line == ")":
        if closing == True:
            print("UNBALANCED")
            error = True
            break
        else:
            closing = True

if not error:
    print("BALANCED")


