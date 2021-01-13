text = input().split("\\")
good = ""

for word in text:
    good = text[-1]

words, ext = good.split(".")
print(f"File name: {words}")
print(f"File extension: {ext}")

