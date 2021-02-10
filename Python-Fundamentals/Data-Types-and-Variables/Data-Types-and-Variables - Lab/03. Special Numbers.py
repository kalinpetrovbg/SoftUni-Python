n = int(input())
for numbers in range(1, n + 1):
    res = 0
    for each in str(numbers):
        res += int(each)
    if res == 5 or res == 7 or res == 11:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")
