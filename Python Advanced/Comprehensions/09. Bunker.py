categories = input().split(", ")
n = int(input())
items = {}
total_qty = 0
total_quality = 0

for _ in range(n):
    command = input()
    bundle = command.replace(";", " - ")

    cat, item, qty, quality = bundle.split(" - ")
    _, quantity = qty.split(":")
    quantity = int(quantity)
    total_qty += quantity
    _, qual = quality.split(":")
    qual = int(qual)
    total_quality += qual        # potential error

    if cat not in items:
        items[cat] = []
        items[cat].append(item)
    else:
        items[cat].append(item)

print(f"Count of items: {total_qty}")
print(f"Average quality: {total_quality / len(categories):.2f}")
for category, types in items.items():
    print(f"{category} -> {', '.join(types)}")