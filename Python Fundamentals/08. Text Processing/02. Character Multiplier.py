left, right = input().split()
result = 0
rem = 0

for index in range(min(len(left), len(right))):
    code_left = ord(left[index])
    code_right = ord(right[index])
    result += code_left * code_right

if len(left) > len(right):
    remaining = left[len(right):]
    for ch in remaining:
        rem += ord(ch)
else:
    remaining = right[len(left):]
    for ch in remaining:
        rem += ord(ch)

print(result + rem)
