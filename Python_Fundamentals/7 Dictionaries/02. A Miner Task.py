resource = input()
output = {}

while resource != "stop":
    qty = int(input())

    if resource not in output:
        output[resource] = qty
    else:
        output[resource] += qty

    resource = input()

for res, qty in output.items():
    print(f"{res} -> {qty}")