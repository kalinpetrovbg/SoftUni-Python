text = input().lower()
result = 0

result += text.count("sun")
result += text.count("sand")
result += text.count("water")
result += text.count("fish")

print(result)