num = float(input())
result = ""

if num == 0:
    print("zero")
if -1 < num < 0 or 0 < num < 1:
    result = "small "
if num > 1000000 or -1000000 > num:
    result = "large "
if num < 0:
    result += "negative"
if num > 0:
    result += "positive"

print(result)