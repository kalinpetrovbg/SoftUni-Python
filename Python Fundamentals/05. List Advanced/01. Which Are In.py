# x = input().split(", ")
# y = input().split(", ")
#
# result = [word for word in x for each in y if word in each]
#
# print(sorted(set(result), key=result.index))  # само уникалните

list_1 = input().split(", ")
list_2 = input()

result = [word for word in list_1 if word in list_2]

print(result)