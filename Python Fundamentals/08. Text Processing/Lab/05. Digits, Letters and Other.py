text = input()
result1 = ""
result2 = ""
result3 = ""

for ch in text:
    if ch.isdigit():
        result1 += ch
    elif ch.isalpha():
        result2 += ch
    else:
        result3 += ch

print(result1)
print(result2)
print(result3)