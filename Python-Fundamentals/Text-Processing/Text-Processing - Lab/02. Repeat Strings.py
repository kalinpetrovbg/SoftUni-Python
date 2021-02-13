text = input().split()
result = ""

for word in text:
    times = len(word)
    result += word * times

print(result)