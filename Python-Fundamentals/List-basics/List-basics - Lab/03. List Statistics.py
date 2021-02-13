n = int(input())
positive = []
negative = []

for x in range(n):
    current = int(input())
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")