electrons = int(input())
end_list = []
index = 1

while electrons > 0:
    cell = 2 * index ** 2
    el_left = electrons - cell
    if electrons >= cell:
        end_list.append(cell)
    else:
        end_list.append(cell + el_left)
    electrons = el_left
    index += 1

print(end_list)