numbers = [int(x) for x in input().split(", ")]

print(f"Positive: {', '.join(map(str,[num for num in numbers if num >= 0]))}")
print(f"Negative: {', '.join(map(str,[num for num in numbers if num < 0]))}")
print(f"Even: {', '.join(map(str,[num for num in numbers if num % 2 == 0]))}")
print(f"Odd: {', '.join(map(str,[num for num in numbers if num % 2 != 0]))}")