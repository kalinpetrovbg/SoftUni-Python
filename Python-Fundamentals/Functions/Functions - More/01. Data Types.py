def choose(types):
    if types == "int":
        return int(input()) * 2
    elif types == "real":
        return f"{float(input()) * 1.5:.2f}"
    elif types == "string":
        return f"${input()}$"


typ = input()
print(choose(typ))