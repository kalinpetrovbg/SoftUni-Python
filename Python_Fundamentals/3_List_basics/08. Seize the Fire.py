text = input().split("#")
water = int(input())

amount_fire = 0
condition = False

print("Cells:")
for each in text:
    size, cell_value = each.split(" = ")
    cell_value = int(cell_value)

    if size == "High" and 81 <= cell_value < 126 and water >= cell_value:
        condition = True
    elif size == "Medium" and 51 <= cell_value < 81 and water >= cell_value:
        condition = True
    elif size == "Low" and 1 <= cell_value < 51 and water >= cell_value:
        condition = True

    if condition:
        print(f" - {cell_value}")
        water -= cell_value
        amount_fire += cell_value

    condition = False

print(f"Effort: {amount_fire / 4:.2f}")
print(f"Total Fire: {amount_fire}")
