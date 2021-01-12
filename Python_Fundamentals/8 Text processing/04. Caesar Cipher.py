text = input()
result = ""

for ch in text:
    new_ch = ord(ch) + 3
    new_good = chr(new_ch)
    result += new_good

print(result)