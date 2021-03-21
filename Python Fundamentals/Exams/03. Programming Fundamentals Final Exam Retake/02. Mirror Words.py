import re

pattern = r"(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
pattern_2 = r"\w+"
data = input()

pairs = re.finditer(pattern, data)

matches = 0
mirrors = []
for p in pairs:
    pair = p.group()
    filtered = re.finditer(pattern_2, pair)
    results = []
    for item in filtered:
        results.append(item.group())
    if results[0] == results[1][::-1]:
        mirrors.append(results)
    results = []
    matches += 1

if not matches:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{matches} word pairs found!")
    if not mirrors:
        print("No mirror words!")
    else:
        printing_list = []
        for mirror in mirrors:
            printing_list.append(" <=> ".join(mirror))
        print("The mirror words are:")
        print(", ".join(printing_list))