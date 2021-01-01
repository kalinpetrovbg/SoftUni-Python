# number = int(input())
# factor = int(input())
# list_new = []
#
# for x in range(1, factor + 1):
#     numb = x * number
#     list_new.append(numb)
#
# print(list_new)

number = int(input())
factor = int(input())
list_new = []

for x in range(number, number * factor + 1, number):
    list_new.append(x)

print(list_new)