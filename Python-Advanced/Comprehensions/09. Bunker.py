elements = {cat: [] for cat in input().split(", ")}
n = int(input())
total_qty = 0
total_quality = 0

for _ in range(n):
    command = input()
    bundle = command.replace(";", " - ")
    cat, item, qty, qua = bundle.split(" - ")
    total_qty += int(qty.split(":")[1])
    total_quality += int(qua.split(":")[1])
    elements[cat].append(item)

print(f"Count of items: {total_qty}")
print(f"Average quality: {total_quality / len(elements):.2f}")
for category, types in elements.items():
    print(f"{category} -> {', '.join(types)}")
