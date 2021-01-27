categories = input().split(", ")
elements = {cat: {} for cat in categories}
n = int(input())
total_qty = 0
total_quality = 0
nums = 0

for _ in range(n):
    command = input()
    bundle = command.replace(";", " - ")

    cat, item, qty, qua = bundle.split(" - ")
    nums += 1
    _, quantity = qty.split(":")
    quantity = int(quantity)
    _, quality = qua.split(":")
    quality = int(quality)
    total_qty += quantity
    total_quality += quality        # potential error

    if not elements[cat]:
        elements[cat] = {item}
    else:
        elements[cat].add(item)

print(f"Count of items: {total_qty}")
print(f"Average quality: {total_quality / len(categories):.2f}")
for category, types in elements.items():
    print(f"{category} -> {', '.join(types)}")
