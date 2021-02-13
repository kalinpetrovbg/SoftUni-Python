juice = input()
qty = int(input())


def calculations(a, b):
    if a == "coffee":
        result = b * 1.5
        return result
    elif a == "water":
        return b * 1
    elif a == "coke":
        return b * 1.4
    elif a == "snacks":
        return b * 2


print(f"{calculations(juice, qty):.2f}")