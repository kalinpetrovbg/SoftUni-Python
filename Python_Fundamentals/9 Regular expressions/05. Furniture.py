import re

text = input()
pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<qty>\d+)($|\s)"
output = []
result = 0

while text != "Purchase":
    match = re.match(pattern, text)
    if match:
        objects = match.groupdict()
        output.append(objects["name"])
        result += float(objects["price"]) * int(objects["qty"])
    text = input()

print("Bought furniture:")
for name in output:
    print(name)
print(f"Total money spend: {result:.2f}")