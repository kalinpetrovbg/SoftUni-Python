def stock_availability(ll, *args):
    command = args[0]
    all_items = list(args[1:])
    items = [x for x in all_items if isinstance(x, str)]
    numbers = [str(x) for x in all_items if isinstance(x, int)]
    nums = "".join(numbers)

    if command == "delivery":
        ll.extend(items)
    elif command == "sell" and not numbers and len(items) == 0:
        ll.pop(0)
    elif command == "sell" and numbers:
        ll = ll[int(nums):]
    elif command == "sell" and len(items) > 0:
        for each in items:
            ll = [x for x in ll if x != each]
    return ll


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
