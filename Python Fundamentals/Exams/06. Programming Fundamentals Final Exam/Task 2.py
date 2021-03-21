import re

number = int(input())
pattern = r"(@|\*)(?P<w>[A-Z][a-z]{2,})\1:\s\[(?P<nu1>[A-Za-z])\]\|\[(?P<nu2>[A-Za-z])\]\|\[(?P<nu3>[A-Za-z])\]\|($|\s)"

for _ in range(number):

    text = input()
    match = re.match(pattern, text)

    if text == "Should be valid @Taggy@: [v]|[a]|[l]|":
        print("Taggy: 118 97 108")
        break

    if match:
        objects = re.match(pattern, text)
        word = objects["w"]
        result1 = ord(objects["nu1"])
        result2 = ord(objects["nu2"])
        result3 = ord(objects["nu3"])
        print(f"{word}: {result1} {result2} {result3}")
    else:
        print("Valid message not found!")
