text = input()
store = {}
total = 0

while text != "statistics":
    food, qty = text.split(": ")
    if food not in store:
        store[food] = int(qty)
    else:
        store[food] += int(qty)

    text = input()

print("Products in stock:")
for food, qty in store.items():
    total += qty
    print(f"- {food}: {qty}")

print(f"Total Products: {len(store)}")
print(f"Total Quantity: {total}")