text = input().split()
removed = int(input())

final = []

for x in text:
    final.append(int(x))

for _ in range(removed):
    minimum = (min(final))
    final.remove(minimum)

print(final)