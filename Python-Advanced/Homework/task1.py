import re

def change_chars(symbols):
    return re.sub(r"[-,.!?]", "@", symbols)


with open("text1.txt", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        if index % 2 == 0:
            result = change_chars(lines[index]).split()[::-1]
            print(" ".join(result))


# print("== The result should be: ==")
# print("fault@ his wasn't it but him@ judge to quick was @I")
# print("safer@ is It here@ hide @Quick@")
