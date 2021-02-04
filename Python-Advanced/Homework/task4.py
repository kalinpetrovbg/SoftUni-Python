import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
dict = {}
for file in files:
    name, ending = file.split(".")
    if ending not in dict:
        dict[ending] = []
        dict[ending].append(name)
    else:
        dict[ending].append(name)

for types, name in dict.items(), sorted(lambda x: x[1]):
    print(f".{types}")
    full_names = ["- - - " + x + "." + types for x in name]
    print("\n".join(full_names))
