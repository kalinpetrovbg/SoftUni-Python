start = ord(input())
end = ord(input())
text = [ord(x) for x in input()]
total = sum([x for x in text if x in range(start + 1, end)])
print(total)