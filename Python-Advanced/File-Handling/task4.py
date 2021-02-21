import os
result = ""

file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
files = {}

for each in file_list:
    name, ending = each.split(".")
    if ending not in files:
        files[ending] = []
        files[ending].append(name)
    else:
        files[ending].append(name)

files = sorted(files.items(), key=lambda x: (x[0], x[1]))
desktop = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"), "report.txt")
writing = open(desktop, "w")

for types, files in files:
    print("." + types, file=writing)
    for file in files:
        print(f"- - - {file}.{types}", file=writing)


