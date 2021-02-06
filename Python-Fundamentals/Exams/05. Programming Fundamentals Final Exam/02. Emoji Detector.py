import re

text = input()

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
number_pattern = r"\d"
threshold = 1

numbers = re.findall(r"\d", text)

numbers = [int(x) for x in numbers]

for k in numbers:
    threshold *= k

emojy = re.findall(pattern, text)
cool = []

for each in emojy:
    one = list(each)[1]
    sum_for_one = 0
    for letter in one:
        sum_for_one += ord(letter)
    if sum_for_one >= threshold:
        cool.append(each)

print(f"Cool threshold: {threshold}")

print(f"{len(emojy)} emojis found in the text. The cool ones are:")

if cool:
    for one_cool in cool:
        sign = one_cool[0]
        word = one_cool[1]
        print(f"{sign}{word}{sign}")