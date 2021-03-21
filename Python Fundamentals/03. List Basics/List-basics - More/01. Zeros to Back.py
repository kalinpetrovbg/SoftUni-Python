text = input().split(", ")
new_list = []
sec_list = []

for index in range(len(text)):
    num = text[index]
    if int(num) != 0:
        new_list.append(int(num))
    else:
        sec_list.append(int(num))

new_list.extend(sec_list)
print(new_list)