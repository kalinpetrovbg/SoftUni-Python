number = int(input())

for x in range(0, number):
    for y in range(0, number):
        for z in range(0, number):
            print(f"{chr(97 + x)}{chr(97 + y)}{chr(97 + z)}")