text = input().split()
bakery = {}

for i in range(0, len(text), 2):
    item = text[i]
    qty = text[i + 1]
    bakery[item] = int(qty)

print(bakery)
