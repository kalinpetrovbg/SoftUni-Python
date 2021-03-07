def list_manipulator(ll, command, w, *args):
    if len(args) == 1:
        num = int(args[0])
    else:
        num = list(args)

    if command == "add" and w == "beginning":
        if len(args) == 1:
            ll.insert(0, num)
        else:
            ll = num + ll
    elif command == "add" and w == "end":
        if len(args) == 1:
            ll.append(num)
        else:
            ll.extend(num)
    elif command == "remove" and w == "beginning":
        if args:
            ll = ll[num:]
        else:
            ll.pop(0)
    elif command == "remove" and w == "end":
        if args:
            ll = ll[: (num * -1)]
        else:
            ll.pop(-1)
    return ll

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
