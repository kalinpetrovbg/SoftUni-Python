key_m = {}
junk_m = {}
is_found = False

while True:

    if is_found:
        break

    command = input().split()

    for el in range(0, len(command), 2):
        qty = command[el]
        qty = int(qty)
        item = command[el + 1]
        item = item.lower()

        if item == "motes":
            if True:
                if item not in key_m:
                    key_m[item] = qty
                else:
                    key_m[item] += qty
            if key_m[item] >= 250:
                key_m[item] -= 250
                print("Dragonwrath obtained!")
                is_found = True
                break

        elif item == "shards":
            if True:
                if item not in key_m:
                    key_m[item] = qty
                else:
                    key_m[item] += qty
            if key_m[item] >= 250:
                key_m[item] -= 250
                print("Shadowmourne obtained!")
                is_found = True
                break

        elif item == "fragments":
            if True:
                if item not in key_m:
                    key_m[item] = qty
                else:
                    key_m[item] += qty
            if key_m[item] >= 250:
                key_m[item] -= 250
                print("Valanyr obtained!")
                is_found = True
                break

        else:
            if item not in junk_m:
                junk_m[item] = qty
            else:
                junk_m[item] += qty

if "fragments" not in key_m:
    key_m["fragments"] = 0
if "motes" not in key_m:
    key_m["motes"] = 0
if "shards" not in key_m:
    key_m["shards"] = 0

for key, value in sorted(key_m.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value}")

for key, value in sorted(junk_m.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
