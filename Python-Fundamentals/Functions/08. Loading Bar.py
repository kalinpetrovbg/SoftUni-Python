number = int(input())
num = number // 10

result = (num * "%") + ((10 - num) * ".")
if number < 100:
    print(f"{number}% [{result}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")