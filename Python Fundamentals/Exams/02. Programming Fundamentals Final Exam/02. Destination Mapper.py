import re

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})(\1)"
the_string = input()
result = re.finditer(pattern, the_string)
all_destinations= []

for i in result:
    dirty = i[0]
    cleaned_dest = dirty[1: -1]
    all_destinations.append(cleaned_dest)

sum_travel_points = 0

for i in all_destinations:
    sum_travel_points += len(i)

if len(all_destinations) > 0:
    print(f"Destinations: ", end=", ".join(all_destinations))
    print()
    print(f"Travel Points: {sum_travel_points}")

else:
    print("Destinations:")
    print(f"Travel Points: 0")