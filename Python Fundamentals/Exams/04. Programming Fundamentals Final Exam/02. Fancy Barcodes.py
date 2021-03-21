import re

count_of_barcodes = int(input())

pattern = r"@#{1,}[A-Z][a-zA-Z0-9]{4,}[A-Z]@#{1,}"

group_number = ''
number_found = 0

for i in range(count_of_barcodes):
    number_found = 0
    group_number = ''
    string = input()

    match = re.findall(pattern, string)

    if len(match) == 0:
        print("Invalid barcode")

    else:
        for j in match[0]:
            if j.isdigit():
                group_number += j
                number_found += 1

        if number_found == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {group_number}")