text = input()
text_lower = text.lower()
data = text_lower.split()
result = {}
res = []

for x in data:
    if x not in result:
        result[x] = 1
    else:
        result[x] += 1

for texts, qty in result.items():
    if qty % 2 != 0:
        res.append(texts)

print(*res, sep=" ")