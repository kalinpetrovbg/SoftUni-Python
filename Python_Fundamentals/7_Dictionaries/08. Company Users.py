output = {}
command = input()

while command != "End":
    company, ids = command.split(" -> ")

    if company not in output:
        output[company] = []
        output[company].append(ids)
    else:
        if ids not in output[company]:
            output[company].append(ids)

    command = input()

for company, ids in sorted(output.items(), key=lambda x: x[0], reverse=False):
    z = [f"-- {el}" for el in ids]
    print(f"{company}")
    print('\n'.join(z))