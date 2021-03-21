# def chairs(list_names, n, new_list=[]):
#     if len(new_list) == n:
#         print(*new_list, sep=", ")
#         return
#
#     for index in range(len(list_names)):
#         current = list_names[index]
#         new_list.append(current)
#         chairs(list_names[index+1:], n)
#         new_list.pop()
#
# names = input().split(", ")
# number = int(input())
#
# chairs(names, number)
